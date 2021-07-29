from lib.db import find_user
from .event import post_event

def upgrade_plan(email):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    post_event("user_upgrade_plan", user)
