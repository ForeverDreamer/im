export default function ({ $axios, redirect }) {
  $axios.onError((error) => {
    switch (error.response.status) {
      case 401:
        redirect('/error/auth')
        break
      case 403:
        redirect('/error/permission')
        break
      case 404:
        redirect('/error/404')
        break
      case 500:
        redirect('/error/server')
        break
    }
  })
}
