class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 < new_floor and new_floor < self.number_of_floors:
                print(i)
            else:
                print("Такого этажа не существует.")
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"'Название: ', {self.name}, 'Количество этажей: ', {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    
house1 = House('ЖК Эльбрус', 10)
house2 = House('ЖК Акация', 20)
# house1.go_to(5)
# house2.go_to(10)
print(str(house1))
print(str(house2))

print(house1 == house2)#__eq__

house1 = house1 + 10 # __add__
print(house1)
print(house1 == house2)

house1 += 10 # __iadd__
print(house1)

house2 = 10 + house2 # __radd__
print(house2)

print(house1 > house2) # __gt__
print(house1 >= house2) # __ge__
print(house1 < house2) # __lt__
print(house1 <= house2) # __le__
print(house1 != house2) # __ne__