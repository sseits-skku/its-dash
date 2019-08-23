<template>
  <v-navigation-drawer
    permanent
    width="320px"
    app
  >
    <v-toolbar
      color="teal lighten-1"
      dark
      height="80px"
    >
      <v-spacer />
      <v-btn class="elevation-0" color="transparent" :ripple="false" large>
        <div class="display-1">SSE-ITS</div>
      </v-btn>
      <v-spacer />
    </v-toolbar>
    <v-list>
      <v-list-group
        v-for="item in memberItems"
        :key="item.title"
        v-model="item.active"
        :prepend-icon="item.icon"
        no-action
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </template>

        <v-list-item
          v-for="subItem in item.items"
          :key="subItem.title"
          @click="doNothing"
        >
          <v-list-item-content>
            <v-list-item-title v-text="subItem.title" />
          </v-list-item-content>
          <v-list-item-action v-if="'icon' in subItem">
            <v-icon v-text="subItem.icon" />
          </v-list-item-action>
        </v-list-item>
      </v-list-group>
    </v-list>
    <template v-slot:append>
      <div class="pa-2">
        <v-btn color="primary" block @click="openDialog">
          <v-icon left>mdi-lock-open</v-icon> MEMBER LOGIN
        </v-btn>
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script>
export default {
  data () {
    return {
      guestItems: [
        {
          icon: 'mdi-account-supervisor-circle',
          title: 'SSE-ITS 소개',
          items: [
            { id: 'about', title: 'SSE-ITS란?' },
            { id: 'project', title: '프로젝트' },
            { id: 'education', title: '교육자료' },
            { id: 'recruit', title: '지원하기' }
          ]
        },
        {
          icon: 'mdi-monitor-dashboard',
          title: '워크스테이션실',
          items: [
            { id: 'notice', title: '공지사항' },
            { id: 'dashboard', title: '현황 보기' },
            { id: 'service', title: '건의 사항' }
          ]
        },
        {
          icon: 'mdi-calendar-check',
          title: '예약하기',
          items: [
            { id: 'room', title: '세미나실' },
            { id: 'register', title: '학생증 등록' }
          ]
        }
      ]
    }
  },
  computed: {
    memberItems () {
      return this.guestItems.concat([
        {
          icon: 'mdi-incognito',
          title: '멤버전용 패널',
          items: [
            { id: 'memberdash', title: '대시보드', icon: 'mdi-view-dashboard' },
            { id: 'timetable', title: 'OH 시간표', icon: 'mdi-calendar' },
            { id: 'gallery', title: '갤러리', icon: 'mdi-image-multiple' },
            { id: 'agenda', title: '안건게시판', icon: 'mdi-gavel' },
            { id: 'debt', title: '채무관계', icon: 'mdi-cash-100' },
            { id: 'vote', title: '투표', icon: 'mdi-vote' }
          ]
        }
      ])
    }
  },
  methods: {
    openDialog () {
      // TODO: do something...
    },
    doNothing () {
      // TODO: do something...
    }
  }
}
</script>

<style scoped>
.v-simple-table .thead {
  background-color: black;
}
</style>
<!--
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
        { id: 'memberdash', title: 'DASHBOARD', icon: 'mdi-view-dashboard' },
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
-->
