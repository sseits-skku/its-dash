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
        />
        <v-text-field
          v-model="pw"
          label="Password"
          name="password"
          prepend-icon="mdi-lock"
          type="password"
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
    postLogin () {
      this.isPending = true
      this.$axios.$post('/auth/', {
        username: this.id,
        password: this.pw
      }).then((res) => {
        const { access, refresh } = res
        this.$store.commit('auth/setLogin', {
          username: this.id,
          refresh,
          access
        })
      })
      this.diaOpen = false
      this.isPending = false
      this.$vuetify.theme.dark = true
    }
  }
}
</script>
