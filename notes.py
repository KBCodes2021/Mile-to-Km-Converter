# #To be able to add unlimited variables:
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# # print(add(1, 3, 6, 65, 32))
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     # print(n)
#
#
#
# calculate(7, add=3, multiply=5)
#
# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)