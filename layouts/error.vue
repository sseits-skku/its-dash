<template>
  <v-container
    class="fill-height"
    fluid
  >
    <v-col>
      <v-row
        align="center"
        justify="center"
      >
        <h1 v-if="error.statusCode === 404">
          {{ pageNotFound.detail }}
        </h1>
        <h1 v-else>
          {{ otherError.detail }}
        </h1>
      </v-row>
      <v-row
        align="center"
        justify="center"
      >
        <NuxtLink to="/">
          <h2>{{ this.$t('error.main') }}</h2>
        </NuxtLink>
      </v-row>
    </v-col>
  </v-container>
</template>

<script>
export default {
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  head () {
    const title =
      this.error.statusCode === 404
        ? this.pageNotFound.title
        : this.otherError.title
    return {
      title
    }
  },
  data () {
    return {
      pageNotFound: {
        title: '404 Not Found',
        detail: '페이지를 찾을 수 없습니다.'
      },
      otherError: {
        title: 'An error occurred',
        detail: '웹 사이트에 문제가 생겼습니다. 관리자에게 문의해주세요.'
      }
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 40px;
}
h2 {
  font-size: 28px;
}
</style>
