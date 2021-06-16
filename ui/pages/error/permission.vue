<template>
  <div></div>
</template>

<script>
export default {
  name: 'Permission',
  layout: 'login',
  created() {
    this.$message.error('没有操作权限')
    setTimeout(() => {
      this.$router.push('/home')
    }, 3000)
  },
}
</script>

<style scoped></style>
