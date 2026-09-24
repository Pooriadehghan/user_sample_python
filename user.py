from curses.ascii import isdigit
from datetime import date
from utils import *


class User:
    def __init__(self, user_id, name, family, national_id,
                 birth_date, phone_number, username,
                 password, locked, role):
        self.user_id = None
        self.name = name
        self.family = family
        self.national_id = national_id
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.locked = locked
        self.role = role

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Invalid!!! name must be a string")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        if isinstance(value, str):
            self._family = value
        else:
            raise ValueError("Invalid!!! family must be a string")

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid!!! national_id must be exactly 10 digits")
        self._national_id = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        if not isinstance(value, date):
            raise ValueError("Invalid!!! birth_date must be a date")

        # todo:برای کارمند بودن شرط بین 20-40 سال در منطق تجاری داریم که در ادامه باید اضافه شود

        self._birth_date = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = phone_validator(value, "Invalid phone number!!!")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid!!! username must be a string")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid!!! password must be a string")
        self._password = value

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        if not isinstance(value, bool):
            raise ValueError("Invalid!!! locked must be a boolean (TRUE or FALSE)")
        self._locked = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid!!! role must be a string")
        self._role = value

    def __repr__(self):
        return (f"User(user_id= {self.user_id}, name= {self.name},family={self.family}\n,"
                f"national_id={self.national_id},birth_date={self.birth_date}\n"
                f",phone_number={self.phone_number},\n"
                f"username={self.username},password={self.password},\n"
                f"locked={self.locked},role={self.role}) )")
