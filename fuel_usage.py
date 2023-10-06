#this is the main function that contains the inputs and out puts to display to user.
def main():
    str_odometer = float(input("Enter the first odometer reading (in miles): "))
    end_odometer = float(input("Enter the second odometer reading (in miles): "))
    fuel_used = float(input("Enter the amount os fuel usend (in gallons): "))

    #The invokation of others functions.
    miles_per_gallon = computing_fuel_efficiency(str_odometer, end_odometer, fuel_used)
    liters_per_100km = computing_liters_per_100km (miles_per_gallon)
    
    #The result of program goes here.
    print()
    print(f"{miles_per_gallon:.1f} miles per gallon.")
    print(f"{liters_per_100km:.2f} liter per 100 kilometers.")

#this funcion calculate the fuel efficiency
def computing_fuel_efficiency(str_odometer, end_odometer, fuel_used):
    efficiency = (end_odometer - str_odometer) / fuel_used
    return efficiency

#ths function calculate liters per 100 kilometers.
def computing_liters_per_100km(miles_per_gallon):
    liters_per_km = 235.215 / miles_per_gallon 
    return liters_per_km

main()