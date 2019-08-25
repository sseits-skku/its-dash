<template>
  <v-snackbar
    v-model="show"
    :timeout="5000"
    :top="true"
    :success="$store.state.snackbar.type === 'success'"
    :info="$store.state.snackbar.type === 'info'"
    :warning="$store.state.snackbar.type === 'warning'"
    :error="$store.state.snackbar.type === 'error'"
  >
    {{ $store.state.snackbar.snack }}
    <v-btn @click.native="show = false">Close</v-btn>
  </v-snackbar>
</template>

<script>
export default {
  data () {
    return {
      show: false
    }
  },
  created () {
    this.$store.watch(state => state.snackbar.snack, () => {
      const msg = this.$store.state.snackbar.snack
      if (msg !== '') {
        this.show = true
        this.$store.commit('snackbar/setSnack', '', '')
      }
    })
  }
}
</script>
