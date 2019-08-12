import express from 'express'
import root from './root/index'

const router = express.Router()

router.use('/', root)

export default router
