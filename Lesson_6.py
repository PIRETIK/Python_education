# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:02:27 2022

@author: Leshk
"""

# ____________________Домашнее задание к Шестому уроку_________________________
# ---------------------------- Задание первое ---------------------------------

import time
class TrafficLight_1:
    __color = ["КРАСНЫЙ", "ЖЕЛТЫЙ", "ЗЕЛЕНЫЙ"]
    
    def running(self):
        i = 0
        for i in range(3):
            print(f' Сейчас горит { TrafficLight_1.__color[i]}')
            if i == 0:
                time.sleep(7)
            if i == 1:
                time.sleep(2)
            if i == 2:
                time.sleep(10)

class TrafficLight_2:
    __color = ["КРАСНЫЙ", "ЖЕЛТЫЙ", "ЗЕЛЕНЫЙ"]
    sec =  [7,2,10]

    def timer(sec, color):
        while sec != 0:
            print(sec,color )
            time.sleep(1)
            sec -= 1
    def running(self):
        for i in range(3):
           TrafficLight_2.timer( TrafficLight_2.sec[i], TrafficLight_2.__color[i])
crossroads_1 = TrafficLight_1()
crossroads_2 = TrafficLight_2()
crossroads_1.running()
crossroads_2.running()
# ---------------------------- Задание второе ---------------------------------

class Road:    
    thickness = 15
    mass = 23
    def __init__(self, length, width):
        self._length = length
        self._width = width      
    def mass_count(self):
        return (self._width * self._length * Road.thickness * Road.mass/1000)

road = Road(int(input("ВВедите длинну дороги в метрах: ")), int(input("ВВедите ширину дороги в метрах: ")))
print(f'Масса асфальта = {road.mass_count()} тонн')


# ---------------------------- Задание третье ---------------------------------
class Worker:
    def __init__(self, name, surname,position,income):
        self.name = name
        self.surname = surname   
        self.position = position
        self.__income = income
        
        
class Position(Worker):
    
    def get_full_name(self):
        return (f"{self.position} {self.name} {self.surname}")
        #print(f"{self.position} {self.name} {self.surname}")
        # не могу понять почему при использовании команды принт
        # после строки текста ваводится None

    def get_total_income(self):
        return self._Worker__income["wage"] + self._Worker__income["bonus"]
    # Вот тут то я голову поломал. вспомнил Ваши хакерские методы
n = "Вася" #input("ВВедите имя сотрудника: ")
s = "Пупкин" #input("ВВедите Фамилию сотрудника: ")
p = "Сторож" #input("ВВедите Должность сотрудника: ")       
i = {"wage": 1100, "bonus": 800}   
b = Position(n,s,p,i)

b._Worker__income
b.get_full_name()
b.get_total_income()


# ---------------------------- Задание четвертое ------------------------------

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name =  name
        self.is_police = is_police
    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self,a):
        print(f"Машина повернула на{a}")
    def show_speed(self):
        print (f"Машина едет со скоротью {self.speed}" )
        
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__( speed, color, name, is_police) 
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Вы превысили скорость, ограничение 60")
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__( speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__( speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Вы превысили скорость, ограничение 40")
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
pc = police_car = PoliceCar(90,"White","Dodge", True)    
sc = sport_car = SportCar(110,"Orange","Lambo", False)
wc = work_car = WorkCar(80, "color", "Ford", False)
tc = town_car = TownCar(80 , "Grey" , "Lincoln",False)  

tc.go()
l = "лево" # input("Введите право или лево")
r = "право"# input("Введите право или лево")
tc.turn(l),tc.go(),tc.turn(r),tc.stop()
tc.name
sc.show_speed()
wc.show_speed()
pc.show_speed()         
        

# ---------------------------- Задание пятое----------------------------------------------------------- Задание шестое ---------------------------------

class Stationery:    
    def __init__(self,title):
        self.title = title
    def drow(self):
        print(f"Запуск отрисовки '{self.title}'")
class Pen(Stationery):
    def drow(self):
        super().drow()
class Pencil(Stationery):  
    def drow(self):
        super().drow()
class Handle(Stationery):
    def drow(self):
        super().drow()
        
pen = Pen("ручка")
pencil = Pencil("карандаш")
handle =  Handle("маркер")

pen.drow()
pencil.drow()
handle.drow()
