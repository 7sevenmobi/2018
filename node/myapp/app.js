var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const mongoose = require('mongoose');

// require modules
var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

// connect database
let url = 'mongodb://localhost:27017';
let Schema = mongoose.Schema;
let ObjectId = Schema.ObjectId;

// 定义数据结构
let schema = new Schema({
  title: 'string',
  task: String,
  id: 'number',
  fork: 'number',
  comments: String,
  hide: Boolean
});
let Task = mongoose.model('Task',schema);

mongoose.connect(url);

// 数据库操作
Task.create({title: 'test1',fork: 12},{comments: 'comfjdklasfda',fork: 33232});
Task.find(function(err,docs){
  console.log(docs);
});


// Application
var app = express();


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
