print("Py-fest 2026 Stage Manager")
print("1. View Lineup and Total Time")
print("2. Add a New Band")
print("3. Move a First Band to End (Late Arrival)")
print("4.Remove a Band By Name")
print("5. Move Band to End (late arrivals)")
print("6. Exit")

total_time = 0  
lineup = []     
choice = input("Select an option 1-6: ")

if choice == "1":
    print(f"Lineup: {', '.join(lineup) if lineup else 'No bands in the lineup'}")
    print(f"Total time: {total_time} minutes")
elif choice == "2":
    try:
        band_name = input("Enter the name of the new band: ")
        duration = int(input(f"Enter the duration of {band_name}'s performance in minutes: "))
        lineup.append(band_name)
        total_time += duration
        print(f"Band '{band_name}' added. Total time updated: {total_time} minutes")
    except ValueError:
        print("Invalid duration entered. Please enter a valid number.")
elif choice == "3":
    if lineup:
        band_name = lineup.pop(0) 
        lineup.append(band_name)  
        print(f"Band '{band_name}' moved to the end of the lineup.")
    else:
        print("No bands in the lineup to move.")
elif choice == "4":
    band_name = input("Enter the name of the band to remove: ")
    if band_name in lineup:
        lineup.remove(band_name)
        print(f"Band '{band_name}' removed from the lineup.")
    else:
        print(f"Band '{band_name}' not found in the lineup.")
elif choice == "5":
    band_name = input("Enter the name of the band to move to the end: ")
    if band_name in lineup:
        lineup.remove(band_name)
        lineup.append(band_name)
        print(f"Band '{band_name}' moved to the end of the lineup.")
    else:
        print(f"Band '{band_name}' Your band has been added to the end of the lineup.")
elif choice == "6":
    print("Exiting the program. Goodbye!")
else:
    print("Invalid option. Please select a number between 1 and 6.")

