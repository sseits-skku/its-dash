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
  async checkLogin (context, vuetify) {
    try {
      const cAuth = Cookie.get('Authorization')
      if (typeof cAuth === 'undefined') {
        throw new TypeError('failed.')
      }
      const auth = JSON.parse(cAuth)
      const resAccess = await this.$axios.$post('/auth/verify', {
        token: auth.access
      })
      const resRefresh = await this.$axios.$post('/auth/verify', {
        token: auth.refresh
      })
      if (Object.entries(resRefresh).length === 0 &&
          resRefresh.constructor === Object) {
      // refresh token is valid.
        if (Object.entries(resAccess).length !== 0 &&
            resAccess.constructor === Object) {
        // access token is NOT valid.
          const { access, refresh } = await this.$axios.$post(
            '/auth/refresh',
            { refresh: auth.refresh }
          )
          auth.refresh = refresh
          auth.access = access
        }
        auth.vuetify = vuetify
        context.commit('setLogin', auth)
      } else {
        throw new TypeError('failed. ff')
      }
    } catch (err) {
      // invalid cookie and logout.
      console.error(err)
      context.commit('logout', vuetify)
    }
  }
}
