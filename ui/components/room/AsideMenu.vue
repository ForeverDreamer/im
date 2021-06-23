<template>
  <el-menu :default-active="activeRoomIdx | numToString" @select="enterRoom">
    <div v-for="(item, index) in rooms" :key="index" class="room-tab">
      <el-menu-item :index="index | numToString" class="room-tab__info">
        <img class="room-avatar" :src="item.avatar" />
        <span slot="title">{{ item.name }}（{{ item.description }}）</span>
      </el-menu-item>
      <el-dropdown class="room-tab__more" @command="handleCommand">
        <span class="el-dropdown-link">
          更多<i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="leave">离开</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </el-menu>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
  name: 'AsideMenu',
  props: {
    // socket: {
    //   type: Object,
    //   default: null,
    // },
    // rooms: {
    //   type: Array,
    //   default: () => [],
    // },
  },
  computed: {
    // mix the getters into computed with object spread operator
    ...mapGetters({
      rooms: 'auth/rooms',
      currentRoomId: 'auth/currentRoomId',
      activeRoomIdx: 'auth/activeRoomIdx',
    }),
  },
  methods: {
    ...mapMutations({
      updateCurrentRoomId: 'auth/updateCurrentRoomId',
    }),
    enterRoom(key, keyPath) {
      console.log(key, keyPath)
      this.$ws.emit('enter_room', {
        r_id: this.rooms[key].r_id,
      })
      this.updateCurrentRoomId(this.rooms[key].r_id)
    },
    leaveRoom(rId) {
      console.log(rId)
      this.$ws.emit('leave_room', {
        r_id: rId,
      })
    },
    handleCommand(cmd) {
      switch (cmd) {
        case 'leave':
          console.log(this.currentRoomId)
          this.leaveRoom(this.currentRoomId)
          break
      }
    },
  },
}
</script>

<style scoped>
.room-avatar {
  height: 46px;
  width: 46px;
  margin-right: 10px;
}

.room-tab {
  background: #2f343d;
  display: flex;
  justify-content: space-between;
  align-items: center;
  /*margin-bottom: 10px;*/
  cursor: pointer;
}

.room-tab:hover,
.room-tab:active,
.room-tab__info:hover,
.room-tab__info:active {
  background: #1f2329;
}

.room-tab__info {
  color: #81858b;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
