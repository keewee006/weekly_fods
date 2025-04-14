def add_daily_temp(temp_dict, day, temp):
    if day not in temp_dict:
        temp_dict[day] = temp
    return temp_dict

temps = {}
print(add_daily_temp(temps, "sunday", 25))
print(add_daily_temp(temps, "Monday", 30))
