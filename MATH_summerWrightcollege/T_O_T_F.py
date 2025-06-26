import math

def TOTF():
    print("--------The other trigonometric fuctions--------")
    print("")
    print("cos, sec, sin, and more calculator |=1")
    print("")
    print("Trig Identity Calculator from sin(θ) and quadrant |=2")
    print("")
    print("Trig Calculator from tan(θ) and quadran |=3")
    print("")
    print("Trig Expression Simplifier |=4")
    print("")




    Q = int(input("what type?-"))

    if Q == 1:
        print("")
        print("--------cos, sec, sin, and more calculator--------")
        print("")
        print("cos |=1")
        print("")
        print("cot |=2")
        print("")
        print("sin |=3")
        print("")
        print("sec |=4")
        print("")
        print("tan |=5")
        print("")
        print("csc |=6")
    
        q = int(input("what problem?-"))

        if q == 1:
            import math
            print("Exact Cosine Calculator")
            print("------------------------------------")
            print("Enter angle in terms of π (e.g. 7*pi/2, -3*pi, 0)")
            from sympy import cos, pi, sympify, simplify
            angle = input("θ = ") 

            try:
                theta = sympify(angle)
                result = simplify(cos(theta))
                print(f"cos({angle}) = {result}")
            except:
                print("⚠️ Invalid input.")
        if q == 2:
            print("")
            print("Exact Cotangent Calculator (Symbolic)")
            print("-------------------------------------")
            print("Enter angle in terms of π (e.g. 7*pi/2, -3*pi, 0)")
            from sympy import tan, pi, sympify, simplify
            angle = input("θ = ")

            try:
                theta = sympify(angle)
                tan_val = tan(theta)
                if tan_val == 0:
                    print(f"cot({angle}) is undefined")
                else:
                    result = simplify(1 / tan_val)
                    print(f"cot({angle}) =", result)
            except:
                print("⚠️ Invalid input.")
        if q == 3:
            print("")
            from sympy import sin, pi, sympify, simplify
            print("Exact Sine Calculator (Symbolic)")
            print("--------------------------------")
            print("Enter angle in terms of π (e.g. 7*pi/2, -3*pi, 0)")
            angle = input("θ = ") 

            try:
                theta = sympify(angle)
                result = simplify(sin(theta))
                print(f"sin({angle}) = {result}")
            except Exception as e:
                print("⚠️ Invalid input.")
        if q == 4:
            print("")
            from sympy import cos, pi, sympify, simplify

            print("Exact Secant Calculator (Symbolic)")
            print("----------------------------------")
            print("Enter angle in terms of π (e.g. 7*pi/2, -3*pi, 0)")
            angle = input("θ = ")  # e.g. 5*pi/4

            try:
                theta = sympify(angle)
                cos_val = cos(theta)
                if cos_val == 0:
                    print(f"sec({angle}) is undefined")
                else:
                    result = simplify(1 / cos_val)
                    print(f"sec({angle}) =", result)
            except:
                print("⚠️ Invalid input.")
        if q == 5:
            print("")
            print("Exact Tangent Calculator (Symbolic)")
            print("-----------------------------------")
            print("Enter angle in terms of π (e.g. 7*pi/2, -3*pi, 0)")
            from sympy import tan, pi, sympify, simplify
            angle = input("θ = ") 

            try:
                theta = sympify(angle)
                result = simplify(tan(theta))
                print(f"tan({angle}) =", result)
            except:
                print("⚠️ Invalid input.")
        if q == 6:
            print("")
            from sympy import sin, pi, sympify, simplify

            print("Exact Cosecant Calculator (Symbolic)")
            print("------------------------------------")
            print("Enter angle in terms of π (e.g. 7*pi/2, -3*pi, 0)")
            angle = input("θ = ") 

            try:
                theta = sympify(angle)
                sin_val = sin(theta)
                if sin_val == 0:
                    print(f"csc({angle}) is undefined")
                else:
                    result = simplify(1 / sin_val)
                    print(f"csc({angle}) =", result)
            except:
                print("⚠️ Invalid input.")
    if Q == 2:
        print("")
        from sympy import Rational, sqrt, simplify, S
        print("Trig Identity Calculator from sin(θ) and quadrant")
        print("--------------------------------------------------")
        n1 = int(input("first # (if negitive place -):"))
        n2 = int(input("second number:"))
        sin_val = Rational(n1, n2)
        quadrant = int(input("quandrant:"))

        cos_squared = 1 - sin_val**2
        cos_val = sqrt(cos_squared)

        if quadrant in [I := 1, IV := 4]:
            cos_val = +cos_val
        else:
            cos_val = -cos_val

        tan_val = simplify(sin_val / cos_val)
        sec_val = simplify(1 / cos_val)
        csc_val = simplify(1 / sin_val)
        cot_val = simplify(1 / tan_val)

        print(f"sin(θ) = {sin_val}")
        print(f"(a) cos(θ) = {cos_val}")
        print(f"(b) tan(θ) = {tan_val}")
        print(f"(c) sec(θ) = {sec_val}")
        print(f"(d) csc(θ) = {csc_val}")
        print(f"(e) cot(θ) = {cot_val}")
    if Q == 3:
        print("")
        from sympy import Rational, sqrt, simplify

        print("Trig Calculator from tan(θ) and quadrant")
        print("----------------------------------------")

        numerator = int(input("Enter numerator of tan(θ): "))   # e.g. 4
        denominator = int(input("Enter denominator of tan(θ): "))  # e.g. 3
        quadrant = int(input("Enter quadrant (1–4): "))  # Use 1 for 0 ≤ θ ≤ π/2

        opp = Rational(numerator)
        adj = Rational(denominator)
        hyp = sqrt(opp**2 + adj**2)

        sin_val = simplify(opp / hyp)
        cos_val = simplify(adj / hyp)
        if cos_val == 0:
            sec_val = "undefined"
        else:
            sec_val = simplify(1 / cos_val)

        if quadrant in [2, 3]:
            cos_val = -cos_val
            sec_val = -sec_val
        if quadrant in [3, 4]:
            sin_val = -sin_val

        print(f"\nGiven tan(θ) = {opp}/{adj}")
        print(f"sin(θ) = {sin_val}")
        print(f"cos(θ) = {cos_val}")
        print(f"sec(θ) = {sec_val}")
    if Q == 4:
        print("")
        from sympy import symbols, sin, cos, tan, sec, csc, cot, simplify, trigsimp
        print("Trig Expression Simplifier (Single Trig Function Output)")
        print("----------------------------------------------------------")

        t = symbols('t')

        expr_input = input("Enter trig expression (e.g. (csc(t)**2 - 1)/csc(t)**2): ").replace(" ", "")

        allowed = {
            "sin": sin, "cos": cos, "tan": tan,
            "sec": sec, "csc": csc, "cot": cot,
            "t": t
        }

        try:
            expr = eval(expr_input, allowed)
            
            simplified = trigsimp(expr)

            rewritten = simplified.rewrite(sin).rewrite(cos).rewrite(tan).rewrite(cot).rewrite(sec).rewrite(csc)

            final = trigsimp(rewritten)

            print(f"Simplified result: {final}")
        except Exception as e:
            print(f"⚠️ Invalid input. Details: {e}")


TOTF()