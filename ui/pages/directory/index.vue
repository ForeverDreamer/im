<template>
  <el-container>
    <el-aside width="400px">
      <aside-room />
    </el-aside>
    <el-main>
      <main-directory ref="roomDialog" />
    </el-main>
  </el-container>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'
import AsideRoom from '~/components/aside/room'
import MainDirectory from '~/components/main/directory'

export default {
  name: 'Index',
  components: {
    AsideRoom,
    MainDirectory,
  },
  data() {
    return {
      socket: null,
    }
  },
  created() {
    // this.initStore(`${this.$conf.apiVersion}/auth/login`).then(() => {
    //   this.initChat()
    // })
  },
  methods: {
    ...mapMutations({
      updateUser: 'home/updateUser',
      updateRoom: 'home/updateRoom',
      clearStore: 'home/clear',
    }),
    ...mapActions({
      initStore: 'home/initStore',
    }),
    // handleClick(e) {
    //   e.stopPropagation()
    // },
  },
}
</script>

<style scoped>
.room-tab__more {
  /*background: #37ff00;*/
}

.el-dropdown-link {
  cursor: pointer;
  color: #409eff;
}

.el-icon-arrow-down {
  font-size: 12px;
}
</style>
