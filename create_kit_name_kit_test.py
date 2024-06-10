import pytest
import data
import sender_stand_request

def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    response_body = response.json()
    assert response_body['name'] == kit_body['name']

def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

@pytest.fixture
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    assert user_response.status_code == 201
    return user_response.json().get('authToken')

# 1. Prueba para el número permitido de caracteres (1)
def test_kit_name_with_1_character(get_new_user_token):
    kit_body = data.get_kit_body("a")
    positive_assert(kit_body, get_new_user_token)


# 2. Prueba para el número permitido de caracteres (511)
def test_kit_name_with_511_character(get_new_user_token):
    long_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    kit_body = data.get_kit_body(long_name)
    positive_assert(kit_body, get_new_user_token)


# 3. Prueba el numero de caracteres es menor a la cantidad permitida (0)
def test_kit_name_with_0_character(get_new_user_token):
    kit_body = data.get_kit_body("")
    negative_assert_code_400(kit_body, get_new_user_token)


# 4. Prueba el numero de caracteres es mayor que la permitida (512)
def test_kit_name_with_512_character(get_new_user_token):
    kit_body = data.get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body, get_new_user_token)


# 5. Prueba se permiten caracteres especiales ($%^&*)
def test_kit_name_with_special_character(get_new_user_token):
    kit_body = data.get_kit_body("№%@")
    positive_assert(kit_body, get_new_user_token)


# 6. Prueba se permiten espacios ( A Aaa )
def test_kit_name_with_blank_character(get_new_user_token):
    kit_body = data.get_kit_body(" A Aaa ")
    positive_assert(kit_body, get_new_user_token)


# 7. Prueba se permiten numeros (123)
def test_kit_name_with_number_character(get_new_user_token):
    kit_body = data.get_kit_body("123")
    positive_assert(kit_body, get_new_user_token)


# 8. Prueba el parametro no se pasa en la solicitud ()
def test_kit_name_with_nothing_character(get_new_user_token):
    kit_body = data.get_kit_body()
    negative_assert_code_400(kit_body, get_new_user_token)


# 9. Prueba tipo de parametro diferente (123)
def test_kit_name_with_different_character(get_new_user_token):
    kit_body = data.get_kit_body(123)
    negative_assert_code_400(kit_body, get_new_user_token)