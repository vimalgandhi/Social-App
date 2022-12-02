#Importing libraries
from fastapi import APIRouter, Request
from controllers.auth_controller import AuthController
from schemas.auth_models import LoginRequest , RegistrationRequest , ForgotPasswordModel , ResetPassword

# Declaring router
auth = APIRouter(tags=['Authentication'],  prefix="/api")

# Login API
@auth.post('/login')
def login(user: LoginRequest, request: Request):
    return AuthController.login(request=user)
# Registration API
@auth.post('/registration')
def registration(request: RegistrationRequest):
    return AuthController.registration(request=request)

@auth.post('/forget-password')
def forgot_password(request: ForgotPasswordModel):
    return AuthController.forgot_password(request)

@auth.post('/password/reset')
def reset_password(request:ResetPassword):
    return AuthController.reset_password(request)