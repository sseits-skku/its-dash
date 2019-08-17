import fs from 'fs'
import path from 'path'
import Sequelize from 'sequelize'

import user from './user'
import rawConfig from '@/config/config.json'

const env = process.env.NODE_ENV || 'development'
const config = rawConfig[env]
const db = {}

const sequelize = new Sequelize(config)

db.User = user(sequelize, Sequelize)

Object.keys(db).forEach((modelName) => {
  if (db[modelName].associate) {
    db[modelName].associate(db)
  }
})

db.sequelize = sequelize
db.Sequelize = Sequelize

export default db
