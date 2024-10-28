from abc_classes import ABot
from teams_classes import NewUser, NewPost

from datetime import datetime


def get_time_now():
    dt = datetime.utcnow()
    iso_format = dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    return iso_format


class Bot(ABot):
    def create_user(self, session_info):
        # todo logic
        # Example:
        new_users = [
            NewUser(username="GradTestBot1", name="gradbot1", description="This is a gradbot1."),
            NewUser(username="GradTestBot2", name="gradbot2", description="This is a gradbot2."),
        ]
        return new_users

    def generate_content(self, datasets_json, users_list):
        # todo logic
        # It needs to return json with the users and their description and the posts to be inserted.
        # Example:

        posts = []
        n_tweets = 6
        for i in range(n_tweets):
            for j in range(len(users_list)):
                posts.append(NewPost(text=f'{i}: Gradbots are working!', author_id=users_list[j].user_id, created_at=get_time_now(),user=users_list[j]))
        return posts
