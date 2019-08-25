<template>
  <v-app :dark="isauth">
    <Login />
    <Toolbar />
    <Drawer />
    <v-content>
      <v-container fluid fill-height>
        <nuxt />
      </v-container>
    </v-content>
    <Footer />
    <Snackbar />
  </v-app>
</template>

<script>
import Snackbar from '@/components/core/Snackbar'
import Toolbar from '@/components/core/Toolbar'
import Drawer from '@/components/core/Drawer'
import Footer from '@/components/core/Footer'
import Login from '@/components/core/Login'
// TODO: Pagination 어떻게 처리할지 고민해보기.
export default {
  components: {
    Snackbar,
    Drawer,
    Footer,
    Login,
    Toolbar
  },
  data () {
    return {
      drawer: false,
      dialog: false,
      isauth: false
    }
  },
  beforeDestroy () {
    if (typeof window !== 'undefined') {
      window.removeEventListener('resize', this.onResize, { passive: true })
    }
  },
  mounted () {
    this.$store.dispatch('auth/checkLogin', this.$vuetify)
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
  },
  methods: {
    onResize () {
      if (this.$vuetify.breakpoint.name === 'xs') {
        this.$store.commit('setDrawerPerm', false)
      } else if (this.$vuetify.breakpoint.name === 'sm') {
        this.$store.commit('setDrawerPerm', false)
      } else {
        this.$store.commit('setDrawerPerm', true)
        this.$store.commit('setDrawerOpen', true)
      }
    }
  },
  head () {
    return this.$store.state.auth.auth === null
      ? { title: 'SSE-ITS Website' }
      : { title: 'ITS Member zone' }
  }
}
</script>
