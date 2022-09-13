#!/usr/bin/node

const axios = require('axios').default;

const url = 'https://swapi-api.hbtn.io/api/films/';

axios.get(url + process.argv[2])
  .then(function (response) {
    // handle success
    console.log(response.data.title);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
