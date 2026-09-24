from user_data_manager import UserDataAccess


class UserService:
    def __init__(self):
        self.__data_access = UserDataAccess()

    def save(self, user):
        # todo: کد ملی/شماره تلفن ==>unique
        # todo: اگر کارمند بود سنش باید بین 20-40 باشه
        print("شروط تایید شد")
        self.__data_access.save_user(user)

    def edit(self, user):
        # todo: کد ملی/شماره تلفن ==>unique
        # todo: اگر کارمند بود سنش باید بین 20-40 باشه
        print("شروط تایید شد")
        self.__data_access.edit_user(user)

    def delete(self, user_id):
        self.__data_access.delete_user(user_id)

    def get_all(self):
        return self.__data_access.get_all_user()

    def get_by_name(self, name):
        return self.__data_access.get_user_by_name(name)
