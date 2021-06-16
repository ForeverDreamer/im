<template>
  <div></div>
</template>

<script>
export default {
  name: 'Server',
  layout: 'login',
  created() {
    this.$message.error('服务器繁忙，请稍后再试')
    setTimeout(() => {
      this.$router.push('/home')
    }, 3000)
  },
}
</script>

<style scoped></style>
