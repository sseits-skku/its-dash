export default (sequelize, DataTypes) => {
  return sequelize.define('user', {
    id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    loginId: {
      type: DataTypes.STRING,
      allowNull: false
    },
    passwd: {
      type: DataTypes.STRING,
      allowNull: false
    },
    nickname: {
      type: DataTypes.STRING,
      allowNull: true
    },
    email: {
      type: DataTypes.STRING,
      allowNull: false
    },
    active: {
      type: DataTypes.BOOLEAN,
      allowNull: false
    },
    description: {
      type: DataTypes.TEXT,
      allowNull: true
    },
    person: {
      type: DataTypes.INTEGER,
      allowNull: true
    },
    phone: {
      type: DataTypes.STRING,
      allowNull: false
    },
    birthDay: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.literal('CURRENT_TIMESTAMP')
    }
  })
}
