import express from 'express'
import authzone from '@/middlewares/authzone'
const router = express.Router()

router.get('/', (req, res) => {
  // notice lists.
})

router.get('/:id', (req, res) => {
  // a notice.
  const noticeId = req.params.id

  // TODO: do some DB Queries.
})

router.use('/', authzone)

router.post('/', (req, res) => {
  // upload a notice.
})

router.delete('/', (req, res) => {
  // delete all notices.
  // it's too dangerous,
  // so I will not implement this.
  return res.status(400).json({
    success: false,
    reason: 'TOO_DANGEROUS_OPERATION'
  })
})

router.delete('/:id', (req, res) => {
  // delete a notice
  const noticeId = req.params.id

  // TODO: do some DB Queries.
})

export default router
