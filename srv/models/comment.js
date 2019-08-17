export default (sequelize, DataTypes) => {
  const comment = sequelize.define('comment', {
    nickname: {
      type: DataTypes.STRING,
      allowNull: false
    },
    ipAddr: {
      type: DataTypes.STRING,
      allowNull: false
    },
    deleted: {
      type: DataTypes.BOOLEAN,
      allowNull: false,
      defaultValue: false
    },
    content: {
      type: DataTypes.TEXT,
      allowNull: false
    },
    passwd: {
      type: DataTypes.STRING,
      allowNull: false
    },
    createdAt: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.literal('CURRENT_TIMESTAMP')
    },
    updatedAt: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.literal('CURRENT_TIMESTAMP')
    }
  }, {
    underscored: true
  })
  comment.associate = (models) => {
    models.comment.belongsTo(models.post, {
      onDelete: 'SET_NULL',
      foreignKey: {
        field: 'post_id',
        allowNull: true
      }
    })
  }
  return comment
}
