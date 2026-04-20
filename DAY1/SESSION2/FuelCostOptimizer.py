def fuelCostOptimiser(distance, mileage, fuel_price, toll, daily_wage, budget):
    fuel_cost = distance / mileage * fuel_price
    days = distance // 500;
    driver_cost = daily_wage * days
    total_trip_cost = fuel_cost + driver_cost + toll

    if total_trip_cost > budget:
        print("OVER BUDGET by: ",(total_trip_cost - budget))
    else:
        print("WITHIN BUDGET, savings: ", (budget - total_trip_cost))

#fuelCostOptimiser(distance=1000, mileage=10, fuel_price=100, toll=500, ddw=800, budget=15000)
#fuelCostOptimiser(distance=2000, mileage=8, fuel_price=105, toll=1000, daily_wage=900, budget=30000)

distance = int(input("Enter the Distance: "))
mileage = int(input("Enter the Mileage: "))
fuel_price = int(input("Enter the fuel_price: "))
toll = int(input("Enter the Toll price: "))
daily_wage = int(input("Enter the daily_wage: "))
budget = int(input("Enter the budget: "))

fuelCostOptimiser(distance, mileage, fuel_price, toll, daily_wage, budget)

