'''
Sometimes you have an object that is so complicated
that you need multiple builders to do it.

Here lets have two builders:
1. Employment builder
2. Address Builder

For both of these builders we have a third builder
called PersonBuilder
'''
class Person:

    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None
    
    def __str__(self):
        return ( 
            'Address {}, PostCode: {}, City: {},'
            'Company: {}, Position: {}, Annual Salary: {}'
        ).format(
            self.street_address, self.postcode,
            self.city, self.company_name, self.position,
            self.annual_income
        )

    @staticmethod
    def create():
        return PersonBuilder()


class PersonBuilder:

    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def __str__(self):
        return str(self.person)


class PersonJobBuilder(PersonBuilder):

    def __init__(self, person):
        super().__init__(person)
    
    def at(self, company_name):
        self.person.company_name = company_name
        return self
    
    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):

    def __init__(self, person):
        self.person = person
    
    def at(self, street_address):
        self.person.street_address = street_address
        return self
    
    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self
    
    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == "__main__":
    person = Person.create()
    person.lives.at('BTM 2nd stage').in_city('Bangalore')\
                .with_postcode('537008')\
            .works.at('Biofourmis').as_a('Software Engineer')\
                .earning('10LPA')
    print(person)