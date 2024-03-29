#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
const dict = {};

axios.get(url)
  .then(function (response) {
    // handle success
    const results = response.data;
    for (const i in results) {
      const task = results[i];
      if (task.completed === true) {
        if (!(task.userId in dict)) {
          dict[task.userId] = 0;
        }
        dict[task.userId] += 1;
      }
    }
    console.log(dict);
  })
  .catch(function (err) {
    // handle error
    console.log(err);
  })
  .then(function () {
    // always executed
  });
