import express from 'express'
import { User } from '@/models/user'

const router = express.Router()

router.post('/', (req, res) => {
  const { id, passwd } = req.body

  if (!id || !passwd) {
    return res.status(400).json({
      success: false,
      reason: 'EMPTY_INPUT'
    })
  }

  User.findOne({ where: { loginId: id } })
    .then()
    .catch()
})
// TODO: make something...

export default router
