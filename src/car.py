class Car(object):
    """
    This is class which represents details of a car.
   
    reg_no = Car Registration Number
    age = Age of Driver 

    """

    def __init__(self):
        self._reg_no = None
        self._age = None

    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @classmethod
    def create(cls, reg_no, age):
        car_obj = cls()
        car_obj.reg_no = reg_no
        car_obj.age = age
        return car_obj
