#Task1
def range_sum(a, b):
    if a > b:
        a, b = b, a
    s = 0
    for i in range(a, b + 1):
        s += i
    return s
print(range_sum(5, 25))

#Task2
def list_product(nums):
    p = 1
    for n in nums:
        p *= n
    return p

print(list_product([1, 2, 3, 4]))

#Task3
def find_min(nums):
    m = nums[0]
    for n in nums:
        if n < m:
            m = n
    return m

print(find_min([5, 2, 9, -3, 7]))

#Task4
def count_primes(nums):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    c = 0
    for n in nums:
        if is_prime(n):
            c += 1
    return c

print(count_primes([2, 3, 4, 5, 10, 11]))

#Task5
def remove_number(nums, x):
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] == x:
            nums.pop(i)
            count += 1
        else:
            i += 1
    return count

a = [1, 2, 3, 2, 4, 2]
print(remove_number(a, 2))
print(a)

#Task6
def merge_lists(a, b):
    return a + b

x = [1, 2, 3]
y = [4, 5, 6]

result = merge_lists(x, y)
print(result)

#Task7
def power_list(nums, p):
    res = []
    for i in nums:
        res.append(i ** p)
    return res

numbers = [1, 2, 3, 4]
power = 3

result = power_list(numbers, power)
print(result)
