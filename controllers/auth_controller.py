# Importing libraries
from helper.api_helper import APIHelper
from schemas.auth_models import LoginRequest, RegistrationRequest
from config.db_config import db
from helper.hashing import Hash
from models.user_table import user_table
from helper.token_helper import TokenHelper
from helper.api_helper import APIHelper


class AuthController:
    # Login api implementation
    def login(request: LoginRequest):
        user = db.execute(user_table.select(whereclause=(
            user_table.c.email == request.email.lower()))).fetchone()
        if user:
            if not Hash.verify(request.password, user.password):
                return APIHelper.send_error_response(errorMessageKey="invalid_credentials")
            else:
                access_token = TokenHelper.create_access_token(data={"sub": request.email})
                data = db.execute(user_table.select(whereclause=user_table.c.email == request.email)).fetchone()
                return {"jwt_token": access_token , "id": data.id ,"email": request.email ,"username": data.username }
        else:
            return APIHelper.send_error_response(errorMessageKey="invalid_credentials")

     # Registration Api implementation
    def registration(request: RegistrationRequest):
        print(request)
        user = db.execute(user_table.select(whereclause=(user_table.c.email == request.email))).fetchone()
        if not user:
            db.execute(user_table.insert().values(email=request.email.lower(), password=Hash.get_hash(request.password), username=request.username))
            access_token = TokenHelper.create_access_token(data={"sub": request.email})
            data = db.execute(user_table.select(whereclause=user_table.c.email == request.email)).fetchone()
            return {"jwt_token": access_token,"id": data.id ,"email": data.email ,"userName": data.username }
        return "Email Alredy existed"