const express = require('express')
const mysql = require('mysql')

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    port: 3307,
    database: "nodedemo"
})

db.connect(error => {
    if(error) {
        throw error
    }
    console.log('MySQL conected successfully')
})

const app = express()
const port = 3000

app.get('/createDB', (req, res) => {
    let sql = 'CREATE DATABASE if not exists nodeDemo'
    db.query(sql, error => {
        if (error) {
            throw error
        }
        res.sendStatus(201)
    })
})

app.get('/createTB', (req, res) => {
    let sql = 'CREATE TABLE if not exists employees (id int AUTO_INCREMENT, name VARCHAR(200), designation VARCHAR(255), PRIMARY KEY(id))'
    db.query(sql, error => {
        if (error) {
            throw error
        }
        res.sendStatus(201)
    })
})

app.get('/employee', (req, res) => {
    let post = {name: 'Ben Goldbridge', designation: 'Director'}
    let sql = 'INSERT INTO employees SET ?'
    db.query(sql, post, error => {
        if (error) {
            throw error
        }
        res.sendStatus(201)
    })
})

app.get('/employees', (req, res) => {
    let sql = 'SELECT * FROM employees'
    db.query(sql, (error, results) => {
        if (error) {
            throw error
        }
        res.json(results)
    })
})

app.get('/update/:id', (req, res) => {
    let newName = 'Mark Golbridge';
    let sql = `UPDATE employees SET name = ? WHERE id = ?`;
    db.query(sql, [newName, req.params.id], (error, results) => {
        if (error) {
            throw error;
        }
        res.sendStatus(204);
    });
});

app.get('/delete/:id', (req, res) => {
    let sql = `DELETE FROM employees WHERE id = ?`;
    db.query(sql, req.params.id, (error, results) => {
        if (error) {
            throw error;
        }
        res.sendStatus(204);
    });
});

app.listen(port, () => {
    console.log(`Running on port ${port}`)
})