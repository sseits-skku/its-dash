export const state = () => ({
  loginDialogOpen: false,
  drawerPerm: true,
  drawerOpen: true
})

export const mutations = {
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
