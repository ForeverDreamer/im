<template>
  <h1>服务器资源不存在，请稍后再试</h1>
</template>

<script>
export default {
  name: '404',
  layout: 'login',
  created() {
    setTimeout(() => {
      this.$router.push('/home/')
    }, 3000)
  },
}
</script>

<style scoped></style>
