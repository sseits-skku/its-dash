<template>
<!--
  <v-content>
    <v-container
      class="fill-height"
      fluid
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col
          cols="12"
          sm="8"
          md="4"
        >
          <v-card class="elevation-12">
            <v-toolbar
              color="primary"
              dark
              flat
            >
              <v-toolbar-title>Member Login</v-toolbar-title>
              <v-spacer />
              <v-btn></v-btn>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                :model="id"
                label="Login"
                name="login"
                prepend-icon="person"
                type="text"
              />
              <v-text-field
                :model="pw"
                id="password"
                label="Password"
                name="password"
                prepend-icon="lock"
                type="password"
              />
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn
                color="primary"
                @click="$store.commit('dialog', false)"
              >Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
  -->
  <v-dialog
    v-model="dialog"
    persistent
  >
    <v-container
      class="fill-height"
      fluid
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col
          cols="12"
          sm="8"
          md="4"
        >
          <v-card class="elevation-12">
            <v-toolbar
              color="primary"
              dark
              flat
            >
              <v-toolbar-title>Member Login</v-toolbar-title>
              <v-spacer />
              <v-btn
                color="red"
                @click="$store.commit('dialog', false)"
              >
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                :model="id"
                label="Login"
                name="login"
                prepend-icon="mdi-person"
                type="text"
              />
              <v-text-field
                :model="pw"
                id="password"
                label="Password"
                name="password"
                prepend-icon="mdi-lock"
                type="password"
              />
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn
                color="primary"
                @click="postLogin"
              >Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-dialog>
</template>

<script>
import axios from 'axios'
const Cookie = process.client ? import('js-cookie') : undefined

export default {
  created () {
    this.$store.watch(state => state.dialog, () => {
      this.dialog = this.$store.state.dialog
    })
  },
  middleware: 'notAuth',
  data: () => ({
    dialog: false,
    id: '',
    pw: ''
  }),
  methods: {
    postLogin () {
      const auth = {}
      auth.accessToken = ''
      // TODO: do some axios things here.
      this.$store.commit('setAuth', auth)
      Cookie.set('auth', auth)
      this.$store.commit('dialog', false)
      // this.$router.push('/')
    }
  }
}
</script>
