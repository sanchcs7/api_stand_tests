import sender_stand_request
import data
def get_user_body(first_name):
   current_body = data.user_body.copy()
   current_body["firstName"] = first_name
   return current_body
def test_create_user_valid_name():
    response = sender_stand_request.post_new_user(get_user_body("Andrea"))
    assert response.status_code == 201

def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)
    print(user_response.status_code)
    print(user_response.json())
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

def test_create_user_15_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = (
        user_body["firstName"] + "," +
        user_body["phone"] + "," +
        user_body["address"] + ",,," +
        user_response.json()["authToken"]
    )
    assert users_table_response.text.count(str_user) == 1
def test_create_user_1_letter_in_first_name_get_error_response():
    user_body = get_user_body("A")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
def test_create_user_16_letter_in_first_name_get_error_response():
    user_body = get_user_body("Aaaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
def test_create_user_first_name_with_space_get_error_response():
    user_body = get_user_body("A Aaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
def test_create_user_first_name_with_special_chars_get_error_response():
    user_body = get_user_body("№%@")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
def test_create_user_first_name_with_numbers_get_error_response():
    user_body = get_user_body("123")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"
def test_create_user_without_first_name_get_error_response():
    user_body = {
        "phone": "+1234567890",
        "address": "123 Elm Street, Hilltop"
    }
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "No se enviaron todos los parámetros requeridos"
def test_create_user_empty_first_name_get_error_response():
    user_body = {
        "firstName": "",
        "phone": "+1234567890",
        "address": "123 Elm Street, Hilltop"
    }
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "No se enviaron todos los parámetros requeridos"


def test_create_user_first_name_as_number_get_error_response():
    user_body = {
        "firstName": 12,  # Valor numérico intencional
        "phone": "+1234567890",
        "address": "123 Elm Street, Hilltop"
    }
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"

