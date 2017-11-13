# CTI 110
# M3LAB
# Pierce
# 9/18

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59
    # TO DO: define the rest of the scores

    
    score = int(input('Enter grade: '))

    if score >= 90:
        print('Your grade is: A')
    else:
        if score >= 80:
            print('Your grade is: B')
        else:
            if score >= 70:
                print('Your grade is: C')
            else:
                if score >= 60:
                    print( 'Your grade is: D')
            if score <= 59:
                        print('Your grade is: F')







# program start
main()
