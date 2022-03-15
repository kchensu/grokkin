# def happy(n):
#     seen = []
#     while n not in seen:
#         seen.append(n)
#         n = sum_of_squares(n)

#         if n == 1:
#             return True
#     return False


# def sum_of_squares(n):
#     output = 0
#     while n:
#         digit = n % 10
#         digit = digit ** 2
#         output = output + digit
#         n = n // 10
#     return output
