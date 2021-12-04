import random
from datetime import datetime
a = [1, -1, 2, 2, 2, 5]
i = 0
startTime = datetime.now()


# function to check whether list is sorted
def is_sorted(b):
    x = 0
    for j in range(1, len(b)):
        if b[j] >= b[j-1]:
            x = x+1
    if x == len(b)-1 or len(b) == 1:
        return True
    else:
        return False


while not is_sorted(a):
    random.shuffle(a)

print(a, "is final")
endTime = datetime.now()
print(f"time taken:{endTime-startTime}")
