import Vue from 'vue'
import Router from 'vue-router'
import error from '@/components/error'
import hello from '@/components/hello'
import introduce from '@/components/introduce'
import introducet from '@/components/introducet'
import introducef from '@/components/introducef'
import footer from '@/components/footer'
import vuex1 from '@/components/vuex1'

Vue.use(Router)

//配置路由
//mode：路由模式。有三个值history、hash（默认值）和abstract
//path：URL路径
//name：路由名称(可选)。对应父组件router-link的to参数
//component/components：import的组件
//redirect：重定向，例如：当链接路径为goParams时，将重定向跳转到params路径，并传递URL参数
//      {
//        path:'/params/:newsId(\\d+)/:newsTitle',
//        component:Params
//      },{
//        path:'/goParams/:newsId(\\d+)/:newsTitle',
//        redirect:'/params/:newsId(\\d+)/:newsTitle'
//      }
//alias：路径别名，例如：点击7seven后跳转到intro组件页面
//        <router-link to="/7seven">7seven</router-link>
//        {
//            path: '/intro',
//            component: intro,
//            alias:'/7seven'
//        }
//alias不要用在path为’/’中，是不起作用的。
//
//redirect：redirect是直接改变了url的值，把url变成了redirect的路径。
//alias：URL路径没有改变，还是真实链接路径，只是改变了<router-view>中的内容。这种情况更友好，让用户知道自己访问的路径。
//
//  
//    在路由文件中只能写一个beforeEnter钩子，但是组件中可以写两个钩子, 接收的参数和beforeEnter相同，分别是：
//      beforeRouteEnter：路由进入之前的行为
//      beforeRouteLeave：路由离开之前的行为
//
//    beforeEnter钩子函数：挂载组件之前的行为，参数如下：
//      to：对象，包含目标路径的信息
//      frome：对象，包含出发路径的信息
//      next：函数，决定了是否挂载当前组件，常用法：next(false)、next(true)
//
//    beforeEnter : (to,from,next)=>{
//      console.log("进入了introduce模板");
//      console.log(to);
//      console.log(from);
//      next();
//    }
//
//
export default new Router({
  mode: "history",
  routes: [
    {//404模块
      path: "*",
      component: error
    },{//单页面多路由
      path: '/',
      name: 'hello',
      components: {
        default: hello,
        footer: footer,
        vuex1: vuex1
      }
    },{//配置子路由
      path: "/introduce",
      name: "introduce",
      component: introduce,
      children: [
        {path: "/introducet",name:"introducet",component: introducet},
        //URL传参
        {path: "/introducef/:userId(\\d+)/:userName",name:"introducef",component: introducef}
      ]
    }
  ]
})