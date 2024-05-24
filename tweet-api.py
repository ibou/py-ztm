import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='WUNTZm95LUNoMjlLcFZlZzJoZkZ0OHo0ZVpBX3ZnZmxxZGx2SVdRWXdNeFRROjE3MTY0NjAwNTE3NTk6MToxOmF0OjE'
# bearer_token = os.environ.get("BEARER_TOKEN")
bearer_token = "d2dtRDBlZlFuRU9naEVqbVJIS1l2eXltYlc0Q2NyQWNVcnRNcnBzUGk2V2ItOjE3MTY0NjU3NDM5MjY6MToxOmF0OjE"
base_url = "https://api.twitter.com/2"

print(bearer_token)

def get_users():
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=ibou888"
    user_fields = "user.fields=description,created_at"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "{}/users/by?{}&{}".format(base_url, usernames, user_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
  
  #  add params if exists
    # if params is not None:
    #   pass
    #   url = f"{url}?{params}"

    print(url)
    response = requests.get( 
        url,
        auth=bearer_oauth 
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_list_followers(users):
  
    for user in users:
        user_id = user['id']
        url = "{}/users/{}/followers".format(base_url, user_id)
        json_response = connect_to_endpoint(url) 
        print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    url = get_users()
    json_response = connect_to_endpoint(url) 
    print(json.dumps(json_response, indent=4, sort_keys=True))

    get_list_followers(json_response['data'])

    # print(json_response['data'])

if __name__ == "__main__":
    main()
