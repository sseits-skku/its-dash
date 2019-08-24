export const state = () => ({
  username: '',
  refreshToken: '',
  accessToken: '',
  isStaff: false
})

export const mutations = {
  setLogin (state, auth) {
    state.username = auth.username
    state.refreshToken = auth.refresh
    state.accessToken = auth.access
    state.isStaff = auth.isStaff
    if (auth.isStaff) {
      auth.vuetify.theme.dark = true
    }
  },
  logout (state, vuetify) {
    state.username = ''
    state.refreshToken = ''
    state.accessToken = ''
    state.isStaff = false
    vuetify.theme.dark = false
  }
}
export const actions = {
  nuxtServerInit ({ commit }, { req }) {
  }
}
