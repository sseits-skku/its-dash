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

/*
import express from 'express'
import authzone from '@/middlewares/authzone'
const router = express.Router()

router.use('/', authzone)

router.get('/', (req, res) => {
  // PLACEHOLDER lists.
  // TODO: do some DB Queries.
})

router.get('/:id', (req, res) => {
  // a PLACEHOLDER.
  const PLACEHOLDERId = req.params.id
  // TODO: do some DB Queries.
})

router.post('/', (req, res) => {
  // upload a PLACEHOLDER.
  // TODO: do some DB Queries.
})

router.put('/:id', (req, res) => {
  // modify a PLACEHOLDER
  const PLACEHOLDERId = req.params.id
  // TODO: do some DB Queries.
})

router.delete('/', (req, res) => {
  // delete all PLACEHOLDERs.
  // TODO: do some DB Queries.
})

router.delete('/:id', (req, res) => {
  // delete a PLACEHOLDER
  const PLACEHOLDERId = req.params.id
  // TODO: do some DB Queries.
})

export default router

*/
