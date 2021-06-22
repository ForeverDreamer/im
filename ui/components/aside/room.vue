<template>
  <div>
    <div v-if="user" class="navigation">
      <user-header :avatar="user.avatar"></user-header>
      <div>
        <i class="el-icon-s-home icon" @click="home"></i>
        <i class="el-icon-search icon" @click="spotlight"></i>
        <i class="el-icon-folder icon" @click="directory"></i>
      </div>
    </div>
    <room-aside-menu :socket="socket" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Aside',
  props: {
    socket: {
      type: Object,
      default: null,
    },
  },
  computed: {
    ...mapGetters({
      user: 'home/user',
    }),
  },
  methods: {
    home() {
      console.log('进入首页')
    },
    spotlight() {
      console.log('进入搜索')
    },
    directory() {
      console.log('进入目录')
      this.$axios
        .$get(`${this.$conf.apiVersion}/room/`)
        .then((response) => {
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error.response.data)
        })
    },
  },
}
</script>

<style scoped>
.navigation {
  border: 1px solid black;
  height: 50px;
  padding: 0 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
