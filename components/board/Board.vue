<template>
  <v-content>
    <v-simple-table
      fixed-header
      class="simpleTable"
      :dark="dark"
    >
      <thead>
        <tr>
          <th
            v-for="(item, idx) in head"
            :key="idx"
            class="text-center"
          >
            {{ item.name }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(item, idx) in body"
          :key="idx"
          class="text-center"
        >
          <td
            v-for="(h, jdx) in head"
            :key="jdx"
          >
            {{ item[h.id] }}
          </td>
        </tr>
      </tbody>
    </v-simple-table>
    <v-container>
      <v-flex>
        <v-row>
          <v-spacer />
          <v-btn color="green lighten-4">{{ write.name }}</v-btn>
        </v-row>
      </v-flex>
    </v-container>
    <v-pagination
      v-model="curPageNum"
      :length="maxPageNum"
      :total-visible="visibleNum"
      circle
      prev-icon="mdi-menu-left"
      next-icon="mdi-menu-right"
    />
  </v-content>
</template>

<script>
export default {
  data () {
    return {
      curPageNum: 1,
      maxPageNum: 100,
      visibleNum: 10,
      head: [
        { id: 'id', name: '번호' },
        { id: 'type', name: 'ui.type' },
        { id: 'title', name: '제목' },
        { id: 'author', name: '글쓴이' },
        { id: 'date', name: '작성 날짜' },
        { id: 'hit', name: '조회수' },
        { id: 'status', name: '상태' }
      ],
      body: [
        // i18n not working because this is fake data.
        // Also not working on real data because that can't be translated.
        { id: 1, type: '일반', title: '안녕하세요_1', author: '이쁜이', date: new Date().toISOString().split('T')[0], hit: 120, status: 'resolved' },
        { id: 2, type: '일반', title: '안녕하세요_2', author: '이쁜이', date: new Date().toISOString().split('T')[0], hit: 121, status: 'resolved' },
        { id: 3, type: '일반', title: '안녕하세요_3', author: '이쁜이', date: new Date().toISOString().split('T')[0], hit: 122, status: 'resolved' },
        { id: 4, type: '일반', title: '안녕하세요_4', author: '이쁜이', date: new Date().toISOString().split('T')[0], hit: 123, status: 'resolved' },
        { id: 5, type: '일반', title: '안녕하세요_5', author: '이븐이', date: new Date().toISOString().split('T')[0], hit: 124, status: 'resolved' },
        { id: 6, type: '일반', title: '안녕하세요_6', author: '이쁜이', date: new Date().toISOString().split('T')[0], hit: 125, status: 'resolved' },
        { id: 7, type: '일반', title: '안녕하세요_7', author: '이쁜이', date: new Date().toISOString().split('T')[0], hit: 126, status: 'resolved' },
        { id: 8, type: '일반', title: '안녕하세요_8', author: '이쁜이', date: new Date().toISOString().split('T')[0], hit: 127, status: 'resolved' },
        { id: 9, type: '일반', title: '안녕하세요_9', author: '이쁜이', date: new Date().toISOString().split('T')[0], hit: 128, status: 'resolved' },
        { id: 10, type: '일반', title: '안녕하세요_10', author: '이쁜이', date: new Date().toISOString().split('T')[0], hit: 129, status: 'resolved' }
      ],
      write: { name: '글 쓰기' }
    }
  }
}
</script>

<style scoped>
.v-simple-table .thead {
  background-color: black;
}
</style>
