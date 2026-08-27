import requests
import configuration


def post_new_user(user_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=user_body,
        headers=configuration.HEADERS
    )


def post_new_client_kit(kit_body, auth_token):
    headers = configuration.HEADERS.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )