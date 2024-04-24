#!/usr/bin/node

const request = require('request');
//to Import the 'request' module.

request.get(process.argv[2])
//to Use the 'request' module to perform an HTTP GET request to the URL.

  .on('response', function (response) {
    // to Set up an event listener for the 'response' event emitted by the HTTP request.

    console.log(`code: ${response.statusCode}`);
    // to Log the HTTP status code of the response to the console.
  });
