<template>
  <el-container>
    <el-aside width="400px">
      <aside-room />
    </el-aside>
    <el-main>
      <main-admin ref="roomDialog" />
    </el-main>
  </el-container>
</template>

<script>
// import { mapMutations, mapActions } from 'vuex'
import AsideRoom from '~/components/aside/room'
import MainAdmin from '~/components/main/admin'

export default {
  name: 'Index',
  components: {
    AsideRoom,
    MainAdmin,
  },
  // data() {
  //   return {
  //     socket: null,
  //   }
  // },
  created() {
    // this.initStore(`${this.$conf.apiVersion}/auth/login`).then(() => {
    //   this.initChat()
    // })
  },
  methods: {
    // ...mapMutations({
    //   updateUser: 'home/updateUser',
    //   updateRoom: 'home/updateRoom',
    //   clearStore: 'home/clear',
    // }),
    // ...mapActions({
    //   initStore: 'home/initStore',
    // }),
    // handleClick(e) {
    //   e.stopPropagation()
    // },
  },
}
</script>

<style scoped></style>
