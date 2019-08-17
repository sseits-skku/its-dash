import express from 'express'
import { User } from '~/models/user'
import authzone from '@/middlewares/authzone'

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
  // get all users
})

router.put('/:id', (req, res) => {
  const userId = req.params.id
})

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
