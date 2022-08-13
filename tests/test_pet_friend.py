import os
from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    response_status, result = pf.get_api_key(email, password)
    assert response_status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=""):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result["pets"]) > 0


def test_post_new_pet_with_valid_key(name="Leo", animal_type="cat", age='10', pet_photo="image/Leo.jpg",):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_information_about_new_pet(auth_key, name, animal_type, age, pet_photo,)

    assert status == 200
    assert result["age"] == age


def test_put_update_pet_information_valid_key(name='sad dogg', animal_type='m', age='9', ):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age, )
    assert status == 200
    assert result['name'] == name
    assert result['age'] == age


