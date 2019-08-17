export default (sequelize, DataTypes) => {
  return sequelize.define('seatsThingsThingsSeats', {
    id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true,
      field: 'id'
    },
    thingId: {
      type: DataTypes.INTEGER,
      allowNull: true,
      field: 'thing_id'
    },
    seatId: {
      type: DataTypes.INTEGER,
      allowNull: true,
      field: 'seat_id'
    }
  }, {
    tableName: 'seats_things__things_seats'
  })
}
