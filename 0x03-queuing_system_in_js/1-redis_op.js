import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err.toString()));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schooleName, value) {
  client.SET(schooleName, value, print);
}

async function displaySchoolValue(schooleName) {
  client.GET(schooleName, (_err, reply) => console.log(reply));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
