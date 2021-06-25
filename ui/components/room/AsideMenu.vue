<template>
  <!--  <el-menu :default-active="activeRoomIdx | numToString" @select="enterRoom">-->
  <!--    <div v-for="(item, index) in rooms" :key="index" class="room-tab">-->
  <!--      <el-menu-item :index="index | numToString" class="room-tab__info">-->
  <!--        <img class="room-avatar" :src="item.avatar" />-->
  <!--        <span slot="title">{{ item.name }}（{{ item.description }}）</span>-->
  <!--      </el-menu-item>-->
  <!--      <el-dropdown class="room-tab__more" @command="handleCommand">-->
  <!--        <span class="el-dropdown-link">-->
  <!--          更多<i class="el-icon-arrow-down el-icon&#45;&#45;right"></i>-->
  <!--        </span>-->
  <!--        <el-dropdown-menu slot="dropdown">-->
  <!--          <el-dropdown-item command="leave">离开</el-dropdown-item>-->
  <!--        </el-dropdown-menu>-->
  <!--      </el-dropdown>-->
  <!--    </div>-->
  <!--  </el-menu>-->
  <div class="list-group">
    <div
      v-for="(item, index) in rooms"
      :key="index"
      class="list-group-item list-group-item-action room-tab"
      :class="{ active: index === activeRoomIdx }"
      @click="enterRoom(index)"
    >
      <div class="room-tab__info">
        <img class="room-avatar" :src="item.avatar" />
        <span slot="title">{{ item.name }}（{{ item.description }}）</span>
        <span class="badge badge-secondary badge-pill">14</span>
      </div>
    </div>
  </div>
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
    enterRoom(index) {
      console.log(index)
      this.$ws.emit('enter_room', {
        r_id: this.rooms[index].r_id,
      })
      this.updateCurrentRoomId(this.rooms[index].r_id)
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
  height: 1.75rem;
  width: 1.75rem;
  margin-right: 10px;
}

.room-tab {
  background: #2f343d;
  display: flex;
  justify-content: space-between;
  align-items: center;
  /*margin-bottom: 10px;*/
  cursor: pointer;
  font-size: 0.875rem;
  line-height: 1.25rem;
  border-radius: 0.125rem;
  padding: 0.25rem 1rem;
}

.room-tab__info {
  color: #81858b;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.room-tab:hover,
.room-tab:active,
.room-tab__info:hover,
.room-tab__info:active {
  background: #1f2329;
}
</style>
