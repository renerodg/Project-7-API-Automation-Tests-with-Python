import copy
import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def post_new_client_kit(kit_body, auth_token):
    kit_body_copy = copy.deepcopy(kit_body)

    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body_copy,
                             headers=headers)

    return response


user_response = post_new_user(data.user_body)
auth_token = user_response.json().get('authToken')

kit_response = post_new_client_kit(data.kit_body, auth_token)
print(kit_response.status_code)
print(kit_response.json())