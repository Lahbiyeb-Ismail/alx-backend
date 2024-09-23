function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // biome-ignore lint/complexity/noForEach: <explanation>
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id || 'test mode'}`);
        }
      });

    job.on('complete', () => {
      console.log(`Notification job ${job.id || 'test mode'} completed`);
    }).on('failed', (err) => {
      console.log(`Notification job ${job.id || 'test mode'} failed: ${err}`);
    }).on('progress', (progress) => {
      console.log(`Notification job ${job.id || 'test mode'} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
