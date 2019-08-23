export const state = () => ({
  username: '',
  refreshToken: '',
  accessToken: ''
})

export const mutations = {
  setLogin (state, auth) {
    state.username = auth.username
    state.refreshToken = auth.refresh
    state.accessToken = auth.access
  },
  logout (state) {
    state.username = ''
    state.refreshToken = ''
    state.accessToken = ''
  }
}
export const actions = {
  nuxtServerInit ({ commit }, { req }) {
  }
}
