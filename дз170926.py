#ДЗ на 17.09.2026
import math


a = float(input("введите длину 1 стороны:"))
b = float(input("введите длину 2 стороны:"))
angle = float(input("введите значение угла между этими сторонами:"))


angle_rad = angle*math.pi/180
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle_rad))
print("длина 3 стороны = ", c)

