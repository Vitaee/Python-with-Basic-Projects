def getConverTo():
    which = input("Enter Selection: ")
    while which != "F" and which != "C":
        which = input("Enter Selection: ")
    return which
which = getConverTo()    

def FahrenToCelsius(start,end):
    #print("Degrees", "Degrees")
    print("Fahrenheit", "Celsius")
    
    for temp in range(start, end, +1 ):
        converted_temp = (temp - 32) * 5/9
        print(" ",format(temp)," ",format(int(converted_temp)))
temp_start = int(input("Enter temprature to convert: "))
temp_end = int(input("Enter ending temprature to convert: ")) 


FahrenToCelsius(temp_start, temp_end)       