class User:

    def __init__(self, user_json=None):
        self.uid = user_json["uid"]
        self.username = user_json["username"]
        self.date_of_birth = user_json["date_of_birth"]

    def __repr__(self):
        return self.username

