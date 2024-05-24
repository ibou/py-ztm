# faire des request sur api twitter avec credentials

import tweepy
bearer_token = "WUNTZm95LUNoMjlLcFZlZzJoZkZ0OHo0ZVpBX3ZnZmxxZGx2SVdRWXdNeFRROjE3MTY0NjAwNTE3NTk6MToxOmF0OjE"
client = tweepy.Client(bearer_token)

# Exemple de requête pour obtenir les informations d'un utilisateur par son nom d'utilisateur
def get_user_info(username):
    user_info = client.get_user(username=username)
    return user_info

# Exemple de requête pour obtenir les tweets d'un utilisateur par son ID
def get_user_tweets(user_id):
    response = client.get_users_tweets(id=user_id)
    return response

def get_user_followers(user_id):
    response = client.get_users_followers(id=user_id)
    return response
# run queries avec les endpoints twitter V2


# Exemple d'utilisation des fonctions
if __name__ == "__main__":
    username = "ibou888"
    user_info = get_user_info(username)
    print(user_info)

    user_id = 559766000
    tweets = get_user_tweets(user_id)
    for tweet in tweets.data:
        print(tweet.id, tweet.text)

    followers = get_user_followers(user_id)
    print(followers)

