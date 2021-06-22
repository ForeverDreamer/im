export default function (context) {
  console.log('[Middleware] route-guard', context)
  context.store.commit('menu/restoreNavMenu')
  const routePermitted = context.store.getters['menu/routePermitted'](
    context.route.fullPath
  )
  if (!routePermitted) {
    context.redirect('/error/404')
  }
}
