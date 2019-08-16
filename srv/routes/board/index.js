import express from 'express'

import notice from './notice'
import recruit from './recruit'
import service from './service'

const router = express.Router()

router.use('/notice', notice)
router.use('/recruit', recruit)
router.use('/service', service)

export default router
