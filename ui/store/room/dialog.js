export const state = () => ({
  msgToSend: '',
})

export const getters = {
  msgToSend(state) {
    return state.msgToSend
  },
}

export const mutations = {
  updateMsgToSend(state, msgToSend) {
    state.msgToSend = msgToSend
  },
}
