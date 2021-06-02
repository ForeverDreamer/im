<template>
  <h1>没有操作权限</h1>
</template>

<script>
export default {
  name: 'Permission',
  layout: 'login',
  created() {
    setTimeout(() => {
      this.$router.push('/home/')
    }, 3000)
  },
}
</script>

<style scoped></style>
