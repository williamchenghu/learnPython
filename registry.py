from user import User
from post import Post

user_one = User("Tom", "tom@tom.com", "strong_password", "Frontend Developer")
user_one.get_user_info()

user_two = User("Bob", "bob@bob.com", "top_secret", "Backend Developer")
user_two.get_user_info()

user_post = Post("I'm tired of dealing with graphic elements!", user_one.name)
user_post.get_post_info()
