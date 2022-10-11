import weather

filename = "w.dat"
weather_data = {}
choice = 0

while choice != 9:
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
    choice = 0
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program\n")
    choice = int(input("Enter menu choice: "))

    if choice == 1:
        filename = input("Enter data filename: ")
        weather_data = weather.read_data(filename)        
    elif choice == 2:
        date = input("Enter data (YYYYMMDD): ")
        time = input("Enter time (hhmmss): ")
        temp = int(input("Enter temperature: "))
        humid = int(input("Enter humidity: "))
        rainfall = float(input("Enter rainfall: "))
        weather_data[date+time] = {"t": temp, "h": humid, "r": rainfall}
        weather.write_data(weather_data, filename)
    elif choice == 3:
        date = input("Enter date (YYYYMMDD): ")
        daily_report = weather.report_daily(weather_data, date)
        print(daily_report)
    elif choice == 4:
        historical = weather.report_historical(weather_data)
        print(historical)
    elif choice == 9:
        break
            



