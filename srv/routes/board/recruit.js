import express from 'express'
import authzone from '~/middlewares/authzone'
const router = express.Router()

// TODO: make something...

router.post('/', (req, res) => {
  // upload a recruit.
})

router.use('/', authzone)

router.get('/', (req, res) => {
  // recruit lists.
})

router.get('/:id', (req, res) => {
  // a recruit.
  const recruitId = req.params.id
  // TODO: do some DB Queries.
})

router.delete('/', (req, res) => {
  // delete all recruits.
})

router.delete('/:id', (req, res) => {
  // delete a recruit
  const recruitId = req.params.id

  // TODO: do some DB Queries.
})

export default router
