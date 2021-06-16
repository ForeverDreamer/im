<template>
  <div></div>
</template>

<script>
export default {
  name: 'Auth',
  layout: 'login',
  created() {
    this.$message.error('请登录后操作')
    setTimeout(() => {
      this.$router.push('/login')
    }, 3000)
  },
}
</script>

<style scoped></style>
