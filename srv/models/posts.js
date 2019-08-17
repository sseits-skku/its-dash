export default (sequelize, DataTypes) => {
  return sequelize.define('posts', {
    id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true,
      field: 'id'
    },
    title: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'title'
    },
    content: {
      type: DataTypes.TEXT,
      allowNull: false,
      field: 'content'
    },
    passwd: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'passwd'
    },
    deleted: {
      type: DataTypes.BOOLEAN,
      allowNull: false,
      field: 'deleted'
    },
    ipAddr: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'ip_addr'
    },
    nickname: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'nickname'
    },
    status: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'status'
    },
    category: {
      type: DataTypes.INTEGER,
      allowNull: true,
      field: 'category'
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
