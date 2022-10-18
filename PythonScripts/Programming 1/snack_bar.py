# write a Python function to do the following steps:
# ask the user for the weight (in grams) of sugar, flour and fruit used to produce a snack bar
# display the total weight of the snack bar
# if the amount of fruit is higher or equal than 80 grams, the program should display "1 portion of your 5 a day"
# if the amount of flour is 0,  display "The snack is gluten free"; otherwise display: "Allergenic:  gluten"
# you need to compute the total calories of the snack bar; you know that 1 gram of sugar has 3.87 calories, 1 gram of flour has 3.64 and 1 gram of fruit has 0.52:
# calories = sugar * 3.87 + flour * 3.64 + fruit * 0.52
# compute and display the amount of calories of the snack
# snacks are classified based on their number of calories:
# 0 – 200    Dietetic
# 201 – 400    Normal
# 401 or more    Highly caloric
# display the category of the snack
# if the snack has less than 300 calories and more than 50 grams of fruit the snack is considered healthy;  in that case display "It's a healthy snack!"
# if the snack has more than 100 grams of flour or sugar and less than 20 grams of fruit the snack is considered unhealthy; in that case display "It's an unhealthy snack!"


def snackComputing(s: float, fl: float, fr: float):
    tC = s * 3.87 + fl * 3.64 + fr * 0.52
    print("\nThe snack weighs in total: ", s + fl + fr, "grams.")
    if fr >= 80.0:
        print("1 portion of your 5 a day")
    if fl == 0:
        print("The snack is gluten free.")
    else:
        print("Your snack contains the following allgerns:\nGluten.")
    print("Your snack contains the following amount of calories per portion: ", tC)
    if tC > 0 and tC <= 200:
        print("Your snack is a Dietetic snack.")
    if tC > 200 and tC <= 400:
        print("Your snack is a Normal snack.")
    if tC > 400:
        print("Your snack is a Highly caloric snack.")
    if tC < 300 and fr > 50:
        print("It's a healthy snack!")
    if fl > 100 and fr < 20:
        print("This is an unhealthy snack.")


snackComputing(float(input("Please insert the amout of sugar in grams: \n")), float(input(
    "Please insert the amount of flour in grams: \n")), float(input("Please insert the amount of fruit in grams: \n")))
