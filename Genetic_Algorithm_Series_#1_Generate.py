'''A genetic algorithm is based in groups of chromosomes, called populations. To start our population of chromosomes we need to generate random binary strings with a specified length.

In this kata you have to implement a function generate that receives a length and has to return a random binary strign with length characters.



Example:
Generate a chromosome with length of 4 generate(4) could return the chromosome 0010, 1110, 1111... or any of 2^4 possibilities.

Note: Some tests are random. If you think your algorithm is correct but the result fails, trying again should work.'''


import random
'''
def generate(length):
    chromosome = []
    for x in range(0, length):
        chromosome.append(str(random.randint(0,1)))
    
    return chromosome
print(generate(3))
'''
def generate(length):
    chromosome = [str(random.randint(0,1)) for _ in range(length)]
    return chromosome
print(generate(3))
