<template>
  <div class="hello">
    <h3>{{ msg }}</h3>
    <ul>
      <li>
        <a href="https://www.baidu.com" target="_blank">百度</a>
      </li>
      <li>
        <a href="https://www.sougou.com" target="_blank">搜狗</a>
      </li>
      <li>
        <a href="https://www.bing.com" target="_blank">必应</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: '欢迎来到7seven的博客'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul{
  list-style-type:none;
  padding:0;
}
li{
  display:inline-block;
  margin:0 1em;
}
</style>
