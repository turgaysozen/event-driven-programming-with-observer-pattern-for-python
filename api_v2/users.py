from lib.db import create_user, find_user
from lib.stringtools import get_random_string
from .event import post_event

def register_new_user(name, password, email):
    #Create a new user in the db
    user = create_user(name, password, email)

    post_event("user_registered", user)

def password_forgetten(email):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(16)

    post_event("user password forgetten", user) 
