<template>
  <div>
    <el-input
      v-model="keyword"
      placeholder="搜索房间"
      suffix-icon="el-icon-search"
    >
    </el-input>
    <el-table :data="roomData" style="width: 100%" @row-click="enterRoom">
      <el-table-column prop="name" label="房间名" width="180">
      </el-table-column>
      <el-table-column prop="user_count" label="成员数" width="180">
      </el-table-column>
      <el-table-column prop="created_at" label="创建于"> </el-table-column>
      <el-table-column prop="last_msg" label="最后消息"> </el-table-column>
      <el-table-column prop="owner" label="群主"> </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'Room',
  data() {
    return {
      keyword: '',
      roomData: [],
    }
  },
  created() {
    this.init()
  },
  methods: {
    init() {
      this.$axios
        .$get(`${this.$conf.apiVersion}/room/`)
        .then((response) => {
          console.log(response.data)
          this.roomData = response.data.rooms
        })
        .catch((error) => {
          console.log(error.response.data)
        })
    },
    enterRoom(row, column, event) {
      console.log(row, column, event)
    },
  },
}
</script>

<style scoped></style>
