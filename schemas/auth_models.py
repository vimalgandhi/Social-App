from typing import Optional
from pydantic import BaseModel, validator
from helper.validation_helper import ValidationHelper


class LoginRequest(BaseModel):
    email: str
    password: str

class RegistrationRequest(BaseModel):
    email : str
    password: str
    username : str
    _email = validator("email", allow_reuse=True)(ValidationHelper.is_email)
    _password = validator("password", allow_reuse=True)(ValidationHelper.is_valid_password)

class ForgotPasswordModel(BaseModel):
    email: str
    # _email = validator("email", allow_reuse=True)(ValidationHelper.is_email)

class ResetPassword(BaseModel):
    email: str
    password: str
    token: str
    _email = validator("email", allow_reuse=True)(ValidationHelper.is_email)
    _password = validator("password", allow_reuse=True)(ValidationHelper.is_valid_password)