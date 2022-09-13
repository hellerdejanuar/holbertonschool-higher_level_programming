#!/usr/bin/node

const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(url)
  .then(function (response) {
    // handle success
    const charactersList = response.data.characters;
    for (const i in characters_list) {
      axios.get(charactersList[i])
        .then(function (character) {
          console.log(character.data.name);
        });
    }
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  });
