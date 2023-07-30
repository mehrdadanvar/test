from datetime import datetime as dt
from fastapi import APIRouter, HTTPException, status, Response, Depends, Request
from pydantic import BaseModel, Field, root_validator, validator, constr
import hashlib
from db import student_collection
from auth import generate_token,  jwtBearer, decode_token, authMiddleware
import secrets
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from auth import secret_algorithem, secret_key
import time
from datetime import datetime as dt, timedelta
from starlette.middleware.base import BaseHTTPMiddleware
router = APIRouter()


def generate_date():
    now = dt.now()
    return now.strftime("%Y-%m-%d %H:%M")


def hash_password(password):
    h = hashlib.new("SHA256")
    h.update((password).encode())
    return h.hexdigest()


def generate_identity():
    return secrets.token_hex(10)


class NewUser(BaseModel):
    identity: str = Field(default_factory=generate_identity)
    firstname: str
    lastname: str
    email: str
    password: str
    role: str
    activated: bool = False
    created_at: str = Field(default_factory=generate_date)

    @classmethod
    @root_validator(pre=True)
    def set_created_at(cls, values):
        if "created_at" not in values:
            values["created_at"] = generate_date()
        return values

    @classmethod
    @root_validator(pre=True)
    def set_identity(cls, values):
        if "identity" not in values:
            values["identity"] = generate_identity()
        return values


def check_existence(user: NewUser) -> bool:
    item = student_collection.find_one({"email": user.email})
    return True if item else False


class LoginUser(BaseModel):
    email:  str
    password: str


class LoggedUser(BaseModel):
    identity: str
    firstname: str
    lastname: str
    email: str
    role: str
    activated: bool
    created_at: str


@router.get("/users")
async def read_users():
    return {"code": "code"}


@router.post("/students/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: NewUser):
    has_account = check_existence(user)
    if has_account:
        raise HTTPException(409, {"code": "409", "error": "User already exists",
                                  "message": "The user with the specified credentials already exists in the system."})
    else:
        hashed_password = hash_password(user.password)
        user.password = hashed_password
        x = student_collection.insert_one(user.dict())
        print(x.inserted_id)
        return {"code": 201, "message": f"successfully created an account for {user.email} "}


@router.post("/students/login", status_code=status.HTTP_200_OK)
async def login(user: LoginUser, response: Response):
    match(user.email, user.password):
        case("", ""):
            raise HTTPException(400, {"code": 400, "error": "Bad Request",
                                "message": "Please provide both email and password for login."})
    retrieved = student_collection.find_one({"email": user.email})
    claiming_hash = hash_password(user.password)
    match (retrieved):
        case (None):
            raise HTTPException(404, detail={"code": 404, "error": "Unauthorized",
                                "message": f"Log in failed because there was no account associated with {user.email}"})
    match(retrieved["email"] == user.email, claiming_hash == retrieved["password"]):
        case(True, False):
            raise HTTPException(401, detail={"code": 401, "error": "Unauthorized",
                                "message": "Incorrect password. Please try again."})
        case (True, True):
            inter = LoggedUser(**retrieved)
            generated_token = generate_token(user)
            print("generated token is", generated_token, " time is", time.time())
            response.set_cookie(key="jwt", value=generated_token,
                                httponly=True, max_age=300,  secure=True, samesite="strict")
            return {"code": 200, "message": "Successfull Login", "user": inter}

# expires=time.ctime(time.time()+300)

security = HTTPBearer()


@router.get("/students/details")
async def create_details(request: Request):
    print(request.headers.get("Authorization"))
    claimed_jwt = request.cookies["jwt"]
    print(claimed_jwt)
    sample = jwt.decode(claimed_jwt, key=secret_key,
                        algorithms=secret_algorithem)
    print(sample)
    # credentials: HTTPAuthorizationCredentials = Depends(security)
    # dependencies = [Depends(jwtBearer())]
    return {"hi": "route works"}


@router.get("/students/logout")
async def remove_cookie(reponse: Response):
    reponse.delete_cookie(key="jwt", path="/", httponly=True)
    return {"code": "200", "message": "successfully deleted jwt", "data": None}


@router.get("/students/test", dependencies=[Depends(authMiddleware)])
async def read_headers(request: Request, response: Response):
    print(request.url)
    return {"data": "some data"}

    # dependencies=[Depends(Intercept)]
    # return {"data": "some data"}
