export const state = () => ({
  authenticated: false,
  // socket: null,
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
    // state.socket = data.socket
    console.log('data', data)
    sessionStorage.setItem('authState', JSON.stringify(data))
    state.user = data.user
    state.rooms = data.rooms
    state.currentRoomId = data.user.current_r_id
    state.authenticated = true
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
  // cacheState(state) {
  //   sessionStorage.setItem('authState', state)
  // },
  clear(state) {
    state.authenticated = false
    // state.socket = null
    state.user = null
    state.rooms = []
    state.currentRoomId = ''
    sessionStorage.removeItem('authState')
  },
}

export const actions = {
  login({ getters }, authData) {
    if (getters.isAuthenticated) {
      console.log('auth.actions.login： isAuthenticated is true')
      return
    }
    return this.$axios
      .$post(authData.url, {
        login_type: 'account',
        arguments: {
          username: authData.username,
          password: authData.password,
        },
      })
      .then((response) => {
        // sessionStorage.setItem('authState', JSON.stringify(response.data))
        console.log('auth.actions.login', response.data)
      })
      .catch((e) => console.log('login => ' + e))
  },
  initAuth({ commit }, apiVersion) {
    // console.log(vuexContext)
    const data = sessionStorage.getItem('authState')
    if (data) {
      // commit('clear')
      commit('init', JSON.parse(data))
      return
    }
    this.$axios
      .$get(`${apiVersion}/auth/login`)
      .then((response) => {
        commit('init', response.data)
      })
      .catch((error) => {
        console.log(error.response.data)
      })
  },
  logout({ commit }) {
    commit('clear')
  },
}
