required = ["Gym", "School", "Store"]

inputList = [
    {required[0]: False, required[1]: True, required[2]: False},
    {required[0]: True, required[1]: False, required[2]: False},
    {required[0]: True, required[1]: True, required[2]: False},
    {required[0]: False, required[1]: True, required[2]: False},
    {required[0]: False, required[1]: True, required[2]: True}
]

MAX = len(inputList) + len(inputList)
distanceFromEachBlock = []

numOfBlocks = len(inputList) - 1
travelled = 0 # The distance travelled from a selected block. Will be zero before every iteration.
currentBlock = 0 # The block which is currently in process.
reqs = [] # Checking the required services distances at each block
counter = 0 # A normal integer counter

print ( numOfBlocks - currentBlock)

reqs = [MAX, MAX, MAX]
distanceFromEachBlock.append(reqs)

temp = distanceFromEachBlock[currentBlock][counter]

print(type(temp))
print(temp)

for test in distanceFromEachBlock[currentBlock]:
    distanceFromEachBlock[currentBlock][0] = 9

temp = distanceFromEachBlock[currentBlock][counter]
print(temp)