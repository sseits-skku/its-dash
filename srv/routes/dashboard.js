import express from 'express'
import authzone from '@/middlewares/authzone'
const router = express.Router()

router.get('/:work', (req, res) => {
  // workstation computer lists.
  // TODO: do some DB Queries.
})

router.get('/:work/:id', (req, res) => {
  // a workstation computer.
  const workRoomId = req.params.work
  const computerId = req.params.id
  // TODO: do some DB Queries.
})

router.use('/', authzone)

router.post('/:work', (req, res) => {
  // upload a workstation computer.
  const workRoomId = req.params.work
  // TODO: do some DB Queries.
})

router.put('/:work/:id', (req, res) => {
  // modify a workstation computer.
  const workRoomId = req.params.work
  const computerId = req.params.id
  // TODO: do some DB Queries.
})

router.delete('/:work', (req, res) => {
  // delete all workstation computers.
  const workRoomId = req.params.work
  // TODO: do some DB Queries.
})

router.delete('/:work/:id', (req, res) => {
  // delete a workstation computer.
  const workRoomId = req.params.work
  const computerId = req.params.id
  // TODO: do some DB Queries.
})

export default router
