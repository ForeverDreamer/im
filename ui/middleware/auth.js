export default function (context) {
  console.log('[Middleware] Auth', context)
  if (!context.store.getters['auth/isAuthenticated']) {
    context.redirect('/login')
  }
}
