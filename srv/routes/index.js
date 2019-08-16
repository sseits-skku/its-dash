import express from 'express'

import recruit from './recruit'
import notice from './notice'
import dashboard from './dashboard'
import service from './service'
import room from './room'
import register from './register'
import login from './login'
import user from './user'
import token from './token'

const router = express.Router()
router.use('/recruit', recruit)
router.use('/notice', notice)
router.use('/dashboard', dashboard)
router.use('/service', service)
router.use('/room', room)
router.use('/register', register)
router.use('/login', login)
router.use('/user', user)
router.use('/token', token)

export default router
