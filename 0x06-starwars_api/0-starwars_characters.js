#!/usr/bin/node
/*
* we need to get all character names of a certain movie
* call https://swapi-api.alx-tools.com/api/films/{FILM ID}/
* it returns a json with [characters] = list of urls
* for every url:
* request it
* it returns a json with ['name']
* print that.
* loop again.
* */
const request = require('request');

async function printCharacterNames (filmID) {
  request(`https://swapi-api.alx-tools.com/api/films/${filmID}/`,
    async function (error, response, body) {
      if (error) throw error;
      const characterUrls = JSON.parse(body).characters;
      const characterPromises = characterUrls.map(url => {
        return new Promise((resolve, reject) => {
          request(url, function (error, response, body) {
            if (error) {
              reject(error);
            } else {
              resolve(JSON.parse(body).name);
            }
          });
        });
      });
      const characterNames = await Promise.all(characterPromises);
      characterNames.forEach(name => console.log(name));
    });
}

printCharacterNames(process.argv[2]);
