from datetime import date

from user_controller import UserController
from user import User
from user_data_manager import UserDataAccess
from user_service import UserService

# user test -PASSED

user1 = User("1", "pooria", "dehghan",
             "0441012365", date(2002, 4, 8),
             "09127040100", "pooria_dhn",
             "123456789", True, "employee")
user2 = User("2", "ali", "amiri",
             "0441012256", date(2004, 6, 8),
             "09356040100", "ali_a12",
             "987456321", False, "user")
#
# print(user1)
# print("-" * 50)
# print(user2)

# user data access object -PASSED
# user_da=UserDataAccess()
# user_da.save_user(user1)
# user_da.save_user(user2)
#
# print(user_da.get_all_user())


# user business logic - PASSED

# service=UserService()
# service.save(user1)
# service.save(user2)
#
# print(service.get_all())


# user controller - PASSED

# controller=UserController()
# controller.save("1", "pooria", "dehghan",
#              "0441012365", date(2002,4,8),
#              "09127040100", "pooria_dhn",
#              "123456789", True, "employee")
# controller.save("2", "ali", "amiri",
#              "0441012256", date(2004,6,8),
#              "09356040100", "ali_a12",
#              "987456321", False, "user")
#
#
# print(controller.get_all())
