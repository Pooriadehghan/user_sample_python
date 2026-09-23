class User:
    def __init__(self, user_id,name, family, national_id,
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
        pass

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        pass
    
    @property
    def national_id(self):
        return self._national_id
    
    @national_id.setter
    def national_id(self, value):
        pass

    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        pass


    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        pass

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        pass

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        pass

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        pass

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        pass

    def __repr__(self):
        return (f"User(user_id= {self.user_id}, name= {self.name},family={self.family}\n,"
                f"national_id={self.national_id},birth_date={self.birth_date}\n"
                f",phone_number={self.phone_number},\n"
                f"username={self.username},password={self.password},\n"
                f"locked={self.locked},role={self.role}) )")

