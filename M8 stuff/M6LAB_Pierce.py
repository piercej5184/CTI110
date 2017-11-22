#CTI 110
#M6Lab
#Jamire Pierce
#10/30

def main():

    #NAME----------------------------------------------------------------
    
    name = input("Whats your name? ")
    greet(name)
    age = int(input("How old are you? "))
    print(ageCategory(age))

def greet(name):

    #GREET---------------------------------------------------------------
    
    print("Hello" ,name)

    #AGE-----------------------------------------------------------------
def ageCategory(age):
    
    
    if age <= 1 :
        Category = "You are a infant."
    elif age >1 and age < 13 :
        Category = "You are a child."
    elif age >= 13 and age < 20 :
        Category = "You are a teenager."
    elif age >= 20 :
        Category = "You are a adult."



    return Category


main()

