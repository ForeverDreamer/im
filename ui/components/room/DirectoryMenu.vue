<template>
  <el-menu @select="enterRoom">
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
import { mapMutations } from 'vuex'

export default {
  name: 'DirectoryMenu',
  methods: {
    ...mapMutations({
      updateCurrentRoomId: 'home/updateCurrentRoomId',
    }),
    enterRoom(key, keyPath) {
      console.log(key, keyPath)
      this.socket.emit('enter_room', {
        r_id: this.rooms[key].r_id,
      })
      this.updateCurrentRoomId(this.rooms[key].r_id)
    },
  },
}
</script>

<style scoped></style>
