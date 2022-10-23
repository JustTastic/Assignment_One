# Question 3
def q3():
    print("Question 3")
    insurance_money = int(input("Enter Insurance Cost: "))
    min_insu = 0.8
    repl_cost = insurance_money * min_insu
    print("the minimum amount of insurance is: ", repl_cost)


# Question 5
def q4():
    print("Question 5")
    actual_property = int(input("Enter Property: "))
    property_tax = 0.6
    assesment_value = actual_property * property_tax
    print(assesment_value)


# Question 6
def q5():
    print("Question 6")
    fat_grams = int(input("Enter Fat Eaten: "))
    carbs_grams = int(input("Enter Carb Eaten: "))

    cal_from_fat = fat_grams * 9
    cal_from_carb = carbs_grams * 4

    print(f"Caloris from fat are: {cal_from_fat}, and Caloris from Carbs are: {cal_from_carb}")

# Question 7
def q6():
    print("Question 7")
    class_a = int(input("Enter total Class A seats: "))
    class_b = int(input("Enter total Class B seats: "))
    class_c = int(input("Enter total Class C seats: "))

    total_seats = class_a + class_b + class_c
    total_income = (class_a * 20) + (class_b * 15) + (class_c * 10)
    print(f"Total Class A seats: {class_a}, Total Class B seats: {class_b}, Total Class C seats: {class_c}")
    print(f"Total Income is: {total_income}")

# Question 8
def q8():
    print("Question 8")


# Question 9
def q9():
    print("Question 9")
    monthly_sale_tax = int(input("Enter Monthly Sales tax: "))
    country_sale_tax = monthly_sale_tax * 0.05
    state_sale_tax = monthly_sale_tax * 0.025

    total_sale_tax = country_sale_tax + state_sale_tax
    print(f"Country sale tax: {country_sale_tax}, State Sale tax: {state_sale_tax}")
    print(f"Total Sale tax: {total_sale_tax}")


# Question 10
def feet_to_inches(feet : int):
    print("Question 10")
    inch = feet / 12
    return inch

result = feet_to_inches(1200)
print(round(result, 1))


# Question 11
def q11():
    print("Question 11")
    import random
    qs = 0

    while qs <= 5:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print(f"{num1} + {num2} = ",num1 + num2)
        qs += 1


# Question 12
def MAX(num1, num2):
    print("Question 12")
    if num1 > num2:
        print("Number 1 is greater ",num1)
    else:
        print("Number 2 is greater ",num2)

result = MAX(1, 32)

import random
# Question 16
def random_Counter():
    print("Question 16")
    even_num = 0
    odd_num = 0
    for i in range(1, 101):
        rand_num = random.randint(1, 100)
        if rand_num % 2 == 0:
            even_num += 1
            print(rand_num)
        else:
            odd_num += 1
            print(rand_num)
    print("Total Even Number is: ", even_num, " Total Odd Number is: ", odd_num)


result = random_Counter()