from passlib.context import CryptContext


class Hashing:
    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # Return Hashed Password
    def get_hash(text):
        return Hashing._pwd_context.hash(text)

    # Verfiy Hashed Password
    def verify(plain_text, hashed_text):
        return Hashing._pwd_context.verify(plain_text, hashed_text)
