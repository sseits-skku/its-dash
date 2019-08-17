import bcrypt from 'bcrypt'

export default {
  comparePassword: passwd => bcrypt.compare(passwd, this.passwd),
  hashPassword: passwd => bcrypt.hash(passwd, 10)
}