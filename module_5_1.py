class House:

    def __init__(self, name, number_of_floors):
        self.mame = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 < new_floor and new_floor < self.number_of_floors:
                print(i)
            else:
                print("Такого этажа не существует.")
                break

house1 = House('ЖК Эльбрус', 30)
house2 = House('Домик в деревне', 2)
house1.go_to(5)
house2.go_to(10)


