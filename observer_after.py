from api.users import register_new_user, password_forgetten
from api.plan import upgrade_plan
from .api_v2.email_listener import setup_email_event_handlers
from api_v2.log_listener import setup_log_event_handlers
from api_v2.slack_listener import setup_slack_event_handlers

setup_slack_event_handlers()
setup_email_event_handlers()
setup_log_event_handlers

# register a new user
register_new_user("Turgay", "turgay123", "turgay@connexease.com")

# send a password reset message
password_forgetten("turgay@connexease.com")

# upgrade the plan
upgrade_plan("turgay@connexease.com")
