<template>
  <v-app>
    <Snackbar />
    <Toolbar />
    <Drawer />
    <nuxt />
    <Footer />
  </v-app>
</template>

<script>
import Snackbar from '@/components/Snackbar'
import Toolbar from '@/components/Toolbar'
import Drawer from '@/components/Drawer'
import Footer from '@/components/Footer'

export default {
  components: {
    Snackbar,
    Toolbar,
    Drawer,
    Footer
  },
  data () {
    return {}
  },
  created () {
    this.$store.watch(state => state.auth.auth, () => {
      if (this.$store.state.auth.auth !== null) {
        this.$vuetify.theme.isDark = true
      } else {
        this.$vuetify.theme.isDark = false
      }
    })
  },
  head () {
    return this.$store.state.auth.auth === null
      ? { title: 'SSE-ITS Website' }
      : { title: 'ITS Member zone' }
  }
}
</script>
