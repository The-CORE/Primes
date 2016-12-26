# From knowing two is prime, make a list of other primes.

import math

DEBUG = True

primes = [2]

try:
    if DEBUG: print("Opening and reading primes.txt.")
    f = open("primes.txt", "r")
    line = f.readline()
    if line != "2\n":
        raise ValueError
    line = f.readline()
    while line != "":
        primes.append(int(line.replace("\n", "")))
        line = f.readline()
    f.close()
except (FileNotFoundError, ValueError):
    if DEBUG: print("Invalid primes.txt. Writing over.")
    f = open("primes.txt", "w")
    f.write("2\n")
    f.close

highest_prime_found = primes[len(primes) - 1]
value_to_test = highest_prime_found + 1
# If the prime is two, then, you do need to test three, but, in all other cases
# this would make testing an even number, and hence not prime, so, this code is
# less efficent than it could have been. But, it feels better to do it this way
# not sure why.

while True:
    #if DEBUG: input("Press enter to continue. ")
    is_prime = True
    index_of_factor_to_check = 0
    factor_to_check = primes[index_of_factor_to_check]
    while factor_to_check <= math.sqrt(value_to_test):
        if value_to_test % factor_to_check == 0:
            is_prime = False
            break
        index_of_factor_to_check += 1
        factor_to_check = primes[index_of_factor_to_check]
    if is_prime:
        if DEBUG: print(str(value_to_test) + " is prime.")
        primes.append(value_to_test)
        f = open("primes.txt", "a")
        f.write(str(value_to_test) + "\n")
        f.close()
    value_to_test += 1
