<template>
  <el-container>
    <el-aside width="400px">
      <el-menu
        :default-active="activeRoomIdx | numToString"
        @select="enterRoom"
      >
        <div
          v-for="(item, index) in rooms"
          :key="index"
          class="d-flex justify-content-between align-items-center"
        >
          <el-menu-item
            :index="index | numToString"
            class="d-flex justify-content-between room-tab"
          >
            <div>
              <el-image class="room-avatar" :src="item.avatar"></el-image>
              <span slot="title"
                >{{ item.name }}（{{ item.description }}）</span
              >
            </div>
          </el-menu-item>
          <el-dropdown @command="handleCommand">
            <span class="el-dropdown-link">
              更多<i class="el-icon-arrow-down el-icon--right"></i>
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="leave">离开</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-menu>
    </el-aside>
    <el-main>
      <room-dialog
        ref="roomDialog"
        :socket="socket"
        :r-id="currentRoomId"
      ></room-dialog>
    </el-main>
  </el-container>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'
import RoomDialog from '~/components/room/Dialog'

export default {
  name: 'Index',
  components: {
    RoomDialog,
  },
  data() {
    return {
      socket: null,
    }
  },
  computed: {
    // mix the getters into computed with object spread operator
    ...mapGetters({
      user: 'home/user',
      rooms: 'home/rooms',
      currentRoomId: 'home/currentRoomId',
      currentRoom: 'home/currentRoom',
      activeRoomIdx: 'home/activeRoomIdx',
    }),
    // msgToSend() {
    //   return this.currentRoom ? this.currentRoom.msgToSend : ''
    // },
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
      updateCurrentRoomId: 'home/updateCurrentRoomId',
      clearStore: 'home/clear',
    }),
    ...mapActions({
      initStore: 'home/initStore',
    }),
    handleCommand(cmd) {
      switch (cmd) {
        case 'leave':
          this.leaveRoom(this.currentRoomId)
          break
      }
    },
    handleClick(e) {
      e.stopPropagation()
    },
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
        console.log('收到消息：' + data)
        // this.rooms[data.r_id].msgs.push(data)
        // console.log(this.rooms)
        if (callback) {
          callback()
        }
      })
      this.socket.on('enter_room', () => {
        console.log('socket enter_room')
        this.$refs.roomDialog.fetchRoomMessages()
      })
      this.socket.on('error', (err) => {
        console.log(err.code)
        console.log(err.msg)
      })
    },
    enterRoom(key, keyPath) {
      console.log(key, keyPath)
      this.socket.emit('enter_room', {
        r_id: this.rooms[key].r_id,
      })
      this.updateCurrentRoomId(this.rooms[key].r_id)
      console.log(`${this.user.nickname}进入房间：${this.rooms[key].name}`)
    },
    leaveRoom(rId) {
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
  /*margin-bottom: 10px;*/
}

.el-dropdown-link {
  cursor: pointer;
  color: #409eff;
}
.el-icon-arrow-down {
  font-size: 12px;
}
</style>
