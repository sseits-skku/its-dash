import express from 'express'
import { User } from '~/models/user'
import authzone from '~/middlewares/authzone'

const router = express.Router()

router.post('/', (req, res) => {
  const { loginId, passwd, studentId, name, email } = req.body
  User
    .fineOrCreate({ where: { studentId }, defaults: { loginId, passwd, studentId, name, email } })
    .then(([user, created]) => {
      if (!created) {
        return res.json({
          success: false,
          reason: 'ALREADY_EXISTS'
        })
      }
      return res.json({
        success: true,
        reason: 'SUCCESS'
      })
    })
    .catch((err) => { throw err })
})

router.use('/', authzone)

router.get('/', (req, res) => {
})

export default router
