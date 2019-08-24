import Cookie from 'js-cookie'

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
    Cookie.set('Authorization', {
      username: auth.username,
      isStaff: auth.isStaff,
      refresh: auth.refresh,
      access: auth.access
    })
  },
  logout (state, vuetify) {
    state.username = ''
    state.refreshToken = ''
    state.accessToken = ''
    state.isStaff = false
    vuetify.theme.dark = false
    Cookie.remove('Authorization')
  }
}
export const actions = {
  nuxtServerInit ({ commit }, { req }) {
  }
}
