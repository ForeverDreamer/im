<template>
  <div></div>
</template>

<script>
export default {
  name: '404',
  layout: 'login',
  created() {
    this.$message.error('服务器资源不存在，请稍后再试')
    setTimeout(() => {
      this.$router.push('/home')
    }, 3000)
  },
}
</script>

<style scoped></style>
