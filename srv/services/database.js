import Sequelize from 'sequelize'

import config from '~/secret.config'

export default new Sequelize(
  config.db.name,
  config.db.user,
  config.db.password,
  config.db.detail
)
