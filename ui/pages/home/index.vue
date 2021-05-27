<template>
  <div>
    <h1>home主页</h1>
  </div>
</template>

<script>
export default {
  name: 'Index',
  beforeCreate() {
    this.$router.push('/home/')
  },
}
</script>

<style scoped></style>
