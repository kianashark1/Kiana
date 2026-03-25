# Define the list of all cars
cars = [
    ["A1", "Hundai Accent WRC", 220, "221,300", 5500, 5.4, 1998, 4],
    ["B4", "VW Golf Kit Car", 220, "191,260", 8000, 6.2, 1998, 4],
    ["E1", "Mitibushi Carisma GT", 225, "213,290", 6000, 5.2, 1996, 4],
    ["B3", "Toyota Corolla WRC", 210, "220,299", 5700, 5.4, 1972, 4],
    ["D3", "Seat Toledo Marathon", 220, "195,330", 2100, 5.2, 2100, 5],
    ["C1", "Subaru Impreza WRC", 220, "215,315", 5500, 5.4, 1994, 4],
    ["F4", "PRD Racing Team", 200, "125,170", 6500, 5.4, 2700, 6],
    ["G2", "Seat Ibiza GTi", 220, "205,280", 8400, 6.5, 1984, 4],
    ["A2", "Ford Focus WRC", 224, "221,300", 5400, 5.5, 1995, 4],
    ["F3", "Renault Megane", 218, "198,270", 8400, 5.9, 1995, 4],
    ["D4", "Peugeot 206 WRC", 225, "221,300", 5600, 5.4, 1996, 4]
]

selected_cars = [
    ["D3", "Seat Toledo Marathon", 220, "195,330", 2100, 5.2, 2100, 5],
    ["F4", "PRD Racing Team", 200, "125,170", 6500, 5.4, 2700, 6],
    ["B3", "Toyota Corolla WRC", 210, "220,299", 5700, 5.4, 1972, 4],
    ["E1", "Mitibushi Carisma GT", 225, "213,290", 6000, 5.2, 1996, 4],
    ["C1", "Subaru Impreza WRC", 220, "215,315", 5500, 5.4, 1994, 4],
    ["A1", "Hundai Accent WRC", 220, "221,300", 5500, 5.4, 1998, 4],
    ["G2", "Seat Ibiza GTi", 220, "205,280", 8400, 6.5, 1984, 4]
]

def print_car(c):
    print(f"Code: {c[0]}")
    print(f"Car Model: {c[1]}")
    print(f"Top Speed: {c[2]} km/h")
    print(f"Power: {c[3]} HP")
    print(f"Weight: {c[4]} kg")
    print(f"0-100 km/h: {c[5]} seconds")
    print(f"Engine Capacity: {c[6]} cc")
    print(f"Cylinders: {c[7]}")
    print()

i = 1
for c in cars:
    print(i,c[1])
    i= i+1


input("Which car would you like to choose?")
1
choice = int(input()) - 1
print_car(cars[choice])










