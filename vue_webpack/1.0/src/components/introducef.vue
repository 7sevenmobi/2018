<template>
  <div class="introducef">
    <h2>{{msg}}</h2>
    <p>{{$route.params.userId}}---{{$route.params.userName}}</p>
  </div>
</template>

<script>
export default {
  name: 'introducef',
  data () {
    return {
      msg: '我是introducef页面'
    }
  }
}
</script>

<style>
</style>
