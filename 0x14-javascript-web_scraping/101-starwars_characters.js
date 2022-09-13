#!/usr/bin/node

const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(url)
  .then(async function (response) {
    // handle success
    const charactersList = response.data.characters;
    for (const i in charactersList) {
      await axios.get(charactersList[i])
        .then(function (character) {
          console.log(character.data.name);
        });
    }
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  });
