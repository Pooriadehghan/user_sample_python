class UserDataAccess:
    def __init__(self):
        self.__user_list = []

    def save_user(self, user):
        self.__user_list.append(user)

    def edit_user(self, user):
        print("EDIT:", user)

    def delete_user(self, user_id):
        print("DELETE:", user_id)

    def get_all_user(self):
        return self.__user_list.copy()

    def get_user_by_name(self, name):
        print("GET By Name:", name)
