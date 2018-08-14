import Vue from "vue"
import Vuex from "vuex"
Vue.use(Vuex);

const state = {
    count : 0
};

//对state的数据进行修改
//在 mutation 中混合异步调用会导致你的程序很难调试，所以在 Vuex 中，mutation 都是同步事务
const mutations = {
    add(state,m){   
        state.count+=m
    },
    reduce(state,n){     //接受参数
        state.count-=n
    }
};

//
const getters = {
    count (state){
        return "当前count值是："+state.count;
    }
};

//异步方法。使用异步方式，通过mutations修改state
const actions = {
    addAction (context){
        setTimeout(()=>{
            context.commit("add",10)
        },5000);
        console.log("我是addAction，我已经执行了，当前值是："+state.count);
    },
    reduceAction ({commit}){
        setTimeout(()=>{
            commit("reduce",5);
        },5000);
        console.log("我是reduceAction，我已经执行了，当前值是："+state.count);
    }
};

//模块组 ====================据说有很多坑，建议小项目不使用
//每个模块组里的参数可以重名
// const moduleA = {state,mutations,getters,actions};
// const moduleB = {state,mutations,getters,actions};
// export default new Vuex.Store({
//     modules : {
//         a : moduleA,
//         b : moduleB,
//         ..
//         ..
//         ..
//     }   
// })
//
//模板中调用：
//{{$store.state.a.count}}
//{{$store.state.b.count}}
//

export default new Vuex.Store({
    state,mutations,getters,actions
})