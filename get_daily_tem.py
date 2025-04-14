def get_daily_temps():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    temps = {}
    for day in days:
        temp = float(input(f"Enter temperature for {day}: "))
        temps[day] = temp
    return temps

daily_temps = get_daily_temps()
print(daily_temps)
