<template>
  <v-container fluid fill-height>
    <v-layout
      justify-center
      align-center
    >
      <v-col
        v-show="$vuetify.breakpoint.xs"
        class="display-2 font-weight-bold text-center"
      >
        화면이 너무 작아서 대시보드를 사용할 수 없습니다.
      </v-col>
      <v-col
        v-show="$vuetify.breakpoint.smAndUp"
      >
        <v-flex
          row
        >
          <v-row>
            <v-btn
              block
              class="grey lighten-1 mb-4"
              :ripple="false"
              text
              @click.native="isClicked = !isClicked"
            >
              칠판
            </v-btn>
            <v-row
              v-for="(i, idx) in Array(4).keys()"
              :key="idx"
              class="Dashboard"
              align-center
              justify-center
            >
              <v-col
                v-for="(j, jdx) in Array(4).keys()"
                :key="`L-${jdx}`"
                no-gutters
                class="pa-1"
              >
                <v-btn
                  block
                  class="Dbtn"
                  :color="seatGrid[idx][jdx].cls"
                />
              </v-col>
              <div class="Dempty" />
              <v-col
                v-for="(j, jdx) in Array(6).keys()"
                :key="`M-${jdx}`"
                no-gutters
                class="pa-1"
              >
                <v-btn
                  block
                  class="Dbtn"
                  :color="seatGrid[idx][jdx+4].cls"
                />
              </v-col>
              <div class="Dempty" />
              <v-col
                v-for="(j, jdx) in Array(4).keys()"
                :key="`R-${jdx}`"
                no-gutters
                class="pa-1"
              >
                <v-btn
                  block
                  class="Dbtn"
                  :color="seatGrid[idx][jdx+10].cls"
                />
              </v-col>
            </v-row>
          </v-row>
        </v-flex>
      </v-col>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    isClicked: false,
    seatGrid: null,
    totalRow: 4,
    leftCol: 4,
    middleCol: 6,
    rightCol: 4,
    defaultSeat: {
      cls: 'blue darken-2'
    }
  }),
  created () {
    this.seatGrid = Array(4).fill(
      Array(14).fill(this.defaultSeat)
    )
  },
  methods: {
  }
}
</script>

<style scoped>
.Dempty{
  width: 3%;
}
.Dbtn {
  width: 100%;
  height: 100%;
}
.Dashboard {
  flex-flow: nowrap;
  width: 100%;
}
</style>
