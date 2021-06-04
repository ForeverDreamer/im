<template>
  <div class="dialog">
    <div class="dialog-msgs">
      <message
        v-for="(msg, index) in msgs"
        :key="index"
        :msg="msg"
        class="d-flex justify-content-between align-items-center"
      />
    </div>
    <div class="dialog-input">
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
</template>

<script>
import Message from '~/components/room/Message'
export default {
  name: 'Dialog',
  components: {
    Message,
  },
  props: {
    socket: {
      type: Object,
      default: null,
    },
    rId: {
      type: String,
      default: '',
    },
    // msgToSend: {
    //   type: String,
    //   default: '',
    // },
  },
  // created() {
  //   this.socket.on('enter_room', () => {
  //     console.log('socket enter_room')
  //     this.fetchRoomMessages()
  //   })
  // },
  data() {
    return {
      msgToSend: '',
      msgs: [],
    }
  },
  computed: {
    formatedMsgs() {
      if (!this.msgs) {
        return ''
      }
      return this.msgs
        .map((msg) => msg.user.username + '说' + msg.msg)
        .join(',')
    },
  },
  watch: {
    rId(newValue, oldValue) {
      this.msgToSend = ''
      this.msgs = []
      this.fetchRoomMessages()
    },
  },
  methods: {
    sendMsg(msg) {
      if (!this.msgToSend) {
        return
      }
      console.log('发送用户消息：' + msg)
      this.socket.emit('msg', {
        r_id: this.rId,
        msg: this.msgToSend,
      })
      if (this.msgToSend.startsWith('@bot ')) {
        console.log('发送bot消息：' + msg)
        this.socket.emit('msg_bot', {
          r_id: this.rId,
          msg: this.msgToSend,
        })
      }
      this.msgToSend = ''
      this.fetchRoomMessages()
    },
    fetchRoomMessages() {
      this.$axios
        .$post(`${this.$conf.apiVersion}/cmd/`, {
          cmd: 'query_message',
          params: { r_id: this.rId },
        })
        .then((response) => {
          console.log(response.data)
          this.msgs = response.data
        })
        .catch((error) => {
          console.log(error.response.data)
        })
    },
  },
}
</script>

<style scoped>
.dialog {
  position: absolute;
  border: 1px solid black;
  height: 100%;
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
  justify-content: space-between;
  align-items: center;
}

.dialog-msgs {
  border: 1px solid black;
  width: 100%;
  height: calc(100% - 60px);
}

.dialog-input {
  border: 1px solid #9a9999;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 90%;
  margin-bottom: 10px;
  padding: 10px;
}
</style>
