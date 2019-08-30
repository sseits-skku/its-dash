<template>
  <!-- eslint-disable vue/no-v-html -->
  <v-layout
    align-center
    justify-center
  >
    <v-card
      min-width="600px"
    >
      <v-card-title>
        <v-text-field
          v-model="title"
          label="제목"
          filled
        />
      </v-card-title>
      <v-card-text>
        <v-textarea
          v-if="!showPreview"
          id="inputTextField"
          v-model="textContent"
          label="내용"
          counter
          single-line
          full-width
          auto-grow
        />
        <div
          v-if="!!(showPreview)"
          class="text--primary"
          v-html="shownContent"
        />
      </v-card-text>
      <v-card-actions>
        <v-btn
          class="grey lighten-3"
          @click.native="showPreview = !showPreview"
        >
          미리보기
        </v-btn>
        <v-btn
          class="grey lighten-2"
          @click.native="imageDialog = !imageDialog"
        >
          <v-icon>mdi-image-plus</v-icon>
        </v-btn>
        <v-spacer />
        <v-btn
          class="primary"
          @click.native="submitPost"
        >
          등록
        </v-btn>
      </v-card-actions>
    </v-card>
    <v-dialog
      v-model="imageDialog"
      width="500px"
    >
      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          이미지 첨부
        </v-card-title>
        <v-card-text
          class="text-center"
        >
          <v-file-input
            v-model="imageFile"
            label="File input"
            show-size
          />
        </v-card-text>
        <v-divider />
        <v-card-actions>
          <v-spacer />
          <v-btn
            large
            @click="imageFile = null; imageDialog = !imageDialog"
          >
            취소
          </v-btn>
          <v-spacer />
          <v-btn
            class="primary"
            large
            @click="imageUpload"
          >
            첨부
          </v-btn>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import Base64 from 'base64-js'
import Pako from 'pako'

export default {
  props: {
    category: {
      type: String,
      default: ''
    }, // eslint-disable-next-line vue/prop-name-casing
    'content-type': {
      type: String,
      default: 'markdown'
    },
    'post-id': {
      type: Number,
      default: NaN
    },
    title: {
      type: String,
      default: ''
    },
    tempContent: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      imageFile: null,
      imageDialog: false,
      showPreview: false,
      textContent: '',
      imageGroup: [],
      md: null
    }
  },
  computed: {
    cursorStart: {
      get () {
        if (process.client) {
          const el = document.getElementById('inputTextField')
          return el.selectionStart
        }
        return 0
      },
      set (value) {
        if (process.client) {
          const el = document.getElementById('inputTextField')
          el.selectionStart = value
        }
      }
    },
    cursorEnd: {
      get () {
        if (process.client) {
          const el = document.getElementById('inputTextField')
          return el.selectionEnd
        }
        return 0
      },
      set (value) {
        if (process.client) {
          const el = document.getElementById('inputTextField')
          el.selectionEnd = value
        }
      }
    },
    shownContent () { return this.$md.render(this.textContent) },
    compressedContent () {
      return Pako.gzip(this.textContent, { level: 9 }).toString()
    }
  },
  mounted () {
    console.log(new Uint8Array(this.tempContent.split(',')))
    if (this.tempContent) {
      this.textContent = String.fromCharCode.apply(null,
        Pako.ungzip(
          new Uint8Array(this.tempContent.split(','))
        )
      )
    }
  },
  methods: {
    async imageUpload () {
      if (this.imageFile !== null) {
        const form = this.formData ? this.formData : new FormData()
        form.append('image', this.imageFile)

        const res = await this.$axios.$post('/content/image/', form, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: 'Bearer ' + this.$store.state.auth.accessToken
          }
        })
        // res.image is imageURL
        this.textContent +=
          '![이미지 설명](' +
          res.image +
          ')'
      }
    },
    async submitPost () {
      const auth = {
        username: this.$store.state.auth.username,
        isStaff: this.$store.state.auth.isStaff,
        refresh: this.$store.state.auth.refreshToken,
        access: this.$store.state.auth.accessToken
      }
      this.$store.dispatch('auth/checkLogin', this.$vuetify)
      try {
        const categories = this.$axios.$get('/board/category/')
        console.log(await categories)
        const curIP = '0.0.0.0' // TODO: should be fixed.
        const owner = JSON.parse(
          atob(auth.access.split('.')[1])
        ).user_id
        if (typeof owner === 'undefined') {
          throw new TypeError('로그아웃되었습니다. 로그인해주세요.')
        }
        if (!(await categories).results.find(x => x.title === this.category)) {
          throw new Error('카테고리가 설정되지 않았습니다.')
        }
        if (this.title === '') {
          throw new Error('제목을 적어주세요.')
        }
        if (this.textContent === '') {
          throw new Error('내용을 적어주세요.')
        }
        console.log(this.$route.params.id)
        if (typeof this.$route.params.id === 'undefined') {
          console.log('POST!')
          const res = this.$axios.$post('/board/post/', {
            title: this.title,
            content_type: this.contentType,
            category: (await categories).results.find(x => x.title === this.category).id,
            text: this.compressedContent,
            ip_addr: curIP,
            owner
          }, {
            headers: {
              Authorization: 'Bearer ' + auth.access
            }
          })
          console.log(await res)
        } else {
          console.log('PUT!')
          const res = this.$axios.$put('/board/post/', {
            id: this['post-id'],
            title: this.title,
            content_type: this.contentType,
            category: (await categories).results.find(x => x.title === this.category).id,
            text: this.compressedContent,
            ip_addr: curIP,
            owner
          }, {
            headers: {
              Authorization: 'Bearer ' + auth.access
            }
          })
          console.log(await res)
        }
      } catch (err) {
        console.error(err)
        this.$store.commit('snackbar/setSnack', err, 'error')
      }
    }
  }
}
</script>

<style scoped>
</style>
