export const state = () => ({
  authenticated: false,
  socket: null,
  user: null,
  rooms: [],
  currentRoomId: '',
})

export const getters = {
  isAuthenticated(state) {
    return state.authenticated
  },
  socket(state) {
    return state.socket
  },
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
    // state = data
    state.authenticated = true
    state.socket = data.socket
    state.user = data.user
    state.rooms = data.rooms
    state.currentRoomId = data.user.currentRoomId
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
  cacheState(state) {
    sessionStorage.setItem('authState', state)
  },
  clear(state) {
    state.authenticated = false
    state.socket = null
    state.user = null
    state.rooms = []
    state.currentRoomId = ''
    sessionStorage.removeItem('authState')
  },
}

export const actions = {
  login({ getters, commit }, authData) {
    if (getters.isAuthenticated) {
      console.log('getters.isAuthenticated')
      return
    }
    return this.$axios
      .$post('/account/passwordlogin/', {
        username: authData.username,
        password: authData.password,
      })
      .then((response) => {
        console.log(response)
        const token = response.data.token
        commit('cacheState', token)
      })
      .catch((e) => console.log('login => ' + e))
  },
  initAuth(vuexContext, apiVersion) {
    let data = localStorage.getItem('authState')
    if (!data) {
      this.$axios
        .$get(`${apiVersion}/auth/login`)
        .then((response) => {
          data = response.data
        })
        .catch((error) => {
          console.log(error.response.data)
        })
    }
    vuexContext.commit('init', data)
  },
  logout(vuexContext) {
    vuexContext.commit('clear')
  },
}
