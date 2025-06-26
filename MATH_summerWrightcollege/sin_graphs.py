import math

def sin_graphs():
    print("--------sin graphs--------")
    print("")
    print("Analyze the sine function: y = A sin(B(x + C)) + D |=1")
    print("")
    print("Sine Function Analyzer: y = A * sin(Bx + C) + D |=2")
    print("")
    print("Sine Function Analyzer (Symbolic Input Allowed) |=3")
    print("")
    print("Sinusoidal Function Finder from Two X-Intercepts |=4")
    print("")
    print("Cosine Function Analyzer: y = A * cos(Bx + C) + D |=5")
    print("")
    print("Ferris Wheel Height Function Generator |=6")
    print("")
    print("Daily Temperature Model Generator |=7")
    print("")

    Q = int(input("type?-"))

    if Q == 1:
        import math
        print("")
        print("Analyze the sine function: y = A sin(B(x + C)) + D")
        print("---------------------------------------------------")

        A = int(input("A="))     
        B = int(input("B="))     
        C = int(input("C="))     
        D = int(input("D="))         

        amplitude = abs(A)
        period = (2 * math.pi) / B
        horizontal_shift = -C
        direction = "left" if horizontal_shift < 0 else "right"

        print("------ Results ------")
        print(f"Amplitude: {amplitude}")
        print(f"Period: {period:.3f}")
        print(f"Horizontal shift: {abs(horizontal_shift)} units to the {direction}")
        print(f"Midline: y = {D}")
    if Q == 2:
        from sympy import symbols, pi, sin, simplify, sympify, Abs
        print("")
        print("Sine Function Analyzer: y = A * sin(Bx + C) + D")
        print("-------------------------------------------------")

        A = sympify(input("Enter A (amplitude, e.g. 1): "))

        B_input = input("Enter B (multiplier on x, leave blank for 1): ")
        B = sympify(B_input) if B_input.strip() else 1

        C = sympify(input("Enter C (horizontal shift constant, e.g. pi/5): "))
        D = sympify(input("Enter D (vertical shift, e.g. 0): "))

        x = symbols('x')
        function = simplify(A * sin(B * x + C) + D)
        amplitude = Abs(A)

        if B == 0:
            period = "undefined (B=0)"
            phase_shift = "undefined (B=0)"
            direction = ""
        else:
            period = simplify((2 * pi) / Abs(B))
            phase_shift_val = simplify(-C / B)
            if phase_shift_val == 0:
                direction = "no horizontal shift"
                phase_shift = 0
            else:
                direction = "left" if phase_shift_val < 0 else "right"
                phase_shift = Abs(phase_shift_val)
        midline = D
        print("------ Results ------")
        print(f"Amplitude: {amplitude}")
        print(f"Period: {period}")

        if direction == "no horizontal shift":
            print("Phase shift: no horizontal shift")
        elif direction == "":
            print("Phase shift: undefined (B=0)")
        else:
            print(f"Phase shift: {phase_shift} units to the {direction}")
        print(f"Midline: y = {midline}")
        print(f"✅ Exact Function: f(x) = {function}")
    if Q == 3:
        print("")
        from sympy import symbols, pi, simplify, Abs

        print("Sine Function Analyzer (Symbolic Input Allowed)")
        print("------------------------------------------------")

        x = symbols('x')

        A = eval(input("A: "))
        B = simplify(input("B (e.g. 4*pi/3): "))
        C = simplify(input("C (e.g. 16*pi/3): "))
        D = eval(input("D: "))

        amplitude = Abs(A)
        period = simplify((2 * pi) / Abs(B))
        phase_shift = simplify(-C / B)
        direction = "left" if phase_shift < 0 else "right"

        print("------ Results ------")
        print(f"Amplitude: {amplitude}")
        print(f"Period: {period}")
        print(f"Horizontal shift: {Abs(phase_shift)} units to the {direction}")
        print(f"Midline: y = {D}")
    if Q == 4:
        print("")
        import math
        from sympy import symbols, pi, sin, simplify

        print("Sinusoidal Function Finder: f(x) = A * sin(B(x - h)) + D")
        print("----------------------------------------------------------")

        x1 = float(input("Enter the first x-intercept: "))
        x2 = float(input("Enter the second x-intercept: "))

        half_period = abs(x2 - x1)
        full_period = 2 * half_period
        midpoint = (x1 + x2) / 2

        B_exact = simplify(2 * pi / full_period)
        B_decimal = round((2 * math.pi) / full_period, 5)

        x = symbols('x')
        f_exact = sin(B_exact * (x - midpoint))     
        f_decimal_str = f"sin({B_decimal} * (x - ({midpoint})))"

        print("------ Results ------")
        print(f"Period: {full_period}")
        print(f"Midpoint (phase shift): {midpoint}")
        print(f"Frequency: {B_exact} or ≈ {B_decimal}")
        print(f"✅ Exact Function:")
        print(f"f(x) = {f_exact}")
        print(f"✅ Decimal Approximation:")
        print(f"f(x) = {f_decimal_str}")
    if Q == 5:
        print("")
        from sympy import symbols, pi, cos, simplify, sympify, Abs
        print("Cosine Function Analyzer: y = A * cos(Bx + C) + D")
        print("---------------------------------------------------")

        A = sympify(input("Enter A (amplitude): "))

        B_input = input("Enter B (frequency multiplier — leave blank for 1): ")
        B = sympify(B_input) if B_input.strip() else 1

        C = sympify(input("Enter C (horizontal shift constant): "))
        D = sympify(input("Enter D (vertical shift): "))

        amplitude = Abs(A)
        period = simplify((2 * pi) / Abs(B))
        phase_shift = simplify(-C / B)
        direction = "left" if phase_shift < 0 else "right"
        midline = D

        x = symbols('x')
        function = simplify(A * cos(B * x + C) + D)

        print("------ Results ------")
        print(f"Amplitude: {amplitude}")
        print(f"Period: {period}")
        print(f"Phase shift: {Abs(phase_shift)} units to the {direction}")
        print(f"Midline: y = {midline}")
        print(f"✅ Exact Function: f(x) = {function}")
    if Q == 6:
        print("")
        from sympy import symbols, pi, cos, simplify, sympify
        print("Ferris Wheel Height Function Generator")
        print("-------------------------------------------")

        diameter = sympify(input("Enter the diameter of the Ferris wheel (in meters): "))
        platform = sympify(input("Enter the platform height from the ground (in meters): "))
        period = sympify(input("Enter the time for one full revolution (in minutes): "))

        radius = diameter / 2
        amplitude = -radius  
        B = simplify((2 * pi) / period)
        D = platform + radius  
        t = symbols('t')
        h = simplify(amplitude * cos(B * t) + D)

        print("Modeled Height Function:")
        print(f"h(t) = {h}")
        print(f"Where:")
        print(f"  - Amplitude = {abs(amplitude)} (radius)")
        print(f"  - Period = {period} minutes")
        print(f"  - Midline = {D} meters (average height)")
        print(f"  - Starts at bottom (6 o'clock position)")
    if Q == 7:
        print("")
        from sympy import symbols, pi, cos, sin, simplify, sympify
        print("Daily Temperature Model Generator")
        print("-------------------------------------------")

        T_mid = sympify(input("Enter the temperature at t=0 (midpoint between low/high): "))
        T_low = sympify(input("Enter the daily low temperature: "))
        T_high = sympify(input("Enter the daily high temperature: "))
        period = sympify(input("Enter the period (hours; e.g., 24): "))

        A = (T_high - T_low) / 2            
        D_mid = (T_high + T_low) / 2       
        B = simplify(2 * pi / period)      

        C = -pi/2

        t = symbols('t')
        D = simplify(A * cos(B * t + C) + D_mid)

        D_sin = simplify(-A * sin(B * t) + D_mid)

        print("Cosine-based model:")
        print(f"D(t) = {D}")
        print("Equivalent sine-based model:")
        print(f"D(t) = {D_sin}")

        print("Where:")
        print(f"  • Amplitude A = {A}")
        print(f"  • Period = {period} hours")
        print(f"  • Midline = {D_mid}°")
        print(f"  • Phase shift C = {C} rad (cosine) → starts at midpoint decreasing")
    if Q == 8:
        print("")

sin_graphs()