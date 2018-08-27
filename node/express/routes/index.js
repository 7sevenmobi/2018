var express = require('express');
var router = express.Router();

let users = {
  uid : 0,
  uname : '7sevenmobi',
  pwd : '123',
  addr : 'wuhan'
}

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { user: users });
});

module.exports = router;
