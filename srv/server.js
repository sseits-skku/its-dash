import path from 'path'
import bodyParser from 'body-parser'
import consola from 'consola'
import cookieParser from 'cookie-parser'
import express from 'express'
import logger from 'morgan'
import { Nuxt, Builder } from 'nuxt'

import config from '../nuxt.config'

import router from '@/routes/index'
config.dev = process.env.NODE_ENV !== 'production'

async function start () {
  const app = express()
  const nuxt = new Nuxt(config)
  const { host, port } = nuxt.options.server

  if (config.dev) {
    const builder = new Builder(nuxt)
    await builder.build()
  } else {
    await nuxt.ready()
  }

  app.use(logger('dev'))
  app.use(express.json())
  app.use(express.urlencoded({ extended: false }))
  app.use(cookieParser())
  app.use(bodyParser.json())
  app.use(express.static(path.join(__dirname, 'public')))

  app.use('/api', router)
  app.use('/static', express.static('static'))
  app.use((err, req, res, next) => {
    console.error(err.stack)
    if (err.code === 'EBADCSRFTOKEN') {
      res.status(400).json({
        success: false,
        reason: 'CSRF_TOKEN'
      })
    } else {
      res.status(500).json({
        success: false,
        reason: 'SOMETHING_WRONG'
      })
    }
  })

  app.use(nuxt.render)

  app.listen(port)
  consola.ready({
    message: `Server listening on http://${host}:${port}`,
    badge: true
  })
}
start()
