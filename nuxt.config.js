const webpack = require('webpack')

module.exports = {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    titleTemplate: '%s - ' + process.env.npm_package_name,
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [
  ],
  /*
  ** Plugins to load before mounting the App
  */
  /*
  ** Nuxt.js dev-modules
  */
  devModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module',
    '@nuxtjs/vuetify'
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios'/*,
    '@nuxtjs/pwa' */
  ],
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
    proxy: true
  },
  proxy: {
  },
  vue: {
    config: {
      productionTip: false,
      devtools: true
    }
  },
  /*
  ** vuetify module configuration
  ** https://github.com/nuxt-community/vuetify-module
  */
  vuetify: {
    defaultAssets: {
      font: false,
      icons: 'mdi'
    }/*,
    theme: {
      themes: {
        light: {
          primary: colors.blue.lighten2,
          accent: colors.grey.base,
          secondary: colors.amber.lighten1,
          info: colors.teal.lighten4,
          warning: colors.amber.lighten2,
          error: colors.deepOrange.accent2,
          success: colors.green.accent2
        },
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    } */
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    analyze: false,
    babel: {
      'presets': [
        '@babel/preset-env'
      ],
      plugins: [
        '@babel/transform-runtime'
      ]
    },
    cache: true,
    cssSourceMap: false,
    extend (config, ctx) {
    },
    parallel: true,
    plugins: [
      new webpack.DefinePlugin({
        'process.VERSION': require('./package.json').version
      })
    ]
  }
}
