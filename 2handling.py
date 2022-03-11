# # handling an exception using try and catch

randomList = ['a', 0, 2]

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         print("The reciprocal of", entry, "is", r)
#         break

#     except Exception as e:
#         print(e.__class__, "occurred. \n")

# ####################################################################################

# # handling Exceptions as shown is not recommended
# # best practice

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         print("The reciprocal of", entry, "is", r)
#         break

#     except (ValueError, TypeError) as e:
#         print("Incorrect variable ", e.__class__, "occurred. \n")

#     except ZeroDivisionError as e:
#         print(e.__class__, "occurred. \n")

#     except Exception as e:
#         print(e.__class__, "occurred. \n")

###################################################################################
# Manually raising an exception

#raise ExceptionClass('More descriptive statement')



# a = int(input("Enter a positive integer: "))

# if a <= 0:
#     raise ValueError("That is not a positive number!")
    



##################################################################################

# Chaining of Exceptions

# 'from' is used in chaining Exceptions

# Exceptions encountered in finally are handled this way

# To remove chaining use from 'None'


# try:
#     print(1 / 0)

# except Exception as exc:
#     # we chain another exception (implicitly)

#     raise RuntimeError("Something bad happened")




####################################################################################

## Try .... Finally
# The finally block is executech) block, if an excepd always after the try(-cattion is thrown or not.

try:
   f = open("README.md",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()


