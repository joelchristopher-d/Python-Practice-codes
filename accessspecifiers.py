# Python
class Animal:
    def __private_method(self):
        print("Private method in Animal")

    def _protected_method(self):
        print("Protected method in Animal")

    def public_method(self):
        print("Public method in Animal")

class Dog(Animal):
    def bark(self):
        self._protected_method()  # Works fine

        # Attempting to access a private method (name-mangled)
        try:
            self.__private_method()  # This will raise an AttributeError
        except AttributeError:
            print("Cannot access private method")

dog = Dog()
dog.bark()
