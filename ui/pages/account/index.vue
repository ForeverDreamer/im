<template>
  <el-container>
    <el-aside width="400px">
      <aside-room :socket="socket" />
    </el-aside>
    <el-main>
      <main-account ref="roomDialog" :socket="socket"></main-account>
    </el-main>
  </el-container>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'
import AsideRoom from '~/components/aside/room'
import MainAccount from '~/components/main/account'

export default {
  name: 'Index',
  components: {
    AsideRoom,
    MainAccount,
  },
  data() {
    return {
      socket: null,
    }
  },
  created() {
    this.initStore(`${this.$conf.apiVersion}/auth/login`).then(() => {
      this.initChat()
    })
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
    initChat() {
      this.socket = this.$socketIo(this.$conf.socketIoUrl, {
        // path: '/chat/',
      })
      this.socket.on('connect', () => {
        console.log('连接成功')
      })
      this.socket.on('disconnect', () => {
        console.log('服务端断开连接, 请登录后操作')
      })
      // const callback = () => console.log('消息收到')
      this.socket.on('msg', (data, callback) => {
        console.log('收到消息：' + data)
        this.$refs.roomDialog.fetchRoomMessages()
        if (callback) {
          callback()
        }
      })
      this.socket.on('enter_room', () => {
        console.log('socket enter_room')
        this.$refs.roomDialog.fetchRoomMessages()
      })
      this.socket.on('leave_room', () => {
        console.log('socket leave_room')
        this.initStore(`${this.$conf.apiVersion}/auth/login`)
      })
      this.socket.on('error', (err) => {
        console.log(err.code)
        console.log(err.msg)
      })
    },
  },
}
</script>

<style scoped>
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #2f343d;
  color: #333;
  text-align: center;
  /*line-height: 200px;*/
}

.el-main {
  background-color: #f2f3f5;
  color: #333;
  text-align: center;
  /*line-height: 160px;*/
  position: relative;
  padding: 0;
}

.el-container {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  padding-right: 10px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

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
