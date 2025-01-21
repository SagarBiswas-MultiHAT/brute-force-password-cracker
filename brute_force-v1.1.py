import itertools

def brute_force_attack(target_password, allowed_characters): # returning string? Yes, password_attempt is a string.
    password_length = len(target_password)
    total_attempts = sum(len(allowed_characters) ** length for length in range(1, password_length + 1))

# length is both declared and defined by the iteration, and it controls the number of times the expression len(characters) ** length is calculated.

    attempt_count = 0 
    
    for length in range(1, password_length + 1):
        possibilities = itertools.product(allowed_characters, repeat=length) # itertools.product() used to get the cartesian product of the allowed_characters. Example: product('ABCD', repeat=2) gives AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD.
        for attempt in possibilities:
            password_attempt = ''.join(attempt) # ''.join() used to join the characters in the attempt tuple into a string. Example: ('a', 'b', 'c') becomes "abc"
            attempt_count += 1
            if attempt_count % 100000 == 0: # 100000 if you want to print it in every 100000 attempts.
                print(f"\t==> Attempts: {attempt_count}/{total_attempts} ({(attempt_count/total_attempts)*100:.5f}%)", end='\r') # '\r' used to overwrite the line
            if password_attempt == target_password: # password found!
                print(f"\n\n\t\t..:: Password found after {attempt_count} attempts.")
                return password_attempt # returning password_attempt! where? in the function call. brute_force_attack? Yes.
    print(f"\n\n !..:: Password not found after {attempt_count} attempts.")
    return None # benifit of returning None? It's a good practice to return None if the function doesn't return anything else. for example, to use if else statement in the function call.

# Example usage
target_password = "aA1bB"
allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"
print("\n")
result = brute_force_attack(target_password, allowed_characters)
if result:
    print("\n\t    ==> Password found:", result)
else:
    print("Password not found.")

print("\n")

'''
Example:

Let us assume:

characters = "abc" (3 characters)
target_password = "abc" (so password_length = 3)
The line will compute:

For length 1: 3 ** 1 = 3 (possible passwords: "a", "b", "c")
For length 2: 3 ** 2 = 9 (possible passwords: "aa", "ab", "ac", ..., "cc")
For length 3: 3 ** 3 = 27 (possible passwords: "aaa", "aab", ..., "ccc")
Now summing these: 3 + 9 + 27 = 39

This means there are 39 total combinations to try if you're brute-forcing passwords up to length 3 with characters "abc".

'''