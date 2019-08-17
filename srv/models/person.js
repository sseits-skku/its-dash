export default (sequelize, DataTypes) => {
  const person = sequelize.define('person', {
    id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true,
      field: 'id'
    },
    skkuId: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'skku_id'
    },
    name: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'name'
    },
    memberuser: {
      type: DataTypes.INTEGER,
      allowNull: true,
      field: 'memberuser'
    },
    seminar: {
      type: DataTypes.INTEGER,
      allowNull: true,
      field: 'seminar'
    },
    card: {
      type: DataTypes.INTEGER,
      allowNull: true,
      field: 'card'
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
  person.associate = (models) => {
    models.comment.belongsTo(models.user, {
      onDelete: 'SET_NULL',
      foreignKey: {
        field: 'user_id',
        allowNull: true
      }
    })
    models.comment.belongsTo(models.seminar, {
      onDelete: 'SET_NULL',
      foreignKey: {
        field: 'seminar_id',
        allowNull: true
      }
    })
    models.comment.belongsTo(models.post, {
      onDelete: 'SET_NULL',
      foreignKey: {
        field: 'post_id',
        allowNull: true
      }
    })
  }
  return person
}
