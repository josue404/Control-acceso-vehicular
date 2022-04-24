# T00062598 - Josue Fadul Mejia - Maycol Casadiegos - T00061889


class Vehicular(object):

    def __init__(self, user_register: str, user_unregister: str, vehicular: str, category: str, control: int):
        self.user_register = user_register
        self.user_unregister = user_unregister
        self.vehicular = vehicular
        self.category = category
        self.control = control

    # methods
    @property
    def user_register(self) -> str:
        return self.user_register

    @user_register.setter
    def user_register(self, user_register: str):
        self.user_register = user_register

    @property
    def user_unregister(self) -> str:
        return self.user_unregister

    @user_unregister.setter
    def user_unregister(self, user_unregister: str):
        self.user_unregister = user_unregister

    @property
    def vehicular(self) -> str:
        return self.vehicular

    @vehicular.setter
    def vehicular(self, vehicular: str):
        self._no_pages = vehicular

    @property
    def category(self) -> str:
        return self.category

    @category.setter
    def category(self, category: str):
        self._category = category

    @property
    def control(self) -> int:
        return self.control

    @control.setter
    def control(self, control: str):
        self._control = control

    def __str__(self):
        """ Returns str of vehicular.
          :returns: sting vehicular
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self.user_register, self.user_unregister, self.vehicular, self.category,
                                                       self.control)

    def see_vehicular(self):
        print("\nUsuario: " + str(
            self.user_register) + "\nTipo de persona: " + self.user_unregister + "\nCategory:" + self.category + "\nTipo de vehiculo: " + self.vehicular + "\nFoto: " + str(
            self.control))


if __name__ == '__main__':
    _user_register = str(input("Insert the Username: "))
    _user_unregister = str(input("Write role: "))
    _category = str(input("Write the car status: "))
    _vehicular = str(input("Write the type of car: "))
    _control = int(input("Insert Photo:"))

    J = Vehicular(user_register=_user_register, user_unregister=_user_unregister, vehicular=_vehicular, category=_category, control=_control)
    print(J)
