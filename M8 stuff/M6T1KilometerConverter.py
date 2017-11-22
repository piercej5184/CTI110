#CTI-110
#M6T1 Kilometer Converter
#Jamire Pierce
#10/25/17


#Miles to kilometers

def main():
    kilo = int(input("Please enter amount of kilometers?"))
    ShowMiles(kilo)
    
def ShowMiles(kilo):
    miles = kilo * 0.6214
    print(miles)

main()
