def main():
    time = getTime()
    mealTime = convertTime(time)
    if mealTime != "error":
        print(mealTime)

        
def getTime():
    userInput = input("What time is it? ").replace(":", ".")   
    return userInput

        
def convertTime(time):
    y = time[:-1]
    x = float(y)
    if x >= 7 and x <= 8:
        return "breakfast time"
    elif x >= 12 and x <=13:
        return "lunch time"
    elif x >= 18 and x <= 19:
        return "dinner time"
    else:
        return "error"

if __name__ == "__main__":
    main()
