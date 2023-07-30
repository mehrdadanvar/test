import time
import os
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import HTTPException, Request, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
secret_key = os.getenv("JWT_SECRET")
secret_algorithem = os.getenv("JWT_ALGORITHM")


def generate_token(user):
    iat = time.time()
    expires = iat + 3600
    encododed_token = jwt.encode({"email": user.email, "iat": iat,
                                 "expires": expires}, key=secret_key, algorithm=secret_algorithem)
    return encododed_token


def decode_token(token, user):
    is_token_valid = False
    claimed_token = jwt.decode(
        token, key=secret_key, algorithms=secret_algorithem)
    print(claimed_token)
    print(type(claimed_token))
    if user.email == claimed_token["email"] and claimed_token["expires"] >= time.time():
        print("users matched and token as not expired")
        is_token_valid = True
        return is_token_valid
    else:
        return is_token_valid


async def authMiddleware(request: Request, response: Response,):
    print("middleware working from authMiddleware function")
    print(request.headers)
    print(response.body)
    return response


class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request):
        credentails: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        print(credentails)
        if credentails:
            if not credentails.scheme == "Bearer":
                raise HTTPException(status_code=403, details={
                                    "message": "Invalid or expired token"})
            else:
                return credentails.credentials
        else:
            raise HTTPException(status_code=403, details={
                                "message": "Invalid or expired token"})

    def verify_jwt(self, claimed_token: str):
        is_token_valid: bool = False
        claimed_payload = decode_token(claimed_token)
        print(claimed_token)
        if claimed_payload:
            is_token_valid = True
            return is_token_valid
        else:
            return is_token_valid
