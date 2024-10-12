class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return True


class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return True