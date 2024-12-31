from collections import UserList

class MyList(UserList):
    def append(self, item):
        if not isinstance(item, int):
            raise TypeError("Only integers are allowed")
        super().append(item)

my_list = MyList([1, 2, 3])
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
# my_list.append("a")  # Raises TypeError
