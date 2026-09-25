from datetime import datetime

from user import User
from user_service import UserService


class UserController:
    def __init__(self):
        self.__service = UserService()

    def save(self, user_id, name, family, national_id,
             birth_date, phone_number, username,
             password, locked, role):
        try:
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
            user = User(user_id, name, family, national_id, birth_date, phone_number, username,
                        password, locked, role)

            self.__service.save(user)
            return True, f"Info:{user} Saved"
        except Exception as e:
            return False, f"Error:{e}"

    def edit(self, user_id, name, family, national_id,
             birth_date, phone_number, username,
             password, locked, role):
        try:
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
            user = User(user_id, name, family, national_id, birth_date, phone_number, username,
                        password, locked, role)

            self.__service.edit(user)
            return True, f"Info:{user} Edited"
        except Exception as e:
            return False, f"Error:{e}"

    def delete(self, user_id):
        try:

            self.__service.delete(user_id)
            return True, f"Info:{user_id} Deleted"
        except Exception as e:
            return False, f"Error:{e}"

    def get_all(self):
        try:
            users = self.__service.get_all()
            return True, users
        except Exception as e:
            return False, f"Error:{e}"

    def get_by_name(self, name):
        try:
            users = self.__service.get_by_name(name)
            return True, users
        except Exception as e:
            return False, f"Error:{e}"
