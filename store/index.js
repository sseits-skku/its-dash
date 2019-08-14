export const state = () => ({
  dialog: false,
  currentPage: 'main'
})

export const mutations = {
  goPage (state, text) {
    state.currentPage = text
  },
  dialog (state, tf) {
    state.dialog = tf
  }
}
