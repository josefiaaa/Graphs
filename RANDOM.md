Learn to demonstrate and show understanding of randomness and its applications.

#### "Randomness has a variety of uses, from algorithm optimization to seeding with robust test data. Understanding the applications of randomness and pseudo-randomness will allow us to utilize randomness as an effective tool when it is appropriate."

### How Random is Random?
  - Most 'random' data generated with Python is not fully random.
  - PRNG: Pseudo-Random Number Generator
  - Any algorithm for generating seemingly random but still reproducible data.
  - TRNG: True Random Number Generator


### PRNGs in Python
##### The random Module

The random.random() function returns a random float in the interval [0.0, 1.0). 

```
# Don't call `random.seed()` yet
import random
random.random()

random.random()
```

With random.seed(), you can make results reproducible, and the chain of calls after random.seed() will produce the same trail of data.

```
random.seed(444)
random.random()
0.3088946587429545


random.random()
0.01323751590501987

random.seed(444)  # Re-seed
random.random()
0.3088946587429545


random.random()
0.01323751590501987
```


With random.randint(), you can generate a random integer between two endpoints.

```
random.randint(0, 10)

random.randint(500, 50000)
```


With random.randrange(), you can exclude the right-hand side of the interval, meaning the generated number always lies within [x, y) and will always be smaller than the right endpoint:

```
random.randrange(1, 10)
```

With random.uniform(), you can generate random floats that lie within a specific [x, y] interval.

```
>>> random.uniform(20, 30)
27.42639687016509
>>> random.uniform(30, 40)
36.33865802745107
```

To pick a random element from a non-empty sequence (list / tuple), you can use random.choice(). For choosing multiple elements from a sequence with replacement (dups are possible), use random.choices().

```
>>> items = ['one', 'two', 'three', 'four', 'five']
>>> random.choice(items)
'four'

>>> random.choices(items, k=2)
['three', 'three']
>>> random.choices(items, k=3)
['three', 'five', 'four']
```

To mimic sampling w/o replacement, use random.sample()

```
>>> random.sample(items, 4)
['one', 'five', 'four', 'three']
```

random.shuffle() will randomize a sequence in-place by modifying the sequence object and randomize the order of elements

```
>>> random.shuffle(items)
>>> items
['four', 'three', 'two', 'one', 'five']
```
