import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers,
                         )

def post_new_client_kit(kit_body):
    create_user = post_new_user(data.user_body)
    auth_token = create_user.json()['authToken']
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers
                         )