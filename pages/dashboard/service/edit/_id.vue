<template>
  <PostEdit
    :title="title"
    :post-id="$route.params.id"
    :tempContent="tempContent"
    :category="'service'"
    :content-type="'markdown'"
  />
</template>

<script>
import PostEdit from '@/components/board/PostEdit'
export default {
  components: {
    PostEdit
  },
  async asyncData ({ params, $axios }) {
    console.log(params)
    if (typeof params.id !== 'undefined') {
      const { title, text } = await $axios.$get(`/board/post/${params.id}`)
      return {
        title,
        tempContent: text
      }
    }
    return {
      title: 'do something',
      tempContent: 'DO!!!!'
    }
  }
}
</script>

<style scoped>
</style>
