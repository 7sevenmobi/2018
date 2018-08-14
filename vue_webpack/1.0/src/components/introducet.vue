<template>
  <div class="introducet">
    <h2>{{msg}}</h2>
    <p>有个问题：如果不是通过锚链接方式 跳转到此页面，参数将无法传输<p>
    <!--接收参数-->
    <p>{{$route.params.id}}---{{$route.params.username}}</p>
    
  </div>
</template>

<script>
export default {
  name: 'introducet',
  data () {
    return {
      msg: '我是introducet页面'
    }
  }
}
</script>

<style>
</style>
