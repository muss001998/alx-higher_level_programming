const fs = require('fs');
// this Import the built-in Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // this Use fs.readFile() to read the contents of a file specified as a command-line argument
  //the  'utf8' specifies the encoding of the file being read

  if (error) {
    // indicates If an error occurs during the file read operation, the 'error' parameter will contain an error object.
    console.error('Error reading the file:', error);

  } else {
    //indicates If the file is read successfully, the 'content' parameter will contain the contents of the file as a string.
    console.log(content);
  }
});
