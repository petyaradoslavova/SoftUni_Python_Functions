def numbers(nums):
    sum_negative = sum(n for n in nums if n < 0)
    sum_positive = sum(n for n in nums if n > 0)

    print(sum_negative)
    print(sum_positive)

    if abs(sum_positive) > abs(sum_negative):
        print('The positives are stronger than the negatives')
    else:
        print("The negatives are stronger than the positives")

#
# def numbers(nums):
#     sum_negative = 0
#     sum_positive = 0
#     for num in nums:
#         if num <0:
#             sum_negative += num
#         else:
#             sum_positive += num
#
#     print(sum_negative)
#     print(sum_positive)
#
#     if abs(sum_positive) > abs(sum_negative):
#         print('The positives are stronger than the negatives')
#     else:
#         print("The negatives are stronger than the positives")
#
#
# nums = [int(n) for n in input().split()]
# numbers(nums)


nums = [int(n) for n in input().split()]
numbers(nums)



