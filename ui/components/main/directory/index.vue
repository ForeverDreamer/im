<template>
  <div class="directory">
    目录
    <el-tabs v-model="currentTabComponent" @tab-click="handleClick">
      <el-tab-pane label="房间" name="DirectoryRoom"></el-tab-pane>
      <el-tab-pane label="用户" name="DirectoryUser"></el-tab-pane>
    </el-tabs>
    <component :is="currentTabComponent"></component>
  </div>
</template>

<script>
import DirectoryRoom from '~/components/main/directory/room'
import DirectoryUser from '~/components/main/directory/user'

export default {
  name: 'Directory',
  components: {
    DirectoryRoom,
    DirectoryUser,
  },
  data() {
    return {
      currentTabComponent: 'DirectoryRoom',
    }
  },
  methods: {
    handleClick(tab, event) {
      this.currentTabComponent = tab.name
    },
  },
}
</script>

<style scoped>
.directory {
  padding: 20px;
}
</style>
