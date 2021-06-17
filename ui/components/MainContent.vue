<template>
  <div>
    <room-dialog ref="roomDialog" :socket="socket" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Main',
  props: {
    socket: {
      type: Object,
      default: null,
    },
  },
  computed: {
    // mix the getters into computed with object spread operator
    ...mapGetters({
      currentRoomId: 'home/currentRoomId',
    }),
  },
}
</script>

<style scoped></style>
