var express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const utility = require('utility');

// connect database
let url = 'mongodb://localhost:27017';
let Schema = mongoose.Schema;
let ObjectId = Schema.ObjectId;

// 定义数据结构
let schema = new Schema({
  username: 'string',
  email: String,
  hide: Boolean,
  date: String
});
let Task = mongoose.model('Task',schema);


/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('users');
})
router.post('/',function(req,res,next){
    let uname = req.body.username.toString();
    let uemail = req.body.email.toString();
    let udate = new Date().toLocaleString();

    // 验证用户提交数据，验证通过则添加到数据库
    if(uname.length>0 && uname.length<20){
        mongoose.connect(url);
        Task.create({username:uname,email:uemail,date:udate});

        Task.find(function(err,docs){
            // md5加密
            console.log(utility.md5(uname),'md5');
            
            // docs.forEach(function(doc){
            //     doc.remove();
            // })

            res.send(docs);
        });
    }else{
        res.send('请重新填写');
    }

});

module.exports = router;
