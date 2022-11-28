#Importing libraries
from fastapi import APIRouter, Request
from controllers.user_controller import UserController
from schemas.user_schamas import check_user

# Declaring router
user = APIRouter(tags=['user'] , prefix="/api")

# check userName API
@user.post('/check_username')
def check_username(request: check_user):
    return UserController.check_username(request)


