<template>
  <el-container>
    <el-aside width="400px">
      <el-menu :default-active="currentRoom" @select="openRoom">
        <el-menu-item
          v-for="(item, index) in rooms"
          :key="index"
          :index="index | numToString"
        >
          <!--          <i :class="item.icon"></i>-->
          <span slot="title">{{ item.name }}</span>
        </el-menu-item>
        <!--<li v-for="i in 100" :key="i">{{ i }}</li>-->
      </el-menu>
    </el-aside>
    <el-main>Main</el-main>
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
      currentRoom: 'home/currentRoom',
    }),
  },
  created() {
    this.initStore(`${this.$conf.apiVersion}/auth/login`)
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
    openRoom(rId) {
      console.log(rId)
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
  line-height: 200px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

.el-container {
  position: absolute;
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
</style>
