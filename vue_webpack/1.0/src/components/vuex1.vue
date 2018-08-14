<template>
    <div>
        <!-- <p>{{$store.state.count}}</p> -->
        <p>{{count}}</p>
        <p>
            <input type="button" value="+" @click="$store.commit('add',10)" />
            <input type="button" value="-" @click="reduce(5)" />
        </p>
        <p>
            <input type="button" value="异步+" @click="addAction(10)" />
            <input type="button" value="异步-" @click="reduceAction" />
        </p>
    </div>
</template>

<script>
    //mapState: 简化对变量的引用写法
    //mapMutations: 简化对mutation中的方法的引用写法
    //mapGetters: 简化对getters的引用写法
    //mapActions: 异步方法
    
    import store from "@/vuex/store"
    import {mapState,mapMutations,mapGetters,mapActions} from "vuex"
    export default {
        store,
        computed: {
            ...mapGetters(["count"]),       //对count执行getters里定义的方法
            ...mapState(["count"])          //对count进行读取。由于这里在getters的方法后执行，
        },                                  //所以重新渲染的效果就是: <p>0</p>
        methods: {
            ...mapMutations(["add","reduce"]),
            ...mapActions(["addAction","reduceAction"]),
        }
    }
</script>

<style>
</style>

