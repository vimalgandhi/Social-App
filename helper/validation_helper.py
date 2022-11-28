import re
import i18n
from config.constants import Constants

class ValidationHelper:
    def is_mobile(cls, v):
        if not re.fullmatch(Constants.NUMBER_REGEX, v):
            raise ValueError(
                i18n.t(key='translations.INVALID_MOBILE'))
        return v

    def is_valid_password(cls, v):
        if not re.fullmatch(Constants.PASSWORD_REGEX, v):
            raise ValueError(
                i18n.t(key='translations.INVALID_PASSWORD'))
        return v

    def is_email(cls, v):
        if not re.fullmatch(Constants.EMAIL_REGEX, v):
            raise ValueError(
                i18n.t(key='translations.INVALID_EMAIL'))
        return v

    def is_valid_lang(cls, v):
        if not re.fullmatch(Constants.LANG_REGEX, v):
            raise ValueError(
                i18n.t(key='translations.INVALID_LANG'))
        return v

    def is_valid_comment_type(cls, v):
        if not re.fullmatch(Constants.COMMENT_TYPE, v):
            raise ValueError(
                i18n.t(key='translations.INVALID_COMMENT_TYPE'))
        return v
