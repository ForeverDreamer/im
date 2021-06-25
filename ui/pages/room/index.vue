<template>
  <div class="main-window">
    <aside-room class="main-window__aside" />
    <main-chat ref="roomDialog" class="main-window__content" />
    <!--    <div class="main-window__aside"></div>-->
    <!--    <div class="main-window__content"></div>-->
  </div>
  <!--  <el-container>-->
  <!--    <el-aside width="400px">-->
  <!--      <aside-room />-->
  <!--    </el-aside>-->
  <!--    <el-main>-->
  <!--      <main-chat ref="roomDialog" />-->
  <!--    </el-main>-->
  <!--  </el-container>-->
</template>

<script>
import { mapMutations, mapActions } from 'vuex'
import AsideRoom from '~/components/aside/room'
import MainChat from '~/components/main/chat'
// import { webSocket } from '~/lib/websocket'

export default {
  name: 'Index',
  components: {
    AsideRoom,
    MainChat,
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
    this.initChat()
  },
  methods: {
    ...mapMutations({
      updateUser: 'auth/updateUser',
      updateRoom: 'auth/updateRoom',
      clearStore: 'auth/clear',
    }),
    ...mapActions({
      initStore: 'auth/initStore',
    }),
    // handleClick(e) {
    //   e.stopPropagation()
    // },
    initChat() {
      // this.socket = webSocket(this.$socketIo, this.$conf.socketIoUrl)
      // console.log('initChat', this.socket)
      // this.socket = this.$socketIo(this.$conf.socketIoUrl, {
      //   // path: '/chat/',
      // })
      // this.socket.on('connect', () => {
      //   console.log('连接成功')
      // })
      // this.socket.on('disconnect', () => {
      //   console.log('服务端断开连接, 请登录后操作')
      // })
      // // const callback = () => console.log('消息收到')
      // this.socket.on('msg', (data, callback) => {
      //   console.log('收到消息：' + data)
      //   this.$refs.roomDialog.fetchRoomMessages()
      //   if (callback) {
      //     callback()
      //   }
      // })
      // this.socket.on('enter_room', () => {
      //   console.log('socket enter_room')
      //   this.$refs.roomDialog.fetchRoomMessages()
      // })
      // this.socket.on('leave_room', () => {
      //   console.log('socket leave_room')
      //   this.initStore(`${this.$conf.apiVersion}/auth/login`)
      // })
      // this.socket.on('error', (err) => {
      //   console.log(err.code)
      //   console.log(err.msg)
      // })
      // sessionStorage.setItem('socket', this.socket)
    },
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
