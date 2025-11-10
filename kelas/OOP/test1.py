class Counter(object):
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return f"value = {self.value}"

    def count(self):
        self.value += 1
    
    def reset(self):
        self.value = 0

my_counter = Counter()
print(my_counter,1)
my_counter.count()
print(my_counter)
my_counter.reset()
print(my_counter)

