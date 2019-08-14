export default function ({ store, redirect }) {
  if (!store.state.auth.auth) {
    store.commit('snackbar/setSnack', '로그인이 필요합니다.', 'error')
    return redirect('/')
  }
}
