import express from 'express'
import authzone from '~/middlewares/authzone'
const router = express.Router()

router.get('/', (req, res) => {
  // service request lists.
})

router.get('/:id', (req, res) => {
  // a service request.
  const serviceId = req.params.id

  // TODO: do some DB Queries.
})

router.post('/', (req, res) => {
  // upload a service request.
})

router.put('/:id', (req, res) => {
  // upload a service request.
  const serviceId = req.params.id

  // TODO: do some DB Queries.
})

router.use('/', authzone)

router.delete('/', (req, res) => {
  // delete all service requests.
  // it's too dangerous,
  // so I will not implement this.
  return res.status(400).json({
    success: false,
    reason: 'TOO_DANGEROUS_OPERATION'
  })
})

router.delete('/:id', (req, res) => {
  // delete a service request
  const serviceId = req.params.id

  // TODO: do some DB Queries.
})

export default router
