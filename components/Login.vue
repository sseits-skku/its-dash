<template>
  <v-dialog
    v-model="dialog"
    width="480px"
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
          rounded
          @click="dialog = false"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text>
        <v-text-field
          :model="id"
          label="Login"
          name="login"
          prepend-icon="mdi-account"
          type="text"
        />
        <v-text-field
          id="password"
          label="Password"
          name="password"
          prepend-icon="mdi-lock"
          type="password"
          :model="pw"
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
    dialog: false,
    isPending: false,
    id: '',
    pw: ''
  }),
  created () {
  },
  methods: {
    postLogin () {
      // TODO: login things...
    }
  }
}
</script>
