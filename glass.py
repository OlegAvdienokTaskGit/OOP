"""
Создать класс стакан с полем объем и методами: добавить воды, 
добавить молока, вылить часть смеси, вывести количество смеси. 
Реализовать проверки на добавление отрицательного количества и на переполнение.
"""

class Glass():
    def __init__(self, max_volume, current_volume=0):
        if current_volume < 0 or current_volume> max_volume:
            raise ValueError('what are doing')
        self.max_volume = max_volume
        self.current_volume = current_volume

    def __repr__(self):
        return "Glass with {} of {}".format(self.current_volume, self.max_volume)

    def add_water(self, add_volume):
        if add_volume < 0:
            print('объем не может быть отрицательным')
            return
        if self.current_volume + add_volume > self.max_volume:
            print('не влезло', self.current_volume + add_volume - self.max_volume)
            self.current_volume = self.max_volume
        else:
            self.current_volume += add_volume


g1 = Glass(200, 150)
print(g1)
g1.add_water(100)
print(g1)

g1.add_water(-10)
