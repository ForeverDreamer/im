<template>
  <div>
    <el-input
      v-model="keyword"
      placeholder="搜索用户"
      suffix-icon="el-icon-search"
    >
    </el-input>
    <el-table :data="roomData" style="width: 100%">
      <el-table-column prop="name" label="姓名" width="180"> </el-table-column>
      <el-table-column prop="address" label="地址"> </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'User',
  data() {
    return {
      keyword: '',
      roomData: [
        {
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
        },
        {
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄',
        },
        {
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄',
        },
        {
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄',
        },
      ],
    }
  },
}
</script>

<style scoped></style>
