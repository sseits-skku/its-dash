export default (sequelize, DataTypes) => {
  const category = sequelize.define('category', {
    title: {
      type: DataTypes.STRING(255),
      allowNull: false
    }
  }, {
    underscored: true
  })
  category.associate = (models) => {
    models.category.hasMany(models.post, {
      onDelete: 'SET_NULL',
      foreignKey: {
        allowNull: false
      }
    })
  }
  return category
}
