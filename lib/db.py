from hashlib import blake2b

"""fake 'database' of users"""

users = []


class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = blake2b(password.encode('UTF-8')).hexdigest()
        self.email = email
        self.plan = "basic plan"
        self.reset_code = ""

    def __repr__(self):
        return f"Name: {self.name}, E-mail: {self.email}, Password: {self.password}"

    def reset_password(self, code, new_password):
        if self.reset_code != code:
            raise Exception("Invalid password reset code")
        self.password = blake2b(new_password.encode('UTF-8')).hexdigest()


"""stub methods for actions related to creating new user"""
def create_user(name, password, email):
    print(f"DB: Creating user database entry for {name} - ({email})")
    new_user = User(name, password, email)
    users.append(new_user)
    return new_user

def find_user(email):
    for user in users:
        if user.email == email:
            return user
        
    raise Exception (f"User with email address {email} not found")
