export const state = () => ({
  username: '',
  refreshToken: '',
  accessToken: ''
})

export const mutations = {
  setLogin (state, auth) {
    console.log(auth)
    state.username = auth.username
    state.refreshToken = auth.refresh
    state.accessToken = auth.access
    auth.vuetify.theme.dark = true
  },
  logout (state, vuetify) {
    state.username = ''
    state.refreshToken = ''
    state.accessToken = ''
    vuetify.theme.dark = false
  }
}
export const actions = {
  nuxtServerInit ({ commit }, { req }) {
  }
}
