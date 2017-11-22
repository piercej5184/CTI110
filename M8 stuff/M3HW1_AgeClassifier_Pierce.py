# CTI-110 
# M3HW1 - Age Classifier 
# Jamire Pierce 
# sept/20/17
#

def main():

    age = int(input("This program will display whether the person is an infant, a child, a teenager, or an adult. Please input age in years:"))

    # infant = age <= 1
    # child = age >1 or age <13
    # tennager = age >+ 13 and age <20
    # adult = age < 20

    if age <= 1 :
        print("He or she is an infant.")
    elif age >1 and age < 13 :
        print("He or she is a child.")
    elif age >= 13 and age < 20 :
        print("He or she is a teenager.")
    elif age >= 20 :
            print("He or she is an adult.")


main()

