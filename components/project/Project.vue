<template>
  <div>
    <v-card
      max-width="280px"
      max-height="400px"
      class="ma-2"
    >
      <v-img
        width="270px"
        height="180px"
        :src="typeof image !== undefined ? image : defaultImage"
      >
        <v-card-title
          class="align-end justify-end fill-height"
        >
          {{ title }}
        </v-card-title>
      </v-img>
      <v-card-text class="pa-2">
        <span>기여자: {{ author }}</span><br>
        <span
          class="text--primary"
        >{{ text }}</span>
      </v-card-text>
      <v-card-actions
        class="py-0"
      >
        <v-spacer />
        <v-btn
          v-show="typeof golink !== 'undefined'"
          text
          icon
          :href="golink"
        >
          <v-icon>mdi-exit-to-app</v-icon>
        </v-btn>
        <v-btn
          v-show="typeof github !== 'undefined'"
          text
          icon
          :href="github"
        >
          <v-icon>mdi-git</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    image: { type: String, default: '/img/dummy_logo.png' },
    title: { type: String, default: 'Dummy Title' },
    author: { type: String, default: 'Author 1, Author 2' },
    text: { type: String, default: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud.' },
    golink: { type: String, default: 'https://www.naver.com' },
    github: { type: String, default: 'https://www.github.com/sseits-skkku' }
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
</style>
