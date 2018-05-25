def generate_numbers(num=20):
    dic = {}
    for i in range(1, num + 1):
        dic[i] = i ** i
    return dic


def count_characters(count_me_string='abcdab'):
    dic = {}
    for char in count_me_string:
        dic[char] = dic.get(char, 0) + 1
    return dic


def fizzbuzz():
    result = []
    for i in range(1, 101):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif int(i) % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def is_happy(n):
    numbers = []
    while True:
        string_number = str(n)
        r = 0
        for i in string_number:
            r += (int(i) * int(i))
        if r == 1:
            return True
        elif r in numbers:
            return False
        numbers.append(r)
        n = r


def happy_numbers(num=200):
    result = []
    for i in range(1, num + 1):
        if is_happy(i):
            result.append(i)
    return result


def is_palindrome(num=1221):
    input_str = str(num)
    reversed_string = input_str[::-1]
    return True if input_str == reversed_string else False
