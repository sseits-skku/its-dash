<template>
  <PostEdit
    :title="''"
    :tempContent="''"
    :category="'service'"
    :content-type="'markdown'"
  />
</template>

<script>
import PostEdit from '@/components/board/PostEdit'
export default {
  components: {
    PostEdit
  }
}
</script>

<style scoped>
</style>
