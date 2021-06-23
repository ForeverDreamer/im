<template>
  <div>
    <img class="avatar" :src="user.avatar" />
    <span>{{ user.username }}</span>
  </div>
</template>

<script>
export default {
  name: 'Header',
  props: {
    user: {
      type: Object,
      default: () => {},
    },
  },
}
</script>

<style scoped>
.avatar {
  height: 24px;
  width: 24px;
  margin-right: 10px;
}
</style>
