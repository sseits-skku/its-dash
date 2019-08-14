import axios from 'axios'

export const state = () => ({
  currentPage: 'main',
  authUser: null
})

export const mutations = {
  goPage (state, text) {
    state.currentPage = text
  },
  _login (state, user) {
    state.authUser = user
  },
  _logout (state) {
    state.authUser = null
    state.currentPage = 'main'
  }
}

export const actions = {
  async nuxtServerInit ({ commit }, { req }) {
    if (req.session && req.session.authUser) {
      await commit('_login', req.session.authUser)
    }
  },
  async login ({ commit }, { id, pw }) {
    const { data } = await axios.post('/api/login', { id, pw })
    if (!data.id) {
      alert('로그인 실패...')
      throw new Error('로그인 실패...')
    } else {
      commit('_login', data.id)
    }
  }
}
