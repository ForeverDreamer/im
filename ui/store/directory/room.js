export const state = () => ({
  rooms: [],
})

export const getters = {
  rooms(state) {
    return state.rooms
  },
}

export const mutations = {
  init(state, data) {
    state.rooms = data.rooms
    console.log(state)
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
