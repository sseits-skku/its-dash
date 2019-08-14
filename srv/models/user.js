import Sequelize from 'sequelize'
import bcrypt from 'bcrypt'

import secret from '~/secret.config'
import db from '@/services/database'

const modelDefinition = {
  username: {
    type: Sequelize.STRING,
    unique: true,
    allowNull: false
  },
  password: {
    type: Sequelize.STRING,
    allowNull: false
  }
}

const modelOptions = {
  instanceMethods: {
    comparePasswords: (password, callback) => {
      bcrypt.compare(password, this.password, function (error, isMatch) {
        if (error) {
          return callback(null, isMatch)
        }
      })
    },
    hashPassword: (user) => {
      if (user.changed('password')) {
        return bcrypt.hash(user.password, 10).then((password) => {
          user.password = password
        })
      }
    }
  }
}

const UserModel = db.define('user', modelDefinition, modelOptions)
export default UserModel
