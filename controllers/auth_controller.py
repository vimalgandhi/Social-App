# Importing libraries
from helper.api_helper import APIHelper
from schemas.auth_models import LoginRequest, RegistrationRequest, ForgotPasswordModel,  ResetPassword
from config.db_config import db
from helper.hashing import Hashing
from fastapi import BackgroundTasks
from models.user_table import user_table
from helper.token_helper import TokenHelper
from helper.api_helper import APIHelper
from helper.common_helper import CommonHelper
from models.password_resets import password_resets_table


class AuthController:
    # Login api implementation
    def login(request: LoginRequest):
        user = db.execute(user_table.select(whereclause=(
            user_table.c.email == request.email.lower()))).fetchone()
        if user:
            if not Hashing.verify(request.password, user.password):
                return APIHelper.send_error_response(errorMessageKey="invalid_credentials")
            else:
                access_token = TokenHelper.create_access_token(
                    data={"sub": request.email})
                data = db.execute(user_table.select(
                    whereclause=user_table.c.email == request.email)).fetchone()
                return {"jwt_token": access_token, "id": data.id, "email": request.email, "username": data.username}
        else:
            return APIHelper.send_error_response(errorMessageKey="invalid_credentials")

     # Registration Api implementation
    def registration(request: RegistrationRequest):
        user = db.execute(user_table.select(whereclause=(
            user_table.c.email == request.email))).fetchone()
        if not user:
            db.execute(user_table.insert().values(email=request.email.lower(
            ), password=Hashing.get_hash(request.password), username=request.username))
            access_token = TokenHelper.create_access_token(
                data={"sub": request.email})
            data = db.execute(user_table.select(
                whereclause=user_table.c.email == request.email)).fetchone()
            return {"jwt_token": access_token, "id": data.id, "email": data.email, "userName": data.username}
        return "Email Alredy existed"

    def forgot_password(request: ForgotPasswordModel):
        user = db.execute(user_table.select(
            user_table.c.email == request.email.lower())).fetchone()
        if user:
            token = CommonHelper.random_string(length=6)
            db.execute(password_resets_table.insert().values(
                token=token, email=user.email))
            return token
        else:
            return APIHelper.send_error_response(errorMessageKey="translations.USER_NOT_FOUND")

    def reset_password(request: ResetPassword):
        print(request.token)
        user = db.execute(password_resets_table.select(whereclause=(password_resets_table.c.email == request.email))).fetchone()
        if user:
            if request.token == user.token:
                db.execute(user_table.update(values={"password": Hashing.get_hash(request.password)}, whereclause=(user_table.c.email == user.email)))
                db.execute(password_resets_table.delete(whereclause=(password_resets_table.c.email == user.email)))
                return APIHelper.send_error_response(errorMessageKey="translations.PASSWORD_SUCCESS")
            else:
                return APIHelper.send_error_response(errorMessageKey="translations.TOKEN_NOT_AVAIABLE")
        else:
            return APIHelper.send_error_response(errorMessageKey="translations.USER_NOT_FOUND")