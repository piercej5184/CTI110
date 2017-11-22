#M6 Test Grading Program
#CTI 110
#Jamire Pierce
#11/6

def main():

    
    avg = 0

    calc_average(avg)


def calc_average(avg):
    
    teststart = 0;
    tests = range(1,6)
    for score in tests:
        test = int(input("What is the score for the test? "))
        total_test = teststart + test
        teststart += test
    grade = total_test / 5
    print(determine_grade(grade))

def determine_grade(grade):


    Category = 'error'
   
    if grade >1 and grade < 69 :
        Category = "Grade is: F"
    elif grade >70 and grade < 79 :
        Category = "Grade is: D"
    elif grade >80 and grade < 89 :
        Category = "Grade is: C"
    elif grade >= 90 and grade < 100 :
        Category = "Grade is: B"
    elif grade >= 100 :
        Category = "Grade is: A"


    return Category


main()
