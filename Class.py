class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower
    
    def drive(self) -> None:
        print(f'{self.brand} is driving!')

    def get_info(self, var: int) -> None:
        print(var)
        print(f'{self.brand} with {self.horsepower} horsepower')

    def __str__(self) -> str:
        return f'{self.brand} with {self.horsepower}hp'

volvo: Car = Car('Volvo', 200)

# volvo.drive()

# volvo.get_info(10)

print(volvo)

volvo