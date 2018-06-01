def count_characters(count_me_string='abcdab'):
    dic = {}
    for char in count_me_string:
        dic[char] = dic.get(char, 0) + 1
    return dic


def fizzbuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif int(number) % 5 == 0:
        return "Buzz"
    else:
        return number


def is_palindrome(num=1221):
    input_str = str(num)
    reversed_string = input_str[::-1]
    return True if input_str == reversed_string else False
