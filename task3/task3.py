def generate_numbers(num=20):
    dictionary = {}
    for i in range(1, num + 1):
        dictionary[i] = i ** i
    return dictionary


def count_characters(count_me_string='abcdab'):
    dic = {}
    for char in count_me_string:
        dic[char] = dic.get(char, 0) + 1
    return dic


print(generate_numbers(200))
print(count_characters('abcdefgabc'))
