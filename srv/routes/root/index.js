import express from 'express'
import postsRouter from './posts'
import usersRouter from './users'

const router = express.Router()
router.use('/users', postsRouter)
router.use('/posts', usersRouter)

export default router