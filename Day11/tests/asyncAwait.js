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

async function readFileAsync(filePath) {
  try {
    const data = await readFilePromise(filePath);
    console.log('File data:', data);
  } catch (err) {
    console.error('Error reading file:', err);
  }
}

readFileAsync('file.txt');