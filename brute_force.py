import itertools

def brute_force_attack(target_password, characters):
    password_length = len(target_password)
    for length in range(1, password_length + 1):
        possibilities = itertools.product(characters, repeat=length)
        for attempt in possibilities:
            password_attempt = ''.join(attempt)
            if password_attempt == target_password:
                return password_attempt
    return None

# Example usage
target_password = "aA1bB"
allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

result = brute_force_attack(target_password, allowed_characters)
if result:
    print("Password found:", result)
else:
    print("Password not found.")
