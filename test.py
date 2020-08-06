class Car:
    # wheels_number:輪胎數量, car_doors:車門數量, passengers:乘客數量
    def __init__(self, wheels_number=4, car_doors=4, passengers=4):
        self.wheels_number = wheels_number
        self.car_doors = car_doors
        self.passengers = passengers
    def drive(self):
        print("Drive a car.")
 
# SUV也是一種車子，所以繼承Car
class SUV(Car):
    # brand_name:品牌名稱, air_bag:安全氣囊數, sunroof:是否擁有天窗
    def __init__(self, wheels_number, car_doors, passengers, brand_name="", air_bag=2, sunroof=False):
        super().__init__(wheels_number, car_doors, passengers)
        self.brand_name = brand_name
        self.air_bag = air_bag
        self.sunroof = sunroof
    # 覆寫父類別的drive
    def drive(self):
        print("Drive this {0} to my vacation.".format(self.brand_name))
 
    def getDetails(self):
        print("==== Details ====")
        print("Brand:", self.brand_name)
        print("Wheels number:", self.wheels_number)    # 可直接呼叫父類別的變數(屬性)
        print("Doors number:", self.car_doors)         # 可直接呼叫父類別的變數(屬性)
        print("Air-bags number:", self.air_bag)
        print("Sunroof:", self.sunroof)
        print("=================")
 
# Bus也是一種車子，所以繼承Car
class Bus(Car):
    # brand_name:品牌名稱, air_bag:安全氣囊數, sunroof:是否擁有天窗
    def __init__(self, wheels_number, car_doors, passengers, brand_name="", air_bag=0):
        super().__init__(wheels_number, car_doors, passengers)
        self.brand_name = brand_name
        self.air_bag = air_bag
 
    # 覆寫父類別的drive
    def drive(self):
        print("Take this {0} to my vacation.".format(self.brand_name))
 
    def getDetails(self):
        print("==== Details ====")
        print("Brand:", self.brand_name)
        print("Wheels number:", self.wheels_number)  # 可直接呼叫父類別的變數(屬性)
        print("Doors number:", self.car_doors)  # 可直接呼叫父類別的變數(屬性)
        print("Air-bags number:", self.air_bag)
        print("=================")
 
# 宣告一台Toyota RAV的休旅車(SUV)
toyota_rav = SUV(4, 5, 5, "Toyota RAV", 4, True)
# 宣告一台BMW X5的休旅車
bmw_x5 = SUV(4, 5, 5, "BMW X5", 6, True)
# 宣告一台Volvo Bus的巴士
volvo_bus = Bus(4, 3, 50, "Volvo Bus", 0)
# 分別呼叫各種車輛的drive()方法
def letsDrive(cars):
    for car in cars:
        car.drive()
def letsgetDetails(cars):
    for car in cars:
        car.getDetails()
letsDrive([toyota_rav, bmw_x5, volvo_bus])
letsgetDetails([toyota_rav, bmw_x5, volvo_bus])




