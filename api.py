import requests
import json

# from settings import valid_email, valid_password
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):
        """Получает и выводит ключ api"""

        headers = {
            'email': email,
            'password': password,
        }
        response = requests.get(self.base_url + "api/key", headers=headers,)
        response_status = response.status_code
        # result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        return response_status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {"auth_key": auth_key['key']}
        filter = {"filter": filter}

        response = requests.get(self.base_url + "api/pets", headers=headers, params=filter)
        response_status = response.status_code

        # result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        return response_status, result

    def post_information_about_new_pet(self, auth_key, name, animal_type, age, pet_photo, ):
        form_data = MultipartEncoder(
            fields={
                "name": name,
                "animal_type": animal_type,
                "age": age,
                "pet_photo": (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {"auth_key": auth_key['key'],
                   "Content-Type": form_data.content_type
                   }
        response = requests.post(self.base_url + "api/pets", headers=headers, data=form_data)
        response_status = response.status_code

        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        print(result)
        return response_status, result

    def update_pet_info(self, auth_key, pet_id, name, animal_type, age):
        data = MultipartEncoder(
            fields={
                "name": name,
                "animal_type": animal_type,
                "age": age
            }
        )
        headers = {"auth_key": auth_key["key"],
                   "Content-Type": data.content_type
                   }

        response = requests.put(self.base_url + "api/pets/" + pet_id, headers=headers, data=data)
        response_status = response.status_code

        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        print(result)
        return response_status, result


# работает, проверка
# PetFriends.update_pet_info(self=PetFriends(),
#                            auth_key={"key": "b37ae8f1ae05dd6b6f19e15bf8cbf8f9d59ca065f9d0e7673613dd3c"},
#                            pet_id="15680215-9930-4c71-9f3d-352e524cc45e",
#                            name="asd",
#                            animal_type="m",
#                            age="10")






# # filter = " "
# auth_key = {'key': 'b37ae8f1ae05dd6b6f19e15bf8cbf8f9d59ca065f9d0e7673613dd3c'}
# pr = PetFriends()
# print(pr.get_api_key(valid_email, valid_password))
# # print(pr.get_list_of_pets(auth_key, filter))