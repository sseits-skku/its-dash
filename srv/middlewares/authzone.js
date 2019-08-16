import jwt from 'jsonwebtoken'
import config from '@/secret.config'

export default (req, res, next) => {
  const accessToken = req.headers['x-access-token']

  if (!accessToken) {
    return res.status(400).json({
      success: false,
      reason: 'NOT_LOGGED_IN'
    })
  }

  const p = new Promise(
    (resolve, reject) => {
      jwt.verify(accessToken, config.secret.access, (err, dec) => {
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

  p.then((dec) => {
    req.decoded = dec
    next()
  }).catch(onError)
}
