from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions.db import db
from app.models import User

"""
USER SERVICE
============
All USER related business logic lives here

मराठीत:
----------
User create करणे,
password hash करणे,
password verify करणे
हे सगळं service मध्ये असतं
"""

def create_user(email: str, password: str) -> User:
    """
    CREATE USER WITH HASHED PASSWORD

    WHY THIS FUNCTION?
    ------------------
    Route मध्ये password hash logic ठेवायचा नाही
    ते messy होतं

    मराठीत:
    ----------
    Password plain text मध्ये
    database मध्ये ठेवणं चुकीचं आहे
    म्हणून hash करतो
    """

    # 🔐 Hash password (ONE-WAY)
    hashed_password = generate_password_hash(password)

    # Create User object
    user = User(
        email=email,
        password_hash=hashed_password
    )

    # Save to database
    db.session.add(user)
    db.session.commit()

    return user


def verify_password(user: User, password: str) -> bool:
    """
    VERIFY PASSWORD DURING LOGIN

    WHY SEPARATE FUNCTION?
    ----------------------
    Login logic reuse करता यावी म्हणून

    मराठीत:
    ----------
    Login वेळी password
    hash compare केला जातो
    """

    return check_password_hash(user.password_hash, password)
