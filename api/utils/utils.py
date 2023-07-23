from passlib.context import CryptContext
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

def is_valid_email(email: str) -> bool:
    # Use regular expression to check if the email is valid
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)

def is_valid_password(password: str) -> bool:
    # Check if the password has at least 12 characters, contains numbers, and special characters
    return len(password) >= 12 and any(char.isdigit() for char in password) and any(char.isalnum() for char in password)
