"""
Stephan and Sophia forget about security and use simple
passwords for everything. Help Nikola develop a password
security check module. The password will be considered
strong enough if its length is greater than or equal to
10 symbols, it has at least one digit, as well as containing
one uppercase letter and one lowercase letter in it.
The password contains only ASCII latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any
data type that can be converted and processed as a boolean.
In the results you will see the converted results.
"""


def checkio(data: str) -> bool:
    is_long = False
    is_strong = False
    if len(data) >= 10:
        is_long = True
    if any(char.isdigit() for char in data) \
            and any(char.isupper() for char in data) \
            and any(char.islower() for char in data):
        is_strong = True

    return is_long and is_strong


if __name__ == '__main__':
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
