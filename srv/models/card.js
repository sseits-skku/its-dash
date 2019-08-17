export default (sequelize, DataTypes) => {
  return sequelize.define('card', {
    phone: {
      type: DataTypes.STRING,
      allowNull: false
    },
    person: { // one to one
      type: DataTypes.INTEGER,
      allowNull: false
    },
    visitDate: {
      type: DataTypes.DATE,
      allowNull: false
    },
    createdDate: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.literal('CURRENT_TIMESTAMP')
    }
  }, {
    underscored: true
  })
}
