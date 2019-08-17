export default (sequelize, DataTypes) => {
  return sequelize.define('things', {
    id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true,
      field: 'id'
    },
    supplyNumber: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'supply_number'
    },
    discarded: {
      type: DataTypes.BOOLEAN,
      allowNull: false,
      field: 'discarded'
    },
    type: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'type'
    },
    broken: {
      type: DataTypes.BOOLEAN,
      allowNull: false,
      field: 'broken'
    },
    description: {
      type: DataTypes.TEXT,
      allowNull: true,
      field: 'description'
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
