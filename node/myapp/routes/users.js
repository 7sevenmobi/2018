var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('users');
});

// why dont work?????????????????????????????
// router.post('/',function(req,res,next){
//   res.send(res.body);
// });

module.exports = router;
