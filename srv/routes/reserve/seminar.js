import express from 'express'
import authzone from '@/middlewares/authzone'
const router = express.Router()

router.use('/', authzone)

router.get('/', (req, res) => {
  // seminar lists.
  // TODO: do some DB Queries.
})

router.get('/:id', (req, res) => {
  // a seminar.
  const seminarId = req.params.id
  // TODO: do some DB Queries.
})

router.post('/', (req, res) => {
  // upload a seminar.
  // TODO: do some DB Queries.
})

router.put('/:id', (req, res) => {
  // modify a seminar
  const seminarId = req.params.id
  // TODO: do some DB Queries.
})

router.delete('/', (req, res) => {
  // delete all seminars.
  // TODO: do some DB Queries.
})

router.delete('/:id', (req, res) => {
  // delete a seminar
  const seminarId = req.params.id
  // TODO: do some DB Queries.
})

export default router
