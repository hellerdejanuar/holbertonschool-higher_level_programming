#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
let cn = 0;

axios.get(url)
  .then(function (response) {
    // handle success
    const movies = response.data.results
    for (i in movies) {

      if (movies[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        cn++;
      }
    }
    console.log(cn)
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
