export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: '中经网即时通信软件',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['element-ui/lib/theme-chalk/index.css'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: ['~/plugins/element-ui', '~/plugins/init', '~/plugins/network'],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    'bootstrap-vue/nuxt',
    // 请求代理配置，解决跨域
    '@gauseen/nuxt-proxy',
  ],

  proxyTable: {
    '/backend': {
      // 请求服务器地址
      // target: 'http://localhost:5000/dm',
      // target: 'http://localhost:5001/ds',
      // target: 'http://192.168.71.20:7090/dm',
      // target: 'http://192.168.71.20:7090/ds',
      target: 'http://127.0.0.1:5000',
      // target: 'http://zlbxxcj.bjceis.com',
      // target: 'https://api.weixin.qq.com',
      ws: true,
      changeOrigin: true,
      pathRewrite: {
        '^/backend': '',
      },
    },
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // baseURL: process.env.BASE_URL || 'http://zlbxxcj.bjceis.com',
    // baseURL: process.env.BASE_URL || 'http://192.168.71.20:5000',
    baseURL: process.env.BASE_URL || 'http://127.0.0.1:5000',
    // baseURL: process.env.BASE_URL || '/backend',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: [/^element-ui/],
    publicPath: '/static/client/',
  },
  publicRuntimeConfig: {
    apiVersion: '/v1',
    socketIoUrl: 'http://127.0.0.1:5000/events',
  },
}
