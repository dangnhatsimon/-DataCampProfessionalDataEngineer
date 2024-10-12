class Person:
    CURRENT_YEAR = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add a class method decorator
    @classmethod
    # Define the from_birth_year method
    def from_birth_year(cls, name, birth_year):
        # Create age
        age = Person.CURRENT_YEAR - birth_year
        # Return the name and age
        return cls(name, age)

bob = Person.from_birth_year("Bob", 1990)