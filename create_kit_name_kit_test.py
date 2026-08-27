import sender_stand_request
import data


def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]


def get_kit_body(name):
    body = data.kit_body.copy()
    body["name"] = name
    return body


def positive_assert(name):
    token = get_new_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == name


def negative_assert_code_400(name):
    token = get_new_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400


def test_1_min_length_allowed():
    positive_assert("a")

def test_2_max_length_allowed():
    positive_assert("a" * 511)

def test_3_zero_length_rejected():
    negative_assert_code_400("")

def test_4_over_max_length_rejected():
    negative_assert_code_400("a" * 512)

def test_5_special_characters_allowed():
    positive_assert('"№%@",')

def test_6_spaces_allowed():
    positive_assert(" A Aaa ")

def test_7_numbers_as_string_allowed():
    positive_assert("123")

def test_8_no_name_param_rejected():
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit({}, token)
    assert response.status_code == 400

def test_9_number_type_rejected():
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit({"name": 123}, token)
    assert response.status_code == 400