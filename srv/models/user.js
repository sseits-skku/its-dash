import Sequelize from 'sequelize'
import bcrypt from 'bcrypt'

import db from '@/services/database'

const modelDefinition = {
  loginId: {
    type: Sequelize.STRING,
    unique: true,
    allowNull: false
  },
  passwd: {
    type: Sequelize.STRING,
    allowNull: false
  },
  studentId: {
    type: Sequelize.STRING,
    allowNull: false
  },
  name: {
    type: Sequelize.STRING,
    allowNull: false
  },
  email: {
    type: Sequelize.STRING,
    allowNull: false
  }
}

const modelOptions = {
  instanceMethods: {
    comparePassword: passwd => bcrypt.compare(passwd, this.passwd),
    hashPassword: passwd => bcrypt.hash(passwd, 10)
  }
}

export default (sequelize, DataTypes) => db.define('user', modelDefinition, modelOptions)
