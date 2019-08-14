<template>
  <v-navigation-drawer
    v-if="drawer"
    permanent
  >
    <v-list
      dense
    >
      <v-list-item
        v-for="(item, index) in items"
        :key="index"
        :to="{path: '/' + item.id}"
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data () {
    return {
      drawer: false,
      items: [
        { id: 'dashboard', title: 'DASHBOARD', icon: 'mdi-view-dashboard' },
        { id: 'timetable', title: 'OH 시간표', icon: 'mdi-calendar' },
        { id: 'gallery', title: '갤러리', icon: 'mdi-image-multiple' },
        { id: 'agenda', title: '안건 게시판', icon: 'mdi-gavel' },
        { id: 'debt', title: '채무 관계', icon: 'mdi-cash-100' },
        { id: 'vote', title: '투표', icon: 'mdi-vote' }
      ]
    }
  },
  created () {
    this.$store.watch(state => state.auth.auth, () => {
      if (this.$store.state.auth.auth !== null) {
        this.drawer = true
      } else {
        this.drawer = false
      }
    })
  }
}
</script>
