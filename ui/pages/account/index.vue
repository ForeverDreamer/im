<template>
  <el-container>
    <el-aside width="400px">
      <aside-room />
    </el-aside>
    <el-main>
      <main-account ref="roomDialog" />
    </el-main>
  </el-container>
</template>

<script>
// import { mapMutations, mapActions } from 'vuex'
import AsideRoom from '~/components/aside/room'
import MainAccount from '~/components/main/account'

export default {
  name: 'Index',
  components: {
    AsideRoom,
    MainAccount,
  },
  // data() {
  //   return {
  //     socket: null,
  //   }
  // },
  created() {},
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
