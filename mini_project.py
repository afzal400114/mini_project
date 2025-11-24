# class Persen:
#     def __init__(self,name,age,roll_num):
#         self.name = name
#         self.age = age
#         self.roll_num = roll_num
#         print("Persen consturction called: ")
#     def details(self):
#         print(f"MY name is {self.name} and MY age is {self.age} and MY roll_num is {self.roll_num}")
# class Student(Persen):
#     def __init__(self,name,age,roll_num):
#         super().__init__(name,age,roll_num)
#         print("Student consturction called: ")
# class Teacher(Persen):
#     def __init__(self,name,age,roll_num):
#         super().__init__(name,age,roll_num)
#         print("Teacher consturction called: ")
# class Staff(Persen):
#     def __init__(self,name,age,roll_num):
#         super().__init__(name,age,roll_num)
#         print("Staff consturction called: ")
# p1 = Persen("afzal",21,409)
# S1 = Student("abc",2,9)
# T1 = Teacher("ab",1,4)   
# S2 = Staff("al",21,49)
# print(p1.__dict__)

# class Payment:
#     def __init__(self,amount,pay_method):
#         self.amount = amount
#         self.pay_method = pay_method
#     def payment_details(self):
#         print(f"Payment amount is {self.amount} and Payment method is {self.pay_method}")   
# class CreditCardPayment(Payment):
#     def __init__(self,amount,pay_method,card_number):
#         super().__init__(amount,pay_method)
#         self.card_number = card_number
#     def payment_details(self):
#         super().payment_details()
#         print(f"Card Number is {self.card_number}")
# class JazzCashPayment(Payment):
#     def __init__(self,amount,pay_method,account_number):
#         super().__init__(amount,pay_method)
#         self.account_number = account_number
#     def payment_details(self):
#         super().payment_details()
#         print(f"Account Number is {self.account_number}")
# class EasypaisaPayment(Payment):
#     def __init__(self,amount,pay_method,mobile_number):
#         super().__init__(amount,pay_method)
#         self.mobile_number = mobile_number
#     def payment_details(self):
#         super().payment_details()
#         print(f"Mobile Number is {self.mobile_number}")
# Payment1 = CreditCardPayment(5000,"Credit Card","1234-5678-9012-3456")
# Payment2 = JazzCashPayment(3000,"JazzCash","9876543210")
# Payment3 = EasypaisaPayment(2000,"Easypaisa","0123456789")
# Payment1.payment_details()
# Payment2.payment_details()
# Payment3.payment_details()