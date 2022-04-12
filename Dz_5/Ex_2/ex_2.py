'''
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n(включительно), не используя
ключевое слово yield.
'''

nums1 = int(input('input number:'))
odd_gen = (num1 for num1 in range(1, nums1 + 1, 2))
for num1 in odd_gen:
    print(num1)
print(type(odd_gen))