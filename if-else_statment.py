"""light = input("light_color : ").lower()
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("look")
else:
    print("signal is not working")"""



# new code
"""def signal(light):
    if light == "red":
        print("stop")
    elif light == "green":
        print("go")
    elif light == "yellow":
        print("look")
    else:
        print("invalid color")

light = input("Enter the color of signal light : ")
signal(light)"""


def result(marks):
    if marks < 100 and marks > 90:
        print("Grade A")
    elif marks < 90 and marks > 80:
        print("Grade B")
    elif marks < 80 and marks > 60:
        print("Grade C")
    else:
        print("You are fail your marks is : ", marks, "\nbetter luck next time :)")

marks = int(input("Enter your marks :"))
result(marks)

