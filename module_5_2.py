class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.nuber_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.nuber_of_floors:
            for i in range(new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.nuber_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.nuber_of_floors}"


house = House('ЖК Эльбрус', 30)
# __str__
print(house)
# __len__
print(len(house))
