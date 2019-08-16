// Change file name to `secret.config.js`

export default {
  db: {
    user: 'username',
    password: 'password',
    name: 'database',
    detail: {
      host: 'your.db.com',
      port: '1234',
      dialect: 'mariadb'
    }
  },
  secret: {
    access: 'something-s3cr3t-things',
    refresh: 'something-s3cr3t-thIngs'
  }
}
