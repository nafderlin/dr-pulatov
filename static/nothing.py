# ============================================================
# useless.py — 200 lines of Python achieving absolutely nothing
# ============================================================

a = 1
b = 2
c = a + b  # 3. A landmark achievement.

name = "World"
greeting = f"Hello, {name}!"
# greeting exists in memory. Quietly. Alone.

colors = ["red", "green", "blue"]
more_colors = ["yellow", "purple", "orange"]
all_colors = colors + more_colors
# 6 colors. Zero use cases.

x = 10
y = 20
z = x * y
z = z // 2
z = z + 0
z = z - 0
# z is 100. We put real effort into that.

is_true = True
is_false = False
is_maybe = is_true and is_false
# is_maybe is False. Like this file's ambitions.

pi = 3.14159265358979
tau = pi * 2
half_pi = pi / 2
pi_squared = pi ** 2
# Math. Floating in the void.

empty_str = ""
not_empty = "not empty"
still_useless = empty_str + not_empty
# still_useless is "not empty". Ironic.

counter = 0
counter += 1
counter += 1
counter += 1
counter -= 1
counter += 1
# counter is 3. The journey mattered to no one.

numbers = [1, 2, 3, 4, 5]
reversed_nums = list(reversed(numbers))
sorted_nums = sorted(numbers)
# Same list. Reversed. Sorted back. A round trip.

upper = "hello".upper()
lower = "WORLD".lower()
stripped = "   spaces   ".strip()
length = len(stripped)
# length is 6. Filed under: who cares.

num = 42
as_float = float(num)
as_string = str(num)
back_to_int = int(as_string)
# back_to_int is 42. Nothing was lost. Nothing was gained.

null_var = None
is_none = null_var is None
is_falsy = not null_var
# Both True. The void confirms itself.

# -------------------------------------------------------
# Functions that exist
# -------------------------------------------------------

def do_nothing():
    return None

def also_do_nothing(param):
    unused = param
    return unused

def add_numbers(p, q):
    result = p + q
    return result

r1 = do_nothing()
r2 = also_do_nothing("ignored value")
r3 = add_numbers(5, 10)
# r3 is 15. A function fulfilled its destiny and nobody noticed.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

fact_7 = factorial(7)
fact_10 = factorial(10)
# fact_10 is 3628800. Computed. Stored. Never printed.

def is_palindrome(s):
    return s == s[::-1]

p1 = is_palindrome("racecar")
p2 = is_palindrome("python")
p3 = is_palindrome("useless")
# p3 is False. "useless" is not a palindrome. It is a descriptor.

def clamp(val, low, high):
    return max(low, min(high, val))

c1 = clamp(150, 0, 100)
c2 = clamp(-5, 0, 100)
c3 = clamp(50, 0, 100)
# All clamped. None liberated.

# -------------------------------------------------------
# Data structures doing nothing
# -------------------------------------------------------

stack = []
stack.append("first")
stack.append("second")
stack.append("third")
popped = stack.pop()
# popped is "third". It lived briefly.

queue = []
queue.append("alpha")
queue.append("beta")
queue.append("gamma")
dequeued = queue.pop(0)
# dequeued is "alpha". Gone.

my_set = {1, 2, 3, 4, 5}
other_set = {4, 5, 6, 7, 8}
union = my_set | other_set
intersection = my_set & other_set
difference = my_set - other_set
# Set theory. Applied to nothing.

my_dict = {"name": "AbuBakr", "tool": "CommitGuard", "lang": "Python"}
keys = list(my_dict.keys())
vals = list(my_dict.values())
items = list(my_dict.items())
# Extracted. Stored. Never read again.

nested = {"outer": {"inner": {"deep": 42}}}
deep_val = nested["outer"]["inner"]["deep"]
# deep_val is 42. We went deep for that.

matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
diagonal = [matrix[i][i] for i in range(3)]
diag_sum = sum(diagonal)
# diag_sum is 3. The identity matrix identifies nothing.

# -------------------------------------------------------
# Comprehensions going nowhere
# -------------------------------------------------------

squares   = [n ** 2 for n in range(1, 11)]
evens     = [n for n in range(1, 21) if n % 2 == 0]
odds      = [n for n in range(1, 21) if n % 2 != 0]
flat      = [x for row in matrix for x in row]
even_sq   = {n: n ** 2 for n in range(1, 6)}
unique_sq = {n ** 2 for n in range(-5, 6)}
# Six comprehensions. Zero comprehension of why.

gen = (n ** 3 for n in range(10))
first_cube = next(gen)
# first_cube is 0. The generator has more. Nobody will ask.

# -------------------------------------------------------
# String operations in quiet desperation
# -------------------------------------------------------

sentence = "the quick brown fox jumps over the lazy dog"
word_list = sentence.split()
word_count = len(word_list)
rejoined = "-".join(word_list)
# A sentence destroyed and rebuilt. Therapy through strings.

replaced = sentence.replace("fox", "cat")
title_case = sentence.title()
capitalized = sentence.capitalize()
# "The Quick Brown Fox..." but make it a cat. Nobody reads it either way.

starts = sentence.startswith("the")
ends = sentence.endswith("dog")
contains = "fox" in sentence
# All True. The string passes all its tests. Unlike this code.

padded_left  = "42".rjust(10)
padded_right = "42".ljust(10)
padded_both  = "42".center(10, "-")
# Padding. The packaging with nothing inside.

chunks = [sentence[i:i+10] for i in range(0, len(sentence), 10)]
chunk_count = len(chunks)
# Chunked. Like the ambition for this file.

# -------------------------------------------------------
# Math and numbers, for no reason whatsoever
# -------------------------------------------------------

import math

log_val   = math.log10(1000)
sqrt_val  = math.sqrt(144)
ceil_val  = math.ceil(4.1)
floor_val = math.floor(4.9)
# sqrt_val is 12. We used the math module for this.

sin_val = math.sin(math.pi / 6)
cos_val = math.cos(math.pi / 3)
tan_val = math.tan(math.pi / 4)
# Trigonometry. The angle of this code's usefulness: approaching zero.

hypotenuse = math.hypot(3, 4)
# 5.0. Pythagoras would be indifferent.

fibonacci = [0, 1]
for i in range(2, 12):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
# 12 Fibonacci numbers. Released into a list. Never seen again.

primes = [n for n in range(2, 50) if all(n % i != 0 for i in range(2, int(n**0.5)+1))]
prime_count = len(primes)
# prime_count is 15. Counted. Noted. Discarded.

import random

random_int   = random.randint(1, 100)
random_float = random.random()
random_choice = random.choice(all_colors)
random.shuffle(all_colors)
# all_colors is shuffled. Chaos introduced into an already meaningless list.

import hashlib

md5_hash  = hashlib.md5(b"nothing").hexdigest()
sha1_hash = hashlib.sha1(b"also nothing").hexdigest()
sha256    = hashlib.sha256(b"still nothing").hexdigest()
# Three hashes. Cryptographically secure meaninglessness.

# -------------------------------------------------------
# Final stretch. Almost at 200. Still nothing.
# -------------------------------------------------------

a, b = 10, 20
a, b = b, a
# Swapped. Without a temp variable. Showing off for an empty room.

result = (lambda x, y: x + y)(3, 7)
# result is 10. A lambda used once, inline, and forgotten.

truthy_things  = [1, "yes", [1], {"k": "v"}, True]
falsy_things   = [0, "", [], {}, None, False]
all_truthy     = all(truthy_things)
any_falsy      = any(falsy_things)
# all_truthy is True. any_falsy is True. Confirmed.

zipped = list(zip([1, 2, 3], ["a", "b", "c"], [True, False, True]))
unzipped_nums, unzipped_chars, unzipped_bools = zip(*zipped)
# Zipped. Unzipped. Like a jacket in an empty room.

enumerated = list(enumerate(["zero", "one", "two", "three"], start=0))
# [(0, "zero"), (1, "one")...]. Indexed. Ignored.

mapped   = list(map(lambda n: n * 3, range(1, 6)))
filtered = list(filter(lambda n: n > 6, mapped))
# filtered is [9, 12, 15]. The survivors of a pointless culling.

from functools import reduce
reduced = reduce(lambda acc, n: acc + n, range(1, 11), 0)
# reduced is 55. reduce used exactly once, for nothing.

# ============================================================
# EOF. 200 lines. No output. No side effects. Immaculate.
# ============================================================