from BestApartmentProblem import BestApartmentProblem

required = ["Gym", "School", "Store"]

inputList = [
    {required[0]: True, required[1]: True, required[2]: False},
    {required[0]: False, required[1]: False, required[2]: False},
    {required[0]: False, required[1]: False, required[2]: True},
    {required[0]: False, required[1]: True, required[2]: False},
    {required[0]: False, required[1]: True, required[2]: False}
]


BestApartmentProblem(inputList)