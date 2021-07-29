from lib.email import send_email
from lib.db import create_user, find_user
from lib.log import log
from lib.slack import post_slack_message
from lib.stringtools import get_random_string

def register_new_user(name, password, email):
    #Create a new user in the db
    user = create_user(name, password, email)

    # post a slack mesage to the sales department
    post_slack_message("Sales", 
    f"{user.name} has registered with email address {user.email}")

    # send a welcome email for new users
    send_email(user.name, user.email, "Welcome",
    "Thanks for registering, {user.name}!\nRegards")

    # write server log
    log(f"User registered with email address {user.email}") 

def password_forgetten(email):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(16)

    # send a password reset message
    send_email(user.name, user.email, "Reset your password", 
    f"To reset your password you can use this code: {user.reset_code}.")

    # write server log
    log(f"User with email address {user.email} requested a password reset code") 
