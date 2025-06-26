import math

def RTT():
    print("--------Right triangle trigonometry--------")
    print("")
    print("Suppose a = # and b = #. |=1")
    print("")
    print("Suppose a = # and A = # degrees. |=2")
    print("")
    print("Suppose c = # and A = # degrees. |=3")
    print("")
    print("Ladder Height Calculator. |=4")
    print("")
    print("Building Height from Angle of Elevation |=5")
    print("")
    print("Radio Tower Height Calculator |=6")
    print("")
    print("Ship Distance from Lighthouse Calculator |=7")
    print("")
    print("Solve for x in a triangle using Law of Sines |=8")
    print("")
    Q = int(input("what type?-"))

    if Q == 1:
        print("")
        import math
        from sympy import Rational, sqrt, nsimplify

        print("Right Triangle Trig Function Calculator (Angle A)")
        print("--------------------------------------------------")

        a = float(input("Enter side a (opposite A): "))
        b = float(input("Enter side b (adjacent to A): "))

        c = math.sqrt(a**2 + b**2)

        a_sym = Rational(a)
        b_sym = Rational(b)
        c_sym = sqrt(a_sym**2 + b_sym**2)

        sin_A = a_sym / c_sym
        cos_A = b_sym / c_sym
        tan_A = a_sym / b_sym
        csc_A = c_sym / a_sym
        sec_A = c_sym / b_sym
        cot_A = b_sym / a_sym

        print("\n------ Results ------")
        print(f"sin(A) = {sin_A} ≈ {float(sin_A):.4f}")
        print(f"cos(A) = {cos_A} ≈ {float(cos_A):.4f}")
        print(f"tan(A) = {tan_A} ≈ {float(tan_A):.4f}")
        print(f"sec(A) = {sec_A} ≈ {float(sec_A):.4f}")
        print(f"csc(A) = {csc_A} ≈ {float(csc_A):.4f}")
        print(f"cot(A) = {cot_A} ≈ {float(cot_A):.4f}")
    if Q == 2:
        print("")
        import math
        print("Right Triangle Solver: Given a and ∠A")
        print("--------------------------------------")
        a = float(input("Enter side a (opposite angle A): "))
        A_deg = float(input("Enter angle A (in degrees): "))
        A_rad = math.radians(A_deg)

        c = a / math.sin(A_rad)         
        b = c * math.cos(A_rad)         
        B_deg = 90 - A_deg              

        print("------ Results ------")
        print(f"b = {b:.3f}")
        print(f"c = {c:.3f}")
        print(f"B = {B_deg:.3f} degrees")
    if Q == 3:
        print("")
        import math
        print("Right Triangle Solver: Given c and ∠A")
        print("--------------------------------------")

        c = float(input("Enter hypotenuse c: "))
        A_deg = float(input("Enter angle A (in degrees): "))
        A_rad = math.radians(A_deg)

        a = c * math.sin(A_rad)
        b = c * math.cos(A_rad)
        B_deg = 90 - A_deg

        print("------ Results ------")
        print(f"a = {a:.3f}")
        print(f"b = {b:.3f}")
        print(f"B = {B_deg:.3f} degrees")
    if Q == 4:
        print("")
        import math
        print("Ladder Height Calculator")
        print("------------------------")

        ladder_length = float(input("Enter ladder length (ft): "))
        angle_deg = float(input("Enter angle with the ground (degrees): "))

        angle_rad = math.radians(angle_deg)

        height = ladder_length * math.sin(angle_rad)

        print("------ Result ------")
        print(f"The ladder reaches approximately {height:.3f} ft up the building.")
    if Q == 5:
        print("")
        import math
        print("Building Height from Angle of Elevation")
        print("----------------------------------------")

        distance_miles = float(input("Enter distance from building (in miles): "))
        angle_deg = float(input("Enter angle of elevation (degrees): "))

        angle_rad = math.radians(angle_deg)

        height_miles = distance_miles * math.tan(angle_rad)

        height_feet = height_miles * 5280

        print("------ Result ------")
        print(f"Estimated height of the building: {height_feet:.2f} feet")
    if Q == 6:
        print("")
        import math
        print("Radio Tower Height Calculator")
        print("-----------------------------")

        distance = float(input("Enter horizontal distance from building to tower (feet): "))
        angle_elevation_deg = float(input("Enter angle of elevation to top (degrees): "))
        angle_depression_deg = float(input("Enter angle of depression to bottom (degrees): "))

        angle_elevation_rad = math.radians(angle_elevation_deg)
        angle_depression_rad = math.radians(angle_depression_deg)

        height_above = distance * math.tan(angle_elevation_rad)
        height_below = distance * math.tan(angle_depression_rad)

        total_height = height_above + height_below

        print("------ Result ------")
        print(f"Estimated height of the tower: {total_height:.2f} feet")
    if Q == 7:
        print("")
        import math

        print("Ship Distance from Lighthouse Calculator")
        print("----------------------------------------")

        height = float(input("Enter height of the lighthouse (in feet): "))
        angle_deg = float(input("Enter angle of depression (in degrees): "))

        angle_rad = math.radians(angle_deg)

        distance = height / math.tan(angle_rad)

        print("------ Result ------")
        print(f"Distance from ship to lighthouse base: {distance:.2f} feet")
    if Q == 8:
        print("")
        import math
        print("Solve for x in a triangle using Law of Sines")
        print("--------------------------------------------")

        height = float(input("Enter the height (opposite side to angle A): "))
        angle_A_deg = float(input("Enter angle A (degrees): "))
        angle_B_deg = float(input("Enter angle B (degrees): "))

        angle_C_deg = 180 - angle_A_deg - angle_B_deg

        angle_A_rad = math.radians(angle_A_deg)
        angle_B_rad = math.radians(angle_B_deg)
        angle_C_rad = math.radians(angle_C_deg)

        x = (height * math.sin(angle_B_rad)) / math.sin(angle_C_rad)

        print("------ Result ------")
        print(f"x = {x:.2f} units")


RTT()