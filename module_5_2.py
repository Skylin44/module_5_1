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


house1 = House('ЖК Эльбрус', 10)
house2 = House('ЖК Акация', 20)
# house1.go_to(5)
# house2.go_to(10)
print(str(house1))
print(str(house2))

print(len(house1))
print(len(house2))


