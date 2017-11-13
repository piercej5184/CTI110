#M5T2 Bug Collector
#Jamire Pierce
#CTI 110
#10/9/2017

def main():

    #7 days (range?)
    #Number of Bugs
    #Todays Bugs
    #Total Bugs

    totalstart = 0;

    week = range(1,8)
    
    for day in week:
        todays_bugs = int(input("What is today's bugs?"))
        Total_bugs = totalstart + todays_bugs
        totalstart += todays_bugs

    print("Total of bugs:", Total_bugs)
   
main()
