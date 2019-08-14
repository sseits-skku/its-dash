export const state = () => ({
  snack: '',
  type: ''
})

export const mutations = {
  setSnack (state, snack, type) {
    state.type = type
    state.snack = snack
  }
}
