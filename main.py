import math


class TenQuestions:
    firstName = ["Dave", " Cave ", "Lave", " Pave", " Save"]
    element = "Mom"
    numberOfPeople = [1, 2, 3, 4, 5, 6]
    numberOFCars = [8, 9, 15, 25, 40, 42]

    def getLastIndex(firstName):
        last_index = len(firstName)
        return last_index

    def getSecondToLastIndex(firstName):
        second_Last_index = len(firstName) - 1
        return second_Last_index

    def getFirstElement(firstName):
        return firstName[0]

    def getLastElement(firstName):
        last_index = len(firstName) - 1
        last_element = firstName[last_index]
        return last_element

    def getSecondToLastElement(firstName):
        second_Last_index = len(firstName) - 2
        second_Last_element = firstName[second_Last_index]
        return second_Last_element

    def getSum(numberOfPeople):
        base = 0
        for x in numberOfPeople:
            base = x + base
        return base

    def getAverage(numberOfPeople):
        base = 0
        howMany = len(numberOfPeople)
        for x in numberOfPeople:
            base = x + base
        total = base/howMany
        return total

    def extractAllOddNumbers(numberOfPeople):
        Odds = []
        for x in numberOfPeople:
            if x % 2 != 0:
                Odds.append(x)
        return Odds

    def extractAllEvenNumbers(numberOfPeople):
        Evens = []
        for x in numberOfPeople:
            if x % 2 == 0:
                Evens.append(x)
        return Evens

    def contains(firstname, element):
        for x in firstname:
            if x == element:
                return True

    # Qa1
    print(getLastIndex(firstName))
    # Qa2
    print(getSecondToLastIndex(firstName))
    # QA3
    print(getFirstElement(firstName))
    # QA4
    print(getLastElement(firstName))
# QA5
    print(getSecondToLastElement(firstName))
# QA6
    print(getSum(numberOfPeople))
# QA7
    print(getAverage(numberOfPeople))
# QA8
    print(extractAllOddNumbers(numberOfPeople))
# QA9
    print(extractAllEvenNumbers(numberOfPeople))
# QA10
    print(contains(firstName,element))
