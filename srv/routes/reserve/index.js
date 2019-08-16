import express from 'express'

import card from './card'
import seminar from './seminar'

const router = express.Router()

router.use('/card', card)
router.use('/seminar', seminar)

export default router
