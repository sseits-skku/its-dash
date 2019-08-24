<template>
  <v-navigation-drawer
    v-model="dOpen"
    app
    :permanent="dPerm"
    width="320px"
  >
    <v-toolbar
      color="teal lighten-1"
      dark
      height="80px"
    >
      <v-spacer />
      <v-btn
        class="elevation-0"
        color="transparent"
        :ripple="false"
        large
        @click.native="goPage('/')"
      >
        <div class="display-1">SSE-ITS</div>
      </v-btn>
      <v-spacer />
    </v-toolbar>
    <v-list>
      <v-list-group
        v-for="item in guestItems"
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
          @click="goPage(subItem.id)"
        >
          <v-list-item-content>
            <v-list-item-title v-text="subItem.title" />
          </v-list-item-content>
          <v-list-item-action v-if="'icon' in subItem">
            <v-icon v-text="subItem.icon" />
          </v-list-item-action>
        </v-list-item>
      </v-list-group>
      <template
        v-if="$store.state.auth.isStaff"
      >
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
            @click="goPage(subItem.id)"
          >
            <v-list-item-content>
              <v-list-item-title v-text="subItem.title" />
            </v-list-item-content>
            <v-list-item-action v-if="'icon' in subItem">
              <v-icon v-text="subItem.icon" />
            </v-list-item-action>
          </v-list-item>
        </v-list-group>
      </template>
    </v-list>
    <template v-slot:append>
      <div
        v-if="$store.state.auth.username === ''"
        class="px-2 pb-2"
      >
        <v-btn color="secondary" block @click="goPage('/add')">
          <v-icon left>mdi-lock-open</v-icon> REGISTRATION
        </v-btn>
      </div>
      <div
        v-if="$store.state.auth.username === ''"
        class="px-2 pb-2"
      >
        <v-btn color="primary" block @click="openDialog">
          <v-icon left>mdi-lock-open</v-icon> MEMBER LOGIN
        </v-btn>
      </div>
      <div
        v-if="$store.state.auth.username !== ''"
        class="px-2 pb-2"
      >
        <v-btn color="primary" block @click="logout">
          <v-icon left>mdi-logout-variant</v-icon> LOGOUT
        </v-btn>
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script>
export default {
  data () {
    return {
      memberItems: [
        {
          icon: 'mdi-incognito',
          title: '멤버전용 패널',
          items: [
            { id: '/member/memberdash', title: '대시보드', icon: 'mdi-view-dashboard' },
            { id: '/member/inventory', title: '비품 관리', icon: 'mdi-package-variant' },
            { id: '/member/timetable', title: 'OH 시간표', icon: 'mdi-calendar' },
            { id: '/member/gallery', title: '갤러리', icon: 'mdi-image-multiple' },
            { id: '/member/agenda', title: '안건게시판', icon: 'mdi-gavel' },
            { id: '/member/debt', title: '채무관계', icon: 'mdi-cash-100' },
            { id: '/member/vote', title: '투표', icon: 'mdi-vote' }
          ]
        }
      ],
      guestItems: [
        {
          icon: 'mdi-account-supervisor-circle',
          title: 'SSE-ITS 소개',
          items: [
            { id: '/sseits', title: 'SSE-ITS란?' },
            { id: '/sseits/project', title: '프로젝트' },
            { id: '/sseits/education', title: '교육자료' },
            { id: '/sseits/recruit', title: '지원하기' }
          ]
        },
        {
          icon: 'mdi-monitor-dashboard',
          title: '워크스테이션실',
          items: [
            { id: '/dashboard/notice', title: '공지사항' },
            { id: '/dashboard', title: '현황 보기' },
            { id: '/dashboard/service', title: '건의 사항' }
          ]
        },
        {
          icon: 'mdi-calendar-check',
          title: '예약하기',
          items: [
            { id: '/reserve/seminar', title: '세미나실' },
            { id: '/reserve/card', title: '학생증 등록' }
          ]
        }
      ]
    }
  },
  computed: {
    dOpen: {
      get () { return this.$store.state.drawerOpen },
      set (value) { this.$store.commit('setDrawerOpen', value) }
    },
    dPerm: {
      get () { return this.$store.state.drawerPerm },
      set (value) { this.$store.commit('setDrawerPerm', value) }
    }
  },
  methods: {
    logout () {
      this.$store.commit('auth/logout', this.$vuetify)
    },
    openDialog () {
      this.$store.commit('setLoginDialogOpen', true)
    },
    goPage (id) {
      this.$router.push(id).catch(() => {})
    }
  }
}
</script>

<style scoped>
.v-simple-table .thead {
  background-color: black;
}
</style>
