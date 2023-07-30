import jwt
import time
import datetime as dt
secret = "wow secret"
algoeithm = "HS256"
iat = dt.datetime.utcnow()
print(type(iat))
# expires = iat + 3600
encoded = jwt.encode({"name":"mehrdad","iat":iat,},secret,algoeithm)

print(encoded)


decoded_token = jwt.decode(encoded,secret,algoeithm)
print(decoded_token)
print(type(decoded_token))