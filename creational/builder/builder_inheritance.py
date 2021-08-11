'''
The idea of combining builders violated the Open Close Principle
Every time we added a builder we would have to add that as a property
On the main builder.
'''

class Person:

    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name}, {self.position}, {self.date_of_birth}'
    
    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:

    def __init__(self):
        self.person = Person()
    
    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):

    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):

    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthBuilder(PersonJobBuilder):

    def born(self, dob):
        self.person.date_of_birth = dob
        return self


'''
As we have inherited one class over the other.
The final builder will have all the methods.
So we can use the final builder class to do things.
'''


if __name__ == "__main__":
    person = PersonBirthBuilder()
    me = person.called(
            'Namah'
        ).born(
            '09/07/1995'
        ).works_as_a('Software Engineer').build()
    print(me)