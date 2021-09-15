class Post:
    def __init__(self, msg, auth):
        self.message = msg
        self.author = auth

    def get_post_info(self):
        print(f"Hey, {self.author} left a post: {self.message}.")
