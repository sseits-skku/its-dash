<template>
  <v-toolbar height="80px">
    <v-toolbar-title>
      <div @click.native="$store.commit('goPage', 'main')">SSE-ITS</div>
    </v-toolbar-title>
    <v-spacer />
    <v-toolbar-items>
      <v-menu
        v-for="(item, index) in items"
        :key="index"
        open-on-hover
        top
      >
        <template v-slot:activator="{ on }">
          <v-btn
            :color="item.color"
            v-on="on"
          >
            {{ item.title }}
          </v-btn>
        </template>
        <v-list-item
          v-for="(jtem, jndex) in item.children"
          :key="jndex"
          :to="{path: '/' + jtem.id}"
          color="white"
        >
          {{ jtem.subtitle }}
        </v-list-item>
      </v-menu>
      <v-btn
        color="red"
      >
        {{ recruit.title }}
      </v-btn>
      <v-icon>mdi-dots-vertical</v-icon>
      <v-btn
        color="orange"
      >
        {{ member.title }}
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
// TODO: v-ment말고 다른거로 작성할 생각 해보기.
export default {
  data () {
    return {
      items: [
        {
          title: 'SSE-ITS란?',
          color: 'orange lighten-2',
          children: [
            { id: 'about', subtitle: '소개', icon: '' },
            { id: 'project', subtitle: '프로젝트', icon: '' },
            { id: 'education', subtitle: '교육 자료', icon: '' }
          ]
        },
        {
          title: '워크스테이션실 현황',
          color: 'teal lighten-1',
          children: [
            { id: 'notice', subtitle: '공지사항', icon: '' },
            { id: 'dashboard', subtitle: '현황 보기', icon: '' },
            { id: 'service', subtitle: '건의사항', icon: '' }
          ]
        },
        {
          title: '예약 신청',
          color: 'pink lighten-1',
          children: [
            { id: 'room', subtitle: '세미나실', icon: '' },
            { id: 'register', subtitle: '학생증 등록', icon: '' }
          ]
        }
      ],
      recruit: { id: 'recruit', title: '지원하기' },
      member: { id: 'login', title: '멤버 로그인' }
    }
  }
}
</script>

<style scoped>

</style>
