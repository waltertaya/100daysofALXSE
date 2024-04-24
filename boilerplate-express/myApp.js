let express = require('express');
let app = express();

// Register the public folder
app.use('/public', express.static(__dirname + '/public'))

app.get('/', (req, res) => {
	// res.send('Hello Express')

	absolutePath = __dirname + '/views/index.html'
	res.sendFile(absolutePath)
})

app.get('/api', (req, res) => {
	data = {
		"message": "Successfully reached the api"
	}
	res.json(data)
})

 module.exports = app;
