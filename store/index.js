export const state = () => ({
  ip: '0.0.0.0',
  loginDialogOpen: false,
  drawerPerm: true,
  drawerOpen: true
})

export const mutations = {
  SET_IP (state, value) {
    state.ip = value
  },
  setLoginDialogOpen (state, value) {
    state.loginDialogOpen = value
  },
  setDrawerPerm (state, value) {
    state.drawerPerm = value
  },
  setDrawerOpen (state, value) {
    state.drawerOpen = value
  }
}

export const actions = {
  async nuxtServerInit ({ commit }, { $axios }) {
  }
}
