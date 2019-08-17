export default (sequelize, DataTypes) => {
  return sequelize.define('seminars', {
    id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true,
      field: 'id'
    },
    room: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'room'
    },
    startTime: {
      type: DataTypes.DATE,
      allowNull: false,
      defaultValue: sequelize.literal('CURRENT_TIMESTAMP'),
      field: 'start_time'
    },
    endTime: {
      type: DataTypes.DATE,
      allowNull: false,
      defaultValue: sequelize.literal('CURRENT_TIMESTAMP'),
      field: 'end_time'
    },
    borrow: {
      type: DataTypes.INTEGER,
      allowNull: true,
      field: 'borrow'
    },
    phone: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'phone'
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
