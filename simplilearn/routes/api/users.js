const router = require('express').Router();
const { v4: uuidv4 } = require('uuid');

let users = require('../../Database/data');

router.get('/', (req, res) => {
  console.log(users);
  res.json(users);
});

router.get('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const found = users.some(user => user.id === id);

  if (found) {
    res.json(users.filter(user => user.id === id));
  } else {
    res.sendStatus(404);
  }
});

router.post('/', (req, res) => {
  const newUser = {
    id: uuidv4(),
    name: req.body.name,
    email: req.body.email
  };
  if (!newUser.name || !newUser.email) {
    res.sendStatus(400);
  }
  users.push(newUser);
  res.sendStatus(201);
});

router.put('/:id', (req, res) => {
  const found = users.some(user => user.id === parseInt(req.params.id));
  if (found) {
    const updateUser = req.body;
    users.forEach(user => {
      if (user.id === parseInt(req.params.id)) {
        user.name = updateUser.name ? updateUser.name : user.name;
        user.email = updateUser.email ? updateUser.email : user.email;
        res.sendStatus(204);
      }
    });
  }
});

router.delete('/:id', (req, res) => {
  const found = users.some(user => user.id === parseInt(req.params.id));
  if (found) {
    users = users.filter((user) => user.id !== parseInt(req.params.id));
    res.sendStatus(204);
  }
});

module.exports = router;
