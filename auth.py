import gmail
import json

def get_creds(configFile):
    with open(configFile) as json_data_file:
        data = json.load(json_data_file)
    username = data["users"]["user1"]["username"]
    password = data["users"]["user1"]["password"]
    access_token = data["users"]["user1"]["access_token"]

    return username, password, access_token

def token():
    username, password, access_token = get_creds("./config.json")
    print username, access_token
    session = gmail.authenticate(username, access_token)

    return session, username

def password():
    username, password, access_token = get_creds("./config.json")
    session = gmail.login(username, password)
    # print g.logged_in  # Should be True, AuthenticationError if login fails
    return session, username