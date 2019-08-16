<template>
  <v-app :dark="isauth">
    <Login />
    <Drawer />
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <Footer />
    <Snackbar />
  </v-app>
</template>

<script>
import Snackbar from '@/components/Snackbar'
import Drawer from '@/components/Drawer'
import Footer from '@/components/Footer'
import Login from '@/components/Login'
// TODO: Pagination 어떻게 처리할지 고민해보기.
export default {
  components: {
    Snackbar,
    Drawer,
    Footer,
    Login
  },
  data () {
    return {
      isauth: false
    }
  },
  created () {
    this.$store.watch(state => state.auth.auth, () => {
      if (this.$store.state.auth.auth !== null) {
        // this.$vuetify.theme.isDark = true
        this.isauth = true
      } else {
        // this.$vuetify.theme.isDark = false
        this.isauth = false
      }
    })
    /*
    this.$store.watch(state => state.currentPage, (newVal, oldVal) => {
      const existPage = [
        'about', 'project', 'education', 'notice',
        'dashboard', 'service', 'room', 'register',
        'recruit', 'login', 'memberadd', 'memberdash',
        'timetable', 'gallery', 'agenda', 'debt', 'vote'
      ]
      const page = this.$store.state.currentPage
      console.log(`${newVal} => ${oldVal}`)
      if (page in existPage) {
        this.$router.push({ path: '/' + page })
      } else {
        this.$router.push({ path: '/' })
      }
    })
    */
  },
  head () {
    return this.$store.state.auth.auth === null
      ? { title: 'SSE-ITS Website' }
      : { title: 'ITS Member zone' }
  }
}
</script>
