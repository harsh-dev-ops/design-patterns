class Driver:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Car:
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f'Car is driven by {self.driver.name}')


class CarProxy:
    def __init__(self, driver: Driver):
        self.driver = driver
        self.__car = Car(driver)

    def drive(self):
        if self.driver.age >= 18:
            self.__car.drive()
        else:
            print('Driver is too young')


if __name__ == '__main__':
    driver = Driver('Harsh', 24)
    car = CarProxy(driver)

    car.drive()

    driver = Driver('Prateek', 11)
    car = CarProxy(driver)

    car.drive()
