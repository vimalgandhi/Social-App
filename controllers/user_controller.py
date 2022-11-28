# Importing libraries
from helper.api_helper import APIHelper
from config.db_config import db
from helper.hashing import Hash
from helper.token_helper import TokenHelper
from helper.api_helper import APIHelper
from models.user_table import user_table
from schemas.user_schamas import check_user


class UserController:
    def check_username(request: check_user):
        data = db.execute(user_table.select(
            whereclause=user_table.c.username == request.username)).fetchone()
        if not data:
            return APIHelper.send_success_response(data="translations.AVAILABLE_USERNAME")
        return APIHelper.send_error_response(errorMessageKey="translations.ALREDY_USERNAME")
