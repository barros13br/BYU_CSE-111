from datetime import datetime
#Main function
def main():
    gender = input("Enter your gender (M or F): ")
    birth = input("Enter your Birthdate (YYYY-MM-DD): ")
    weight = float(input("Enter your weight (lb): "))
    height = float(input("Enter your height (in): "))

    years = age(birth)
    weight_in_kg = weight_kg(weight)
    height_in_cm = height_cm(height)
    Body_mass_index = bmi(weight_in_kg, height_in_cm)
    Basal_metabolic_rate = bmr(gender, weight_in_kg, height_in_cm, years, birth)

    print()
    print(f"Age (years): {years}")
    print(f"Weight (kg): {weight_in_kg:.2f}")
    print(f"Height (cm):{height_in_cm:.1f}")
    print(f"Body mass index: {Body_mass_index:.1f}")
    print(f"Basal metabolic rate (Kcal/day): {Basal_metabolic_rate:.0f}")

#Converting string to a date object and substracting years.
def age(birth):
    birthdate =  datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1
    return years

#changing lb to kg.
def weight_kg(weight):
    lb_to_kg = weight * 0.45359237
    return lb_to_kg

#Changing in to cm.
def height_cm(height):
    in_to_cm = height * 2.54
    return in_to_cm

#It calculate Body mass index.
def bmi(weight_kg, height_cm):
    bmi_math = 10000 * weight_kg / (height_cm ** 2) 
    return bmi_math

#it calculate Basal metabolic rate. 
def bmr(gender, weight_kg, height_cm, years, birth):
    years = age(birth)
    if gender.upper() == "M":
        bmr_math = 88.362 + 13.397 * weight_kg + 4.799 * height_cm - 5.677 * years
    else:
        bmr_math = 447.593 + 9.247 * weight_kg + 3.098 * height_cm - 4.330 * years
    return bmr_math

main()