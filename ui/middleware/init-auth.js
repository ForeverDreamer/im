export default function (context) {
  console.log('[Middleware] initAuth', context)
  context.store
    .dispatch('auth/initAuth', context.$config.apiVersion)
    .catch((e) => {
      console.log(e)
      context.redirect('/login')
    })
  // if (!context.store.getters['auth/isAuthenticated']) {
  //   context.redirect('/login')
  // }
}
