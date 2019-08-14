// app/services/passportStrategy.js
import Passport from 'passport-jwt'

import User from '@/models/user'
import config from '~/secret.config'

const JWTStrategy = Passport.Strategy
const ExtractJwt = Passport.ExtractJwt

// Hooks the JWT Strategy.

function hookJWTStrategy (passport) {
  const options = {
    secretOrKey: config.keys.secret,
    jwtFromRequest: ExtractJwt.fromAuthHeaderWithScheme('jwt'),
    ignoreExpiration: false
  }
  passport.use(new JWTStrategy(options, (JWTPayload, callback) => {
    User.findOne({ where: { username: JWTPayload.username } })
      .then((user) => {
        if (!user) {
          callback(null, false)
          return
        }
        callback(null, user)
      })
  }))
}

export default hookJWTStrategy
