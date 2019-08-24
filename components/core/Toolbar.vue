<template>
  <v-app-bar
    v-if="dPerm !== true"
    app
    dense
  >
    <v-app-bar-nav-icon
      @click="dOpen = true"
    />
    <v-spacer />
  </v-app-bar>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  computed: {
    dOpen: {
      get () { return this.$store.state.drawerOpen },
      set (value) { this.$store.commit('setDrawerOpen', value) }
    },
    dPerm: {
      get () { return this.$store.state.drawerPerm },
      set (value) { this.$store.commit('setDrawerPerm', value) }
    }
  }
}
</script>
