# CTI 110
# M5T1
# Jamire Pierce
# 10/29

def main():

    moving = True

    while moving:
        speed = int(input("What is the speed of the vehicle in mph? "))

        if speed < 1:
            moving = False
            print("Car is not moving")

        else:
            hours = int(input("How many hours has it traveled? "))
            distance = speed * hours
            print("\n")
            print("Hours\tDistance Traveled \n-------------------------")

            hour_table = range(hours)

            import itertools
            for table in hour_table:
                print(table + 2, end="\t" )

                print(speed)
                speed += speed
                
                
main()
