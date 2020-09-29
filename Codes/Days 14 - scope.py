class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):

        maximum = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                difference = abs(self.__elements[i] - self.__elements[j])
                if difference >= maximum:
                    maximum = difference
        self.maximumDifference = maximum


# End of Difference class

_ = input("Enter len of array: ")
a = [int(e) for e in input("Enter array (ex. 1 2 3): ").split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)