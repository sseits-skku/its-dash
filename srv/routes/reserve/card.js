import express from 'express'
import authzone from '@/middlewares/authzone'
const router = express.Router()

router.use('/', authzone)

router.get('/', (req, res) => {
  // card lists.
  // TODO: do some DB Queries.
})

router.get('/:id', (req, res) => {
  // a card.
  const cardId = req.params.id
  // TODO: do some DB Queries.
})

router.post('/', (req, res) => {
  // upload a card.
  // TODO: do some DB Queries.
})

router.put('/:id', (req, res) => {
  // modify a card
  const cardId = req.params.id
  // TODO: do some DB Queries.
})

router.delete('/', (req, res) => {
  // delete all cards.
  // TODO: do some DB Queries.
})

router.delete('/:id', (req, res) => {
  // delete a card
  const cardId = req.params.id
  // TODO: do some DB Queries.
})

export default router
