from collections import UserString

class MyString(UserString):
    def append(self, s):
        self.data += s

    def remove(self, s):
        self.data = self.data.replace(s, '')
        
    def add(self,s):
        self.data = s

my_string = MyString("Hello")
my_string.append(" World")
print(my_string)  # Output: Hello World
my_string.remove(" World")
print(my_string)  # Output: Hello
my_string.add(" World")
print(my_string)  # Output: Hello
