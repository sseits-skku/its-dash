<template>
  <Toolbar />
</template>

<script>
import Toolbar from '@/components/Toolbar'
export default {
  layout () {
    return this.$store.state.logon ? 'default' : 'memberzone'
  },
  components: {
    Toolbar
  }
}
</script>
