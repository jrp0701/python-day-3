def weather_check():
    temp = input("What is the temp?")
    if temp >= 25:
        print("It's hot outside.")
    else:
        if temp < 25:
            print("It's cold ouside.")
        else:
            print("It's nice out.")

def main():
    weather_check()

main()