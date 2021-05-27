<template>
  <h1>服务器繁忙，请稍后再试</h1>
</template>

<script>
export default {
  name: 'Server',
  layout: 'login',
  created() {
    setTimeout(() => {
      this.$router.push('/login/')
    }, 3000)
  },
}
</script>

<style scoped></style>
