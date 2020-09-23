class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def __init__(self, firstname, lastname, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):

        s = sum(self.scores)
        avg = int(s / len(self.scores))

        if avg >= 90 and avg <= 100:
            # print("Grade: O")
            return "O"
        elif avg >= 80 and avg < 90:
            # print("Grade: E")
            return "E"
        elif avg >= 70 and avg < 80:
            # print("Grade: A")
            return "A"
        elif avg >= 55 and avg < 70:
            # print("Grade: P")
            return "P"
        elif avg >= 40 and avg < 55:
            # print("Grade: D")
            return "D"
        else:
            # print("Grade: T")
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())