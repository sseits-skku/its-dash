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
    comparePasswords: (passwd, callback) => {
      bcrypt.compare(passwd, this.passwd, function (error, isMatch) {
        if (error) {
          return callback(null, isMatch)
        }
      })
    },
    hashPassword: (user) => {
      if (user.changed('passwd')) {
        return bcrypt.hash(user.passwd, 10).then((passwd) => {
          user.passwd = passwd
        })
      }
    }
  }
}

const UserModel = db.define('user', modelDefinition, modelOptions)
export default UserModel
