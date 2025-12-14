import secrets
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    pool = ""
    if use_lower:   pool += string.ascii_lowercase
    if use_upper:   pool += string.ascii_uppercase
    if use_digits:  pool += string.digits
    if use_symbols: pool += string.punctuation

    if not pool:
        raise ValueError("At least one character set must be enabled.")

    # Guarantee inclusion from each selected set
    required = []
    if use_lower:   required.append(secrets.choice(string.ascii_lowercase))
    if use_upper:   required.append(secrets.choice(string.ascii_uppercase))
    if use_digits:  required.append(secrets.choice(string.digits))
    if use_symbols: required.append(secrets.choice(string.punctuation))

    # Fill the rest
    remaining = length - len(required)
    if remaining < 0:
        raise ValueError("Length is too short for the required character sets.")

    password_chars = required + [secrets.choice(pool) for _ in range(remaining)]
    # Shuffle for randomness
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

if __name__ == "__main__":

    print(generate_password(length=16, use_symbols=True))
