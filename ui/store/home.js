export const state = () => ({
  user: null,
  rooms: [],
  currentRoomId: '',
})

export const getters = {
  user(state) {
    return state.user
  },
  rooms(state) {
    return state.rooms
  },
  currentRoomId(state) {
    return state.currentRoomId
  },
  currentRoom(state) {
    return state.rooms.find((room) => room.r_id === state.currentRoomId)
  },
  activeRoomIdx(state) {
    return state.rooms.findIndex((room) => room.r_id === state.currentRoomId)
  },
}

export const mutations = {
  init(state, data) {
    state.user = data.user
    state.rooms = data.rooms
    // state.rooms.forEach((room) => {
    //   room.msgToSend = ''
    // })
    state.currentRoomId = data.user.current_r_id
      ? data.user.current_r_id
      : data.rooms[0].r_id
    console.log(state)
  },
  updateUser(state, user) {
    Object.assign(state.user, user)
  },
  updateRoom(state, room) {
    Object.assign(state.rooms[room.r_id], room)
  },
  updateCurrentRoomId(state, currentRoomId) {
    state.currentRoomId = currentRoomId
  },
  clear(state) {
    state.user = null
    state.rooms = []
    state.currentRoomId = ''
  },
}

export const actions = {
  initStore(vuexContext, url) {
    return this.$axios
      .$get(url)
      .then((response) => {
        vuexContext.commit('init', response.data)
      })
      .catch((error) => {
        console.log(error.response.data)
      })
  },
}
