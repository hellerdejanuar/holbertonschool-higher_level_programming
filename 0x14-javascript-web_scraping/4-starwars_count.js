#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
let cn = 0;

axios.get(url)
  .then(function (response) {
    // handle success
    const movies = response.data.results;
    for (const i in movies) {
      for (const j in movies[i].characters) {
        if (movies[i].characters[j].includes('/18/')) {
          cn++;
        }
      }
    }
    console.log(cn);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
