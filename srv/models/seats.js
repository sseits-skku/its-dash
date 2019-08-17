export default (sequelize, DataTypes) => {
  return sequelize.define('seats', {
    id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true,
      field: 'id'
    },
    row: {
      type: DataTypes.INTEGER,
      allowNull: false,
      field: 'row'
    },
    column: {
      type: DataTypes.INTEGER,
      allowNull: false,
      field: 'column'
    },
    createdAt: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.literal('CURRENT_TIMESTAMP'),
      field: 'created_at'
    },
    updatedAt: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.literal('CURRENT_TIMESTAMP'),
      field: 'updated_at'
    }
  }, {
    underscored: true
  })
}
