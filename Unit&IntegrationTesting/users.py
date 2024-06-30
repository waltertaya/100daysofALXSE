class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.logged_in = False

    def login(self):
        self.logged_in = True

    def logout(self):
        self.logged_in = False

    def update_email(self, new_email):
        if '@' in new_email and '.' in new_email:
            self.email = new_email
        else:
            raise ValueError("Invalid email address")
        
    # @property at the top of the method symbolises the method is non-public

    def __str__(self):
        return f"User({self.user_id}, {self.username}, {self.email}, logged_in={self.logged_in})"
