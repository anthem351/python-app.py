import math

def angles():
    print("--------angles--------")
    print("")
    print("Convert the angle # to radians. Give the exact value and use pi |=1")
    print("")
    print("Convert the angle #pi/# from radians to degrees. |=2")
    print("")
    print("The angle between 0 and 360 that is coterminal with the #### |=3")
    print("")
    print("The angle between 0 and 2pi in radians that is coterminal with the angle #/#pi in radians is |=4")
    print("")
    print("Calculate arc length given radius and central angle in radians |=5")
    print("")
    print("Calculate arc length on Earth given angle in minutes |=6")
    print("")
    print("Find the angle in radians given arc length and radius |=7")
    print("")
    print("Calculate the area of a sector (angle in degrees) |=8")
    print("")
    print("Calculate arc length given radius and angle in degrees |=9")
    print("")
    q = int(input("what type?-"))
    if q == 1:
        print("")
        print("Convert the angle # to radians. Give the exact value and use pi |=1")
        import math
        print("Convert degrees to radians (exact and decimal)")
        print("---------IF THE NUMBER IS POSITIVE---------")
        print("count how many 45 degress are in the #, then put the number of 45's into #*pi/4")
        N = int(input("input degrees:"))
        print("")
        if N > 0:
            T = 0
            while N >= 45:
                N = N - 45
                print(str(N))
                T = T + 1
            print("45 degrees removed:"+str(T))
    if q == 2:
        print("")
        import math
        print("Convert the angle #pi/# from radians to degrees.")
        numerator = float(input("Enter numerator (e.g. 4 for 4π/3): "))
        denominator = float(input("Enter denominator (e.g. 3 for 4π/3): "))
        radians = (numerator / denominator) * math.pi
        degrees = math.degrees(radians)
        print("------ Results ------")
        print(f"Radians: ({numerator}π/{denominator})")
        print(f"Degrees: {round(degrees, 3)}°")
    if q == 3:
        print("")
        print("The angle between 0 and 360 that is coterminal with the ####")
        N = int(input("input degrees:"))
        print("")
        if N > 0:
            T = 0
            while N >= 360:
                N = N - 360
                print(str(N))
                T = T + 1
        elif N < 0:
            T = 0
            while N <= 360:
                N = N + 360
                print(str(N))
                T = T + 1
            print("")
            while N >= 360:
                N = N - 360
                print(str(N))
                T = T + 1

        print("")
        print("amount of 360's removed / rotations ="+str(T))
        print("the coterminal:"+str(N))
    if q == 4:
        print("")
        print("The angle between 0 and 2pi in radians that is coterminal with the angle #/#pi in radians is")
        import math

        print("Find coterminal angle in [0, 2π) for angle aπ/b")
        numerator = int(input("Enter numerator (e.g. 55): "))
        denominator = int(input("Enter denominator (e.g. 8): "))
        theta = (numerator / denominator) * math.pi
        coterminal = theta % (2 * math.pi)
        pi_multiple = coterminal / math.pi
        print("------ Results ------")
        print("Original angle: ("+str(numerator)+"π/"+str(denominator)+") radians")
        print("Decimal radians: "+str(round(theta, 3)))
        print("Coterminal angle: "+str(round(pi_multiple, 3))+"π radians")
    if q == 5:
        print("")
        print("Calculate arc length given radius and central angle in radians")
        radius = float(input("Enter radius (in miles): "))
        angle = float(input("Enter central angle (in radians): "))
        arc_length = radius * angle
        print("------ Results ------")
        print("Arc Length = "+str(radius)+" × "+str(angle)+" = "+str(arc_length)+" miles")
    if q == 6:
        print("")
        import math
        print("Calculate arc length on Earth given angle in minutes")
        radius = 3960  # miles
        minutes = float(input("Enter angle in minutes: ")) 
        degrees = minutes / 60
        radians = math.radians(degrees)
        arc_length = radius * radians
        print("------ Results ------")
        print("Angle: "+str(minutes)+" minutes = "+str(round(radians, 6))+" radians")
        print("Arc Length: "+str(round(arc_length, 3))+" miles")
    if q == 7:
        print("")
        import math
        print("Find central angle in both radians and degrees")
        arc_length = float(input("Enter arc length (in feet): "))
        radius = float(input("Enter radius (in feet): "))
        theta_radians = arc_length / radius
        theta_degrees = math.degrees(theta_radians)
        print("------ Results ------")
        print("Angle in radians (exact): "+str(arc_length)+"/"+str(radius)+" radians")
        print("Angle in radians (decimal): "+str(round(theta_radians, 4))+" rad")
        print("Angle in degrees (decimal): "+str(round(theta_degrees, 2)))
    if q == 8:
        print("")
        import math
        print("Calculate the area of a sector (angle in degrees)")
        radius = float(input("Enter radius (in yards): "))
        angle_deg = float(input("Enter central angle (in degrees): "))
        area = (angle_deg / 360) * math.pi * radius**2
        print("\n------ Results ------")
        print("Exact Area: ("+str(angle_deg)+"/360) × π × "+str(radius)+"²")
        print("Approximate Area: "+str(round(area, 3))+" square yards")
    if q == 9:
        print("")
        import math
        print("Calculate arc length given radius and angle in degrees")
        radius = float(input("Enter radius: "))
        angle_deg = float(input("Enter central angle (in degrees): "))
        arc_length = (angle_deg / 360) * (2 * math.pi * radius)
        print("------ Results ------")
        print("Arc Length ≈ "+str(round(arc_length, 2))+" units")
    if q == 10:
        print("")
        import math
        print("Find how far Earth travels in one day around the Sun")
        radius = 93 
        days_in_year = 365
        circumference = 2 * math.pi * radius 
        daily_distance = circumference / days_in_year
        print("------ Results ------")
        print("Total orbit distance (1 year): "+str(round(circumference, 3))+" million miles")
        print("Distance per day: "+str(round(daily_distance, 1))+" million miles")


angles()