import Vue from 'vue'

import '~/lib/filter'
import { io } from 'socket.io-client'
import conf from '~/lib/config'
import { registerEvents } from '~/lib/websocket'

const ws = io(conf.socketIoUrl, {
  // path: '/chat/',
})
registerEvents(ws)
Vue.prototype.$ws = ws
Vue.prototype.$conf = conf
