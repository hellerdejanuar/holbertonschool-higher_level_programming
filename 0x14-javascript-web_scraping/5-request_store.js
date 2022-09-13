#!/usr/bin/node

const axios = require('axios').default;
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

axios.get(url)
  .then(function (response) {
    // handle success
    fs.writeFile(path, response.data, (error) => {
      if (error) throw error;
    });
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
