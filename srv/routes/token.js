import express from 'express'
import authzone from '~/middlewares/authzone'
import config from '@/secret.config'
import { nextTick } from 'q';
const router = express.Router()

router.use(authzone)

router.get('/', (req, res) => {
  const refreshToken = req.headers['x-refresh-token']

  if (!refreshToken) {
    return res.status(400).json({
      success: false,
      reason: 'NOT_LOGGED_IN'
    })
  }

  const p = new Promise(
    (resolve, reject) => {
      jwt.verify(refreshToken, config.secret.refresh, (err, dec) => {
        if (err) {
          reject(err)
          return
        }
        resolve(dec)
      })
    }
  )
  const onError = err =>
    res.status(400).json({
      success: false,
      reason: err.message
    })
  // TODO: 토근 재발급 ㄱㄱ
})

export default router
