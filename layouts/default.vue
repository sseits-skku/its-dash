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
import Cookie from 'js-cookie'
import Snackbar from '@/components/Snackbar'
import Toolbar from '@/components/Toolbar'
import Drawer from '@/components/Drawer'
import Footer from '@/components/Footer'
import Login from '@/components/Login'
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
  async mounted () {
    try {
      const cAuth = Cookie.get('Authorization')
      if (typeof cAuth === 'undefined') {
        throw new TypeError('failed.')
      }
      const auth = JSON.parse(cAuth)
      const resAccess = await this.$axios.$post('/auth/verify', {
        token: auth.access
      })
      const resRefresh = await this.$axios.$post('/auth/verify', {
        token: auth.refresh
      })
      if (Object.entries(resRefresh).length === 0 &&
          resRefresh.constructor === Object) {
      // refresh token is valid.
        if (Object.entries(resAccess).length !== 0 &&
            resAccess.constructor === Object) {
        // access token is NOT valid.
          const { access, refresh } = await this.$axios.$post(
            '/auth/refresh',
            { refresh: auth.refresh }
          )
          auth.refresh = refresh
          auth.access = access
        }
        auth.vuetify = this.$vuetify
        this.$store.commit('auth/setLogin', auth)
      } else {
        throw new TypeError('failed. ff')
      }
    } catch (err) {
      // invalid cookie and logout.
      this.$store.commit('auth/logout', this.$vuetify)
    }
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
