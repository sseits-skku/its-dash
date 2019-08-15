import jwt from 'jsonwebtoken'

const authMiddleware = (req, res, next) => {
  const token = req.headers['x-access-token'] || req.query.token

  if (!token) {
    return res.status(403).json({
      success: false,
      message: '로그인 되지 않음.'
    })
  }

  const p = new Promise(
    (resolve, reject) => {
      jwt.verify(token, req.app.get('jwt-secret'), (err, dec) => {
        if (err) {
          reject(err)
          return
        }
        resolve(dec)
      })
    }
  )
}

export default authMiddleware
