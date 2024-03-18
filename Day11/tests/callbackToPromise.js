const fs = require('fs');

function readFilePromise(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

readFilePromise('file.txt')
  .then(data => console.log('File data:', data))
  .catch(err => console.error('Error reading file:', err));