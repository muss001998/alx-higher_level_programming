#!/usr/bin/node

// to Import the 'request' module.
const request = require('request');

//to Construct the URL for the specific Star Wars film
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

//to Use the 'request' module to perform an HTTP GET request to the constructed URL.
request(url, function (error, response, body) {
  // to log title if successful, log error if not.
  console.log(error || JSON.parse(body).title);
});
