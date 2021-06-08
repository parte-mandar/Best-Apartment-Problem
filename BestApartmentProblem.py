class BestApartmentProblem:
    def __init__(self, inputList):
        MAX = len(inputList) + len(inputList)
        distanceFromEachBlock = []

        numOfBlocks = len(inputList) - 1
        travelled = 0 # The distance travelled from a selected block. Will be zero before every iteration.
        currentBlock = 0 # The block which is currently in process.
        reqs = [] # Checking the required services distances at each block
        counter = 0 # A normal integer counter

        while (currentBlock <= numOfBlocks):
            if (currentBlock != 0):
                counter = 0
                for test in distanceFromEachBlock[currentBlock-1]:
                    if (test > currentBlock-1):
                        reqs.append(distanceFromEachBlock[currentBlock-1][counter] - 1)
                        #distanceFromEachBlock[currentBlock] = distanceFromEachBlock[currentBlock-1] - 1
                    elif (test <= currentBlock-1):
                        reqs.append(distanceFromEachBlock[currentBlock-1][counter] + 1)
                        #distanceFromEachBlock[currentBlock] = distanceFromEachBlock[currentBlock-1] + 1

                    counter = counter + 1

                distanceFromEachBlock.append(self.__appendListCompletely(reqs)) 
                counter = 0

                for test in inputList[currentBlock].values():
                    if (test == True):
                        distanceFromEachBlock[currentBlock][counter] = 0

                    counter = counter + 1
            
            elif (currentBlock == 0):
                for test in inputList[currentBlock].values():
                    if (test == False):
                        reqs.append(MAX)
                    elif (test == True):
                        reqs.append(0)

                distanceFromEachBlock.append(self.__appendListCompletely(reqs)) 
                # the function appendListCompletely is used to assign 'reqs' to the distanceFromEachBlock list completely
                # Otherwise, any changes made in 'reqs' list will also be reflected in 'distanceFromEachBlock' list

            while (travelled < numOfBlocks - currentBlock):
                travelled = travelled + 1
                counter = 0
                for test in inputList[travelled + currentBlock].values():
                    if (test == True):
                        if (distanceFromEachBlock[currentBlock][counter] > travelled):
                            distanceFromEachBlock[currentBlock][counter] = travelled

                    counter = counter + 1

            currentBlock = currentBlock + 1
            travelled = 0
            reqs.clear()


        print(distanceFromEachBlock)
        counter = 0
        maxDistances = {}
        minAdditions = {}

        for block in distanceFromEachBlock:
            maxDistances.update({counter: max(block)})
            minAdditions.update({counter: self.__add(block)})
            counter = counter + 1

        bestBlockFinal = self.__calculateBestBlock(maxDistances.values(), minAdditions.values())

        print("The best apartment for you to live will be in Block " + str(bestBlockFinal+1))

    # Essential functions
    def __appendListCompletely(self, tempList):
        tempList2 = []
        for temp in tempList:
            tempList2.append(temp)

        return tempList2

    def __add(self, tempList):
        result = 0
        for temp in tempList:
            result = result + temp

        return result

    def __calculateBestBlock(self, distanceKeys, additionKeys):
        calc = {}
        counter = 0
        for distance in distanceKeys:
            calc.update({counter: distance}) 
            counter = counter + 1

        counter = 0
        for addition in additionKeys:
        #for distance in distanceKeys:
            calc[counter] = calc[counter] + addition    
            counter = counter + 1

        
        minDist = calc[0]
        minIndex = 0
        counter = 0
        for item in calc.values():
            if (minDist > item):
                minDist = item
                minIndex = counter

            counter = counter + 1

        return minIndex
