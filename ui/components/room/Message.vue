<template>
  <div
    class="message-base"
    :class="
      msg.user.username === user.username ? 'message-me' : 'message-others'
    "
  >
    <img class="avatar" src="http://127.0.0.1:5000/static/asset/room/1.jpg" />
    <div class="info">
      <div>
        <b>{{ msg.user.username }}</b>
        <span>{{ msg.created_at }}</span>
      </div>
      <div>{{ msg.msg }}</div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Message',
  props: {
    msg: {
      type: Object,
      default: null,
    },
  },
  computed: {
    ...mapGetters({
      user: 'home/user',
    }),
  },
}
</script>

<style scoped>
.avatar {
  height: 30px;
  width: 30px;
  margin-right: 10px;
}
.message-base {
  /*border: 1px solid #9a9999;*/
  /*background: #409eff;*/
  display: flex;
  align-items: center;
  padding: 10px;
  /*margin-bottom: 10px;*/
}
.message-others {
  justify-content: flex-start !important;
}
.message-me {
  justify-content: flex-end !important;
}
.info {
  display: flex;
  flex-flow: column nowrap;
  justify-content: space-between;
  align-items: start;
}
</style>
