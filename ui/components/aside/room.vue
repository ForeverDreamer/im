<template>
  <div>
    <div v-if="user" class="navigation">
      <user-header :user="user"></user-header>
      <div>
        <i class="el-icon-s-home icon" @click="home"></i>
        <i class="el-icon-search icon" @click="spotlight"></i>
        <i class="el-icon-folder icon" @click="directory"></i>
        <!--        <i class="el-icon-s-home icon" @click="createRoom"></i>-->
      </div>
    </div>
    <room-aside-menu />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import RoomAsideMenu from '~/components/room/AsideMenu'

export default {
  name: 'Aside',
  components: {
    RoomAsideMenu,
  },
  computed: {
    ...mapGetters({
      user: 'auth/user',
    }),
  },
  methods: {
    home() {
      console.log('进入首页')
      this.$router.push('/home')
    },
    spotlight() {
      console.log('进入搜索')
    },
    directory() {
      console.log('进入目录')
      this.$router.push('/directory')
      // this.$axios
      //   .$get(`${this.$conf.apiVersion}/room/`)
      //   .then((response) => {
      //     console.log(response.data)
      //   })
      //   .catch((error) => {
      //     console.log(error.response.data)
      //   })
    },
    createRoom() {
      this.$axios
        .$post(`${this.$config.apiVersion}/room/`, {
          name: 'GENERAL',
          r_type: 'c',
          description: '默认房间',
        })
        .then((response) => {
          console.log(response.data.msg)
          console.log(response.data.room)
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
