class Base:
    def __init__(self):
        self.grade = 10
        self.name = 'ABC'


class BaseMixIn:
    def __init__(self):
        self.grade = 100
        self.name = 'QWE'


class Student(BaseMixIn, Base):
    def __init__(self):
        super().__init__()
        print(self.name, self.grade)


s = Student()