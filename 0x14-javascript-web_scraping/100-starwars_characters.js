#!/usr/bin/node

const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/'+ process.argv[2];
let cn = 0;

axios.get(url)
  .then(function (response) {
    // handle success
    characters_list = response.data.characters;
    for (let i in characters_list) {
      axios.get(characters_list[i])
        .then(function (character) {
          console.log(character.data.name);
      });
    }
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  });
