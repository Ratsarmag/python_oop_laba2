class Car:
    color = None # цвет автомобиля
    fuel = None # количество топлива
    seats = None
    maxFuel = None

    def go(self): # Команда ехать:
        pass

    def turn(self): # Команда поворачивать:
        pass

    def stop(self): # Команда остановиться:
        pass

    def printInfo(self):
        print('Информация о автомобиле:')
        print(f"Цвет: {myCar.color}")
        print(f"Количество топлива в бензобаке: {myCar.fuel}")
        print(f"Макс. количество топлива: {myCar.maxFuel}")
        print(f"Вместимость: {myCar.seats}")

myCar = Car()

myCar.color = 'red' # красим в красный цвет
myCar.fuel = 50 # заливаем топливо
myCar.maxFuel = 100
myCar.seats = 2

myCar.go()
myCar.turn()
myCar.stop()
myCar.printInfo()