import math

def GOTOTF():
    print("--------Graphs of the other trig fuctions--------")
    print("")
    print("Tangent Function Analyzer: y = A * tan(Bx + C) + D |=1")
    print("")
    print("Secant Function Analyzer: y = A * sec(Bx + C) + D |=2")
    print("")
    print("Cosecant Function Analyzer: y = A * csc(Bx + C) + D |=3")
    print("")
    print("Simplify Any Trig Expression |=4")
    print("")
    print("Identify the function whose graph appears above. |=5")
    print("")


    Q = int(input("type?-"))


    if Q == 1:
        from sympy import symbols, pi, tan, simplify, sympify, Abs
        print("")
        print("Tangent Function Analyzer: y = A * tan(Bx + C) + D")
        print("--------------------------------------------------------")

        A = sympify(input("Enter A (stretch factor): "))
        B_input = input("Enter B (multiplier on x, leave blank for 1): ")
        B = sympify(B_input) if B_input.strip() else 1
        C = sympify(input("Enter C (horizontal shift constant): "))
        D = sympify(input("Enter D (vertical shift, e.g. 0): "))

        x = symbols('x')
        function = simplify(A * tan(B * x + C) + D)

        if B != 0:
            period = simplify(pi / Abs(B))
        else:
            period = "undefined (B=0)"

        if B != 0:
            phase_shift_val = simplify(-C / B)
            direction = "left" if phase_shift_val < 0 else "right"
            phase_shift = Abs(phase_shift_val)
        else:
            phase_shift = "undefined (B=0)"
            direction = ""

        print("Function Summary:")
        print(f"y = {function}")
        print(f"• Period: {period}")
        print(f"• Phase shift: {phase_shift} units to the {direction}" if direction else f"• Phase shift: {phase_shift}")
        print(f"• Vertical shift: {D}")
        print("• Amplitude: N/A (tangent has no amplitude)")
    if Q == 2:
        print("")
        from sympy import symbols, pi, sec, simplify, sympify, Abs
        print("Secant Function Analyzer: y = A * sec(Bx + C) + D")
        print("------------------------------------------------------")

        A = sympify(input("Enter A (vertical stretch factor): "))
        B_input = input("Enter B (multiplier on x, leave blank for 1): ")
        B = sympify(B_input) if B_input.strip() else 1
        C = sympify(input("Enter C (horizontal shift constant): "))
        D = sympify(input("Enter D (vertical shift): "))

        x = symbols('x')
        function = simplify(A * sec(B * x + C) + D)

        if B != 0:
            period = simplify((2 * pi) / Abs(B))
            phase_shift_val = simplify(-C / B)
            direction = "left" if phase_shift_val < 0 else "right"
            phase_shift = Abs(phase_shift_val)
        else:
            period = "undefined (B=0)"
            phase_shift = "undefined (B=0)"
            direction = ""

        print("Function Analysis:")
        print(f"y = {function}")
        print(f"• Period: {period}")
        print(f"• Phase shift: {phase_shift} units to the {direction}" if direction else f"• Phase shift: {phase_shift}")
        print(f"• Vertical shift: {D}")
        print("• Amplitude: N/A (secant has no amplitude)")
    if Q == 3:
        print("")
        from sympy import symbols, pi, csc, simplify, sympify, Abs
        print("Cosecant Function Analyzer: y = A * csc(Bx + C) + D")
        print("--------------------------------------------------------")

        A = sympify(input("Enter A (vertical stretch factor): "))
        B = sympify(input("Enter B (coefficient of x, e.g., 11*pi/6): "))
        C = sympify(input("Enter C (constant inside csc, e.g., -11*pi/2): "))
        D = sympify(input("Enter D (vertical shift): "))

        x = symbols('x')
        function = simplify(A * csc(B * x + C) + D)

        if B != 0:
            period = simplify((2 * pi) / Abs(B))
            phase_shift_val = simplify(-C / B)
            direction = "left" if phase_shift_val < 0 else "right"
            phase_shift = Abs(phase_shift_val)
        else:
            period = "undefined (B=0)"
            phase_shift = "undefined (B=0)"
            direction = ""

        print("Function Analysis:")
        print(f"y = {function}")
        print(f"• Period: {period}")
        print(f"• Phase shift: {phase_shift} units to the {direction}" if direction else f"• Phase shift: {phase_shift}")
        print(f"• Vertical shift: {D}")
        print("• Amplitude: N/A (cosecant has no amplitude)")
    if Q == 4:
        print("")
        from sympy import symbols, sin, cos, tan, csc, sec, cot, simplify, trigsimp, sympify

        print("Simplify Any Trigonometric Expression")
        print("----------------------------------------")

        x = symbols('x')

        expr_input = input("Enter a trig expression in x (e.g. -sin(x) - cos(x)/tan(x)): ")

        try:
            expr = sympify(expr_input)
            simplified_expr = trigsimp(simplify(expr))

            print("\n🔢 Original Expression:")
            print(expr)
            print("\n✅ Simplified Expression:")
            print(simplified_expr)

        except Exception as e:
            print("Error parsing the expression:")
            print(e)
    if Q == 5:
        print("")
GOTOTF()