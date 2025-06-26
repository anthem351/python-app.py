import math

def ITF():
    print("--------Inverse trig fuctions--------")
    print("")
    print("Inverse Sine Calculator (Radians) |=1")
    print("")
    print("Inverse Cosine Calculator with Custom Interval |=2")
    print("")
    print("Inverse Tangent Calculator with Custom Interval |=3")
    print("")
    Q = int(input("type?-"))

    if Q == 1:
        print("")
        from sympy import symbols, sin, asin, sqrt, pi, simplify, sympify, Abs
        print("Inverse Sine Calculator with Custom Interval")
        print("------------------------------------------------")

        value_input = input("Enter the sine value (e.g. sqrt(2)/2 or -1/2): ")
        value = sympify(value_input)

        lower_bound = sympify(input("Enter the lower bound of the interval (e.g. 0, -pi/2): "))
        upper_bound = sympify(input("Enter the upper bound of the interval (e.g. pi, pi/2): "))

        reference_angle = simplify(Abs(asin(Abs(value))))

        if value >= 0:
            angle = reference_angle
        else:
           
            if lower_bound >= 0:
                angle = simplify(pi - reference_angle)
            else:
                angle = simplify(-reference_angle)

        if not (lower_bound <= angle <= upper_bound):
            print("⚠️ The calculated solution is not within the provided interval.")
        else:
            print("Solution within the interval:")
            print(f"sin^(-1)({value}) = {angle} radians")
    if Q == 2:
        print("")
        from sympy import symbols, cos, acos, sqrt, pi, simplify, sympify, Abs

        print("Inverse Cosine Calculator with Custom Interval")
        print("--------------------------------------------------")

        value_input = input("Enter the cosine value (e.g. sqrt(3)/2 or -1/2): ")
        value = sympify(value_input)

        lower_bound = sympify(input("Enter the lower bound of the interval (e.g. 0, -pi/2): "))
        upper_bound = sympify(input("Enter the upper bound of the interval (e.g. pi, pi/2): "))

        reference_angle = simplify(Abs(acos(Abs(value))))

        if value >= 0:
            angle = reference_angle
        else:
           
            if lower_bound >= 0:
                angle = simplify(pi - reference_angle)
            else:
                angle = simplify(-reference_angle)

        if not (lower_bound <= angle <= upper_bound):
            print("⚠️ The calculated solution is not within the provided interval.")
        else:
            print("Solution within the interval:")
            print(f"cos^(-1)({value}) = {angle} radians")
    if Q == 3:
        print("")
        from sympy import symbols, tan, atan, sqrt, pi, simplify, sympify
        print("Inverse Tangent Calculator with Custom Interval")
        print("---------------------------------------------------")

        value_input = input("Enter the tangent value (e.g. sqrt(3), -1, 0): ")
        value = sympify(value_input)

        lower_bound = sympify(input("Enter the lower bound of the interval (e.g. -pi/2, 0): "))
        upper_bound = sympify(input("Enter the upper bound of the interval (e.g. pi/2, pi): "))

        principal_angle = simplify(atan(value))

        angle = principal_angle

        while angle < lower_bound:
            angle += pi
        while angle > upper_bound:
            angle -= pi

        if not (lower_bound <= angle <= upper_bound):
            print("⚠️ The calculated solution is not within the provided interval.")
        else:
            print("Solution within the interval:")
            print(f"tan^(-1)({value}) = {angle} radians")
    if Q == 4:
        print("")
        from sympy import acos, sympify, N

        value_input = '0.9'
        value = sympify(value_input)

        principal_angle = acos(value)

        decimal_result = N(principal_angle, 5)

        print("Result:")
        print(f"cos^(-1)({value}) ≈ {decimal_result} radians")

ITF()