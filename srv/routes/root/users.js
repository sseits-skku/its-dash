import express from 'express'
const router = express.Router()

router.get('/', function(req, res, next) {
  res.json({'default': 'respond user'})
})

export default router