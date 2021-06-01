<template>
  <el-container>
    <el-aside width="300px">
      <el-menu :default-active="activeRoomIdx | numToString" @select="openRoom">
        <el-menu-item
          v-for="(item, index) in rooms"
          :key="index"
          :index="index | numToString"
          class="d-flex justify-content-between room-tab"
        >
          <el-image class="room-avatar" :src="item.avatar"></el-image>
          <span slot="title">{{ item.name }}（{{ item.description }}）</span>
        </el-menu-item>
        <!--<li v-for="i in 100" :key="i">{{ i }}</li>-->
      </el-menu>
    </el-aside>
    <el-main>
      <div class="room-window">
        <div class="room-window_msgs">消息列表</div>
        <div class="room-window_input">
          <el-input
            v-model="msgToSend"
            placeholder="要发送的消息"
            size="medium"
            class="w-50"
          />
          <el-button type="primary" @click="sendMsg(msgToSend)">
            发送消息
          </el-button>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  name: 'Index',
  computed: {
    // mix the getters into computed with object spread operator
    ...mapGetters({
      user: 'home/user',
      rooms: 'home/rooms',
      currentRoomId: 'home/currentRoomId',
      currentRoom: 'home/currentRoom',
      activeRoomIdx: 'home/activeRoomIdx',
    }),
    msgToSend() {
      return this.currentRoom ? this.currentRoom.msgToSend : ''
    },
  },
  created() {
    this.initStore(`${this.$conf.apiVersion}/auth/login`)
    this.initChat()
  },
  methods: {
    ...mapMutations({
      updateUser: 'home/updateUser',
      updateRoom: 'home/updateRoom',
      updateCurrentRoomId: 'home/updateCurrentRoomId',
      clearStore: 'home/clear',
    }),
    ...mapActions({
      initStore: 'home/initStore',
    }),
    initChat() {
      this.socket = this.$socketIo('http://127.0.0.1:5000/events', {
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
        console.log(data)
        // this.rooms[data.r_id].msgs.push(data)
        // console.log(this.rooms)
        if (callback) {
          callback()
        }
      })
      this.socket.on('error', (err) => {
        console.log(err.code)
        console.log(err.msg)
      })
    },
    sendMsg(msg) {
      console.log(msg)
      if (!this.msgToSend) {
        return
      }
      this.socket.emit('msg', {
        r_id: this.rId,
        msg: this.msgToSend,
      })
    },
    enterRoom(rId) {
      console.log(rId)
      this.socket.emit('enter_room', {
        r_id: rId,
      })
      console.log(`${this.user.nickname}进入房间：${rId}`)
    },
    leaveRoom(rId) {
      console.log(rId)
      this.socket.emit('leave_room', {
        r_id: rId,
      })
      console.log(`${this.user.nickname}离开房间：${rId}`)
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
  background-color: #d3dce6;
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
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

.room-avatar {
  height: 56px;
  width: 56px;
}

.room-tab {
  /*background: #00b7ff;*/
  margin-bottom: 10px;
}

.room-window {
  position: absolute;
  border: 1px solid black;
  height: 100%;
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
  justify-content: space-between;
  align-items: center;
}

.room-window_msgs {
  border: 1px solid black;
  width: 100%;
  height: calc(100% - 60px);
}

.room-window_input {
  border: 1px solid black;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 90%;
  margin-bottom: 10px;
  padding: 10px;
}
</style>
