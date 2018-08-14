<template>
  <div class="introduce">
    <h2>{{msg}}</h2>

    <!-- 利用to动态传参 -->
    <router-link :to="{name:'introducet',params:{id:111,username:'to属性传参'}}">introducet</router-link>
    <!-- 利用URL动态传参 -->
    <router-link to="/introducef/222/URL传参">introducef</router-link>
    

    <!--添加transition标签，为模块 挂载和销毁 设置过渡效果-->
    <!-- 
      fade: 有4个class，分别是fade-enter、fade-enter-active、fade-leave、fade-leave-active，
      mode：有2个值，默认值in-out和out-in
     -->
    <transition name="fade" mode="out-in">
      <router-view></router-view>
    </transition>
  
  </div>
</template>

<script>
export default {
  name: 'introduce',
  data () {
    return {
      msg: '站主简介'
    }
  }
}
</script>

<style>
h1, h2 {
  font-weight: normal;
  color: #42b983;
}
a {
  color: #42b983;
}
.fade-enter{opacity:0;}
.fade-leave{opacity:1;}
.fade-enter-active{transition:opacity .5s;}
.fade-leave-active{opacity:0;transition:opacity .5s;}
</style>
