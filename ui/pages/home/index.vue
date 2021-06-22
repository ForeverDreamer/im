<template>
  <div>主页</div>
</template>

<script>
export default {
  name: 'Index',
  beforeCreate() {
    this.$router.push('/room')
  },
}
</script>
