def main():
    print("This program reads data for two people")
    print("and computes their body mass index (BMI).\n")

    print("Person 1 information: ")
    person_info()

    print("\nPerson 2 information: ")
    person_info()

    print("\nHave a nice day!")

def bmi_cal(h, w):
    bmi = w / (h**2) * 703
    return bmi


def person_info():
    height = float(input("height (in inches)? "))
    weight = float(input("weight (in pounds)? "))
    BMI = bmi_cal(height, weight)
    print(f"BMI = {BMI:.1f}")
    if (BMI >= 30.0):
        print("class 4")
    elif (BMI >= 25.0):
        print("class 3")
    elif (BMI >= 18.5):
        print("class 2")
    else:
        print("class 1")

main()