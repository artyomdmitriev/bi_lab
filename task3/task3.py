def generate_numbers(num: int = 20) -> dict:
    dictionary = {}
    for i in range(1, num + 1):
        dictionary[i] = i ** i
    return dictionary


def count_characters(count_me_string: str) -> dict:
    dic = {}
    for char in count_me_string:
        dic[char] = dic.get(char, 0) + 1
    return dic


print(generate_numbers(200))
print(count_characters('abcdefgabc'))
