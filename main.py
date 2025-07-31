from random import sample
from secrets import choice, randbelow
from string import digits, punctuation, ascii_lowercase, ascii_uppercase


class PasswordError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PasswordLengthError(PasswordError):
    pass


class PasswordCharactersError(PasswordError):
    pass


def make_password(length: int=16, delete_chars: str='') -> str:
    if length < 12:
        raise PasswordLengthError(
            'password must be at least 12 characters long.')

    def get_char(seq: str) -> str:
        return choice(seq)

    def remove_spaces(seq: str) -> str:
        return seq.replace(' ', '')

    def remove_chars(seq: str) -> list:
        chars = f'{digits} {punctuation} {ascii_lowercase} {ascii_uppercase}'
        new_seq = ''.join([c for c in chars if c not in remove_spaces(seq)])
        new_seq = new_seq.split()

        if len(new_seq) < 4:
            raise PasswordCharactersError(
                'password must contain upper and lower case letters,'\
                'digits and symbols.')

        return new_seq

    chars = remove_chars(delete_chars)
    password = []
    count = 0

    for i in range(length):
        if count < 4:
            password.append(get_char(chars[count]))
            count += 1
        else:
            password.append(get_char(chars[randbelow(len(chars))]))

    return ''.join(sample(password, k=len(password)))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        prog='genpass',
        description='Strong password generator',
        epilog='Developed by DevTools'
    )

    parser.add_argument(
        '-l',
        help='password length (default 16)',
        type=int,
        metavar='INT',
        default=16
    )

    parser.add_argument(
        '-d',
        help='characters to delete',
        type=str,
        metavar='STR',
        default=''
    )

    args = parser.parse_args()

    try:
        password = make_password(args.l, args.d)
    except Exception as e:
        print(f'\033[31m{type(e).__name__}:\033[0m {e}')
    else:
        print(password)
