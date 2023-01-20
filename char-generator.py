import string
import random

def generator(N, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(N))

digit = int(input("How many chars you want: "))

print("Result: ", generator(digit))