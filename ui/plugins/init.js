import Vue from 'vue'

import '~/lib/filter'
import { io } from 'socket.io-client'
import conf from '~/lib/config'

Vue.prototype.$socketIo = io
Vue.prototype.$conf = conf
