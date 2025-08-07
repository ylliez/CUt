import random
import string

def random_token(length=6):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

filenames = ["step_" + random_token() + ".html" for _ in range(8)]

for i, fname in enumerate(filenames, 1):
    print("Slice {}: {}".format(i, fname))
