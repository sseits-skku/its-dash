<template>
  <v-dialog
    v-model="diaOpen"
    width="480px"
  >
    <v-card
      class="elevation-12"
    >
      <v-toolbar
        color="primary"
        dark
        flat
      >
        <v-toolbar-title>Member Login</v-toolbar-title>
        <v-spacer />
        <v-btn
          color="red"
          rounded
          @click="diaOpen = false"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text>
        <v-text-field
          v-model="id"
          label="Login"
          name="login"
          prepend-icon="mdi-account"
          type="text"
          @keyup.enter.native="postLogin"
        />
        <v-text-field
          v-model="pw"
          label="Password"
          name="password"
          prepend-icon="mdi-lock"
          type="password"
          @keyup.enter.native="postLogin"
        />
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn
          class="mb-4"
          color="primary"
          fab
          rounded
          :loading="isPending"
          @click="postLogin"
          @keyup.enter.native="postLogin"
        >
          <v-icon>mdi-send</v-icon>
        </v-btn>
        <v-spacer />
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data: () => ({
    isPending: false,
    id: '',
    pw: ''
  }),
  computed: {
    diaOpen: {
      get () { return this.$store.state.loginDialogOpen },
      set (value) { this.$store.commit('setLoginDialogOpen', value) }
    }
  },
  created () {
  },
  methods: {
    async postLogin () {
      this.isPending = true
      try {
        const { access, refresh } = await this.$axios.$post('/auth/', {
          username: this.id,
          password: this.pw
        })
        const userId = JSON.parse(atob(access.split('.')[1])).user_id
        const isStaff = await this.$axios.$get(`/account/user/${userId}`)
        this.$store.commit('auth/setLogin', {
          vuetify: this.$vuetify,
          username: this.id,
          refresh,
          access,
          isStaff
        })
        this.id = ''
        this.pw = ''
        this.diaOpen = false
        this.isPending = false
      } catch (err) {
        console.log(err)
      }
    }
  }
}
</script>
