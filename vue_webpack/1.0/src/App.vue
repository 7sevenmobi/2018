
<!--这个是根组件-->

<template>
  <div id="app">
    <div class="header">
      <img src="./assets/logo.png" id="logopic">
      <div class="nav">
        <router-link to="/">首页</router-link>
        <router-link to="/introduce">简介</router-link>
        <input type="button" value="上一页" @click="goBack" />
        <input type="button" value="下一页" @click="goGo" />
        <input type="button" value="返回首页" @click="goHome" />
      </div>
    </div>
    <!--这里引入其他组件-->
    <router-view></router-view>
    <router-view name="footer"></router-view>
    <router-view name="vuex1"></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    goBack : function (){
      this.$router.go(-1);
    },
    goGo : function (){
      this.$router.go(1);
    },
    goHome : function (){
      this.$router.push("/");   //参数是跳转的目标路径
    },
  }
}
</script>

<style>
*{box-sizing:border-box;}
body{
  margin: 0;
  padding: 0;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  font-size: 10px;
  background-color: #f6f6f6;
}
a{
  color: #42b983;
}
#app{
  padding-top:4.6%;
  font-size: 1.6em;
  color: #000;
}
.header{position:fixed;top:0;width:100%;box-shadow:0 2px 2px;background-color:rgba(255,255,255);color:#e1e1e1;text-align:left;}
#logopic{vertical-align:middle;margin:0.3% 0.9%;width:4%;max-width:100%;}
.nav{display:inline-block;}
.nav a{display:inline-block;padding:0 1em;}
</style>
