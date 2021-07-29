from lib.email import send_email
from lib.log import log
from lib.db import create_user, find_user
from lib.slack import post_slack_message

def upgrade_plan(email):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    # post a slack message to sales departmen
    post_slack_message("Sales", f"user with email address {user.name} has upgraded their plan")

    # send a thank you email
    send_email(user.name, user.email, "Thank you for upgrading your plan",
    f"Hi {user.name}\n Thank to upgrade your plan!")

    log(f"User with email address {user.email}, has upgraded their plan")