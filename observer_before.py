from api.users import register_new_user, password_forgetten
from api.plan import upgrade_plan

# register a new user
register_new_user("Turgay", "turgay123", "turgay@connexease.com")

# send a password reset message
password_forgetten("turgay@connexease.com")

# upgrade the plan
upgrade_plan("turgay@connexease.com")
