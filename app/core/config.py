from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "CHANGE_THIS_TO_A_LONG_RANDOM_SECRET_KEY"
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60