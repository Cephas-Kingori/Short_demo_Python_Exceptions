###################################################################
# A user defined Exception

# class ValueTooSmallError(Exception):
#     pass

# number = 10

# try:
#     if number < 50:
#         raise ValueTooSmallError

# except ValueTooSmallError:
#     print("Must be greater than 50")


########################################################################


# class SalaryNotInRangeError(Exception):

#     def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
#         self.salary = salary
#         self.message = message

#     def __str__(self):
#         return f'{self.salary} -> {self.message}'


# salary = int(input("Enter salary amount: "))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary)