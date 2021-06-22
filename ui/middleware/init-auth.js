export default function (context) {
  console.log('[Middleware] initAuth', context)
  // context.store.dispatch('auth/initAuth', context.$config.apiVersion)
}
