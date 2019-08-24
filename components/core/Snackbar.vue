<template>
  <v-snackbar
    v-model="show"
    :timeout="5000"
    :top="true"
    :success="type === 'success'"
    :info="type === 'info'"
    :warning="type === 'warning'"
    :error="type === 'error'"
  >
    {{ message }}
    <v-btn flat @click.native="show = false">Close</v-btn>
  </v-snackbar>
</template>

<script>
export default {
  data () {
    return {
      show: false,
      type: '',
      message: ''
    }
  },
  created () {
    this.$store.watch(state => state.snackbar.snack, () => {
      const type = this.$store.state.snackbar.type
      const msg = this.$store.state.snackbar.snack
      if (msg !== '') {
        this.show = true
        this.type = type
        this.message = msg
        this.$store.commit('snackbar/setSnack', '', '')
      }
    })
  }
}
</script>
