import { promisify } from 'util';
import express from 'express';
import { createClient } from 'redis';
import { createQueue } from 'kue';

const app = express();
const port = 1245;

const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const queue = createQueue();

let reservationEnabled = true;

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? Number(seats, 10) : 0;
}

app.get('/available_seats', async (_req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat')
    .save((err) => {
      if (!err) {
        return res.json({ status: 'Reservation in process' });
      }
      return res.json({ status: 'Reservation failed' });
    });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get('/process', (_req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (_job, done) => {
    const currentSeats = await getCurrentAvailableSeats();

    if (currentSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }

    await reserveSeat(currentSeats - 1);

    if (currentSeats - 1 === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

app.listen(port, async () => {
  console.log(`Server listening on port ${port}`);
  await reserveSeat(50);
});
