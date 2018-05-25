import pytasks as pt
import sys


def runner(*args):
    args_default = ['generate_numbers', 'count_characters',
                    'fizzbuzz', 'happy_numbers', 'is_palindrome']

    if not args:
        args = args_default

    for func_name in args:
        if func_name in args_default:
            print(func_name, getattr(pt, func_name)())


if __name__ == '__main__':
    args = sys.argv[1:]
    runner(*args)
