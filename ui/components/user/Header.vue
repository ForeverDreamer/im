<template>
  <div>
    <img class="avatar" :src="avatar" />
  </div>
</template>

<script>
export default {
  name: 'Header',
  props: {
    avatar: {
      type: String,
      default: '',
    },
  },
}
</script>

<style scoped>
.avatar {
  height: 30px;
  width: 30px;
  margin-right: 10px;
}
</style>
