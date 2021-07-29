from lib.email import send_email
from .event import subscribe

def handle_user_registered_event(user):
    send_email(user.name, user.email, "Welcome",
    "Thanks for registering, {user.name}!\nRegards")

def handle_user_password_forgetten_event(user):
    send_email(user.name, user.email, "Reset your password", 
    f"To reset your password you can use this code: {user.reset_code}.")

def handle_user_upgrade_plan_event(user):
    send_email(user.name, user.email, "Thank you for upgrading your plan",
    f"Hi {user.name}\n Thank to upgrade your plan!")

def setup_email_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgetten", handle_user_password_forgetten_event)
    subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
