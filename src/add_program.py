'''Hello Module'''
def add_numbers(number_one, number_two):
    '''add two numbers'''
    return number_one + number_two

NUM_ONE = 4
NUM_TWO = 5
TOTAL = add_numbers(NUM_ONE, NUM_TWO)
print(f'The sum of {NUM_ONE} and {NUM_TWO} is {TOTAL}')
