import express from 'express'

import board from './board/index'
import dashboard from './dashboard'
import reserve from './reserve/index'
import user from './user/index'
import token from './token'

const router = express.Router()
router.use('/dash', dashboard)
router.use('/reserve', reserve)
router.use('/board', board)
router.use('/user', user)
router.use('/token', token)

export default router
