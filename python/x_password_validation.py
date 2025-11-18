"""
Validate a simple password rule

Ask the user for a password.
Check if it contains at least one digit, one capital letter, one symbol and is longer than a minimum size.
Think: string inspection and flags.
"""


def new_pswrd():
    password = input("Please enter a new valid password:\n" \
    "(Password must contain 1 capital letter, 1 number, 1 symbol and it must be 8 characters long)\n")
    return password

def pswrd_tokeniser():
    password = new_pswrd()
    tokens = password.strip()
    return tokens

def p_lenght_chck(tokens):
    if len(tokens) < 8:
        return False
    return True

def p_symb_chck(tokens):
    symbols = "!@#$%^&*()_-+=/{/}[]"
    symb_check = any(c in symbols for c in tokens)
    return symb_check

def p_upper_chck(tokens):
    upper_check = any(c.isupper()for c in tokens)
    return upper_check

def p_digit_chck(tokens):
    digit_check = any(c.isdigit() for c in tokens)
    return digit_check

def p_validation():
    while True:
        tokens = pswrd_tokeniser()
        num_char = p_lenght_chck(tokens)
        has_symbol = p_symb_chck(tokens)
        has_upper = p_upper_chck(tokens)
        has_digit = p_digit_chck(tokens)

        if num_char:
            print("\nCharacters number: OK")
        else:
            print("\nTry again: the password must contain at least 8 characters:")

        if has_symbol:
            print('Symbol: OK')
        else:
            print("Try again: password must contain at least a symbol.")

        if has_upper:
            print("Uppercase: OK")
        else:
            print("Try again: password must contain at least an uppercase letter.")

        if has_digit:
            print("Number: OK")
        else:
            print("Try again: password must contain at least a number.")

        if num_char and has_symbol and has_upper and has_digit:
            print("\nPassword accepted.")
            break
        print("\nPlease try again.\n")

p_validation()
