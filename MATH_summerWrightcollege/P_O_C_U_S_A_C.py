import math

def POCUSAC():
    print("--------Points on using sine and cosine--------")
    print("")
    print("From the information given, find the quadrant in which the terminal point determined by t lies. Input I, II, III, or IV. |=1")
    print("")
    print("Find the x-coordinate on the unit circle given y and quadrant |=2")
    print("")
    print("Find sin(θ) given cos(θ) and quadrant |=3")
    print("")
    print("Find sine and cosine using reference angle (degrees) |=4")
    print("")
    print("Find sine and cosine of angle using reference angle (radians) |=5")
    print("")
    print("Find angles with same sine or cosine as a given angle |=6")
    print("")
    print("Find angles with same sine and cosine values as a given angle |=7")
    print("")
    print("Find coordinates on a circle of radius r for a given angle θ |=8")
    print("")
    print("cos, sec, sin, and more calculator |=9")
    print("")
    q = int(input("what type?-"))

    if q == 1:
        print("sin(t)-cos(t) |=1")
        print("cos(t)-sin(t) |=2")
        print("cos(t)-tan(t) |=3")
        print("sec(t)-csc(t) |=4")

        q = int(input("what problem?-"))

        if q == 1:
            print("")
            print("sin(t) > 0 and cos(t) > 0, quadrant: I")
            print("sin(t) > 0 and cos(t) < 0, quadrant: II")
            print("sin(t) < 0 and cos(t) < 0, quadrant: III")
            print("sin(t) < 0 and cos(t) > 0, quadrant: IV")
        if q == 2:
            print("")
            print("cos(t) > 0 and sin(t) > 0, quadrant: I")
            print("cos(t) < 0 and sin(t) > 0, quadrant: II")
            print("cos(t) < 0 and sin(t) < 0, quadrant: III")
            print("cos(t) > 0 and sin(t) < 0, quadrant: IV")
    if q == 2:
        import math

        print("Find the x-coordinate on the unit circle given y and quadrant")
        print("--------------------------------------------------------------")

        y1 = float(input("Enter numerator of y (use negative sign if needed): "))
        y2 = float(input("Enter denominator of y: "))
        y = y1 / y2

        print("")
        quadrant = int(input("Enter quadrant number (1 to 4): "))

        x_squared = 1 - y**2

        if x_squared < 0:
            print("⚠️ Invalid input: y² > 1, which is not possible on the unit circle.")
        else:
            x = math.sqrt(x_squared)
            if quadrant in [2, 3]:
                x = -x

            print("------ Results ------")
            print(f"x² = {round(x_squared, 4)}")
            root_expr = f"√({round(x_squared, 4)})"
            sign = "-" if quadrant in [2, 3] else ""
            print(f"x = {sign}{root_expr}")
            print(f"x ≈ {round(x, 4)}")
    if q == 3:
        print("")
        import math
        print("Find sin(θ) given cos(θ) and quadrant")
        print("-------------------------------------")
        numerator = int(input("Enter numerator of cos(θ) (use negative if needed): "))
        denominator = int(input("Enter denominator of cos(θ): "))
        cos_theta = numerator / denominator
        quadrant = int(input("Enter quadrant (1 to 4): "))
        sin_squared = 1 - cos_theta**2
        sin_theta = math.sqrt(sin_squared)
        if quadrant in [3, 4]:
            sin_theta = -sin_theta
        print("------ Results ------")
        print("sin²(θ) = "+str(round(sin_squared, 4)))
        print(f"sin(θ) = {'-' if sin_theta < 0 else ''}√({round(sin_squared, 4)})")
        print(f"sin(θ) ≈ {round(sin_theta, 4)}")
    if q == 4:
        print("")
        import math
        print("Find sine and cosine using reference angle (no calculator mode)")
        print("---------------------------------------------------------------")
        angle = int(input("Enter angle in degrees: "))
        # used refrences and help from online sources
        angle = angle % 360
        if 0 < angle < 90:
            quadrant = 1
            ref_angle = angle
        elif 90 < angle < 180:
            quadrant = 2
            ref_angle = 180 - angle
        elif 180 < angle < 270:
            quadrant = 3
            ref_angle = angle - 180
        elif 270 < angle < 360:
            quadrant = 4
            ref_angle = 360 - angle
        else:
            quadrant = None
            ref_angle = 0
        if ref_angle == 30:
            sin_val = 1/2
            cos_val = math.sqrt(3)/2
        elif ref_angle == 45:
            sin_val = cos_val = math.sqrt(2)/2
        elif ref_angle == 60:
            sin_val = math.sqrt(3)/2
            cos_val = 1/2
        else:
            sin_val = cos_val = None
        if quadrant in [3, 4]:
            sin_val = -sin_val
        if quadrant in [2, 3]:
            cos_val = -cos_val
        print("----- Results ------")
        print(f"Reference angle: {ref_angle}°")
        print(f"Quadrant: {quadrant}")
        print(f"sin({angle}°) = {round(sin_val, 4)}")
        print(f"cos({angle}°) = {round(cos_val, 4)}")
    if q == 5:
        print("")
        import math
        print("Find sine and cosine of angle using reference angle (radians)")
        print("--------------------------------------------------------------")
        # used internet to find help
        import math
        numerator = int(input("Enter numerator (e.g., 5 for 5π/6): "))
        denominator = int(input("Enter denominator (e.g., 6 for 5π/6): "))
        angle_rad = (numerator * math.pi) / denominator
        angle_mod = angle_rad % (2 * math.pi)
        angle_30 = math.pi / 6
        angle_45 = math.pi / 4
        angle_60 = math.pi / 3
        if 0 < angle_mod < math.pi / 2:
            quadrant = 1
            reference_angle = angle_mod
        elif math.pi / 2 < angle_mod < math.pi:
            quadrant = 2
            reference_angle = math.pi - angle_mod
        elif math.pi < angle_mod < 3 * math.pi / 2:
            quadrant = 3
            reference_angle = angle_mod - math.pi
        elif 3 * math.pi / 2 < angle_mod < 2 * math.pi:
            quadrant = 4
            reference_angle = 2 * math.pi - angle_mod
        else:
            quadrant = "Axis (not in a quadrant)"
            reference_angle = 0

        def approx_equal(a, b, tol=1e-4):
            return abs(a - b) < tol

        if approx_equal(reference_angle, angle_30):
            sin_ref = 1/2
            cos_ref = math.sqrt(3)/2
            sin_text = "1/2"
            cos_text = "√3/2"
        elif approx_equal(reference_angle, angle_45):
            sin_ref = cos_ref = math.sqrt(2)/2
            sin_text = cos_text = "√2/2"
        elif approx_equal(reference_angle, angle_60):
            sin_ref = math.sqrt(3)/2
            cos_ref = 1/2
            sin_text = "√3/2"
            cos_text = "1/2"
        else:
            sin_text = cos_text = "N/A"
            sin_ref = cos_ref = None

        if quadrant in [3, 4] and sin_ref is not None:
            sin_ref = -abs(sin_ref)
            sin_text = "-" + sin_text
        if quadrant in [2, 3] and cos_ref is not None:
            cos_ref = -abs(cos_ref)
            cos_text = "-" + cos_text

        print("------ Results ------")
        print(f"Input angle: {numerator}π/{denominator} rad = {round(angle_mod, 4)} rad")
        print(f"Reference angle: {round(reference_angle, 4)} rad")
        print(f"Quadrant: {quadrant}")
        print(f"sin({numerator}π/{denominator}) = {sin_text} ≈ {round(sin_ref, 4) if sin_ref else 'N/A'}")
        print(f"cos({numerator}π/{denominator}) = {cos_text} ≈ {round(cos_ref, 4) if cos_ref else 'N/A'}")
    if q == 6:
        print("")
        import math
        print("Find angles with same sine or cosine as a given angle")
        print("------------------------------------------------------")
        angle = int(input("Enter angle θ (0° < θ < 90°): "))
        if 0 < angle < 90:
            same_sin = 180 - angle
            same_cos = 360 - angle

            print("------ Results ------")
            print(f"Original angle: {angle}°")
            print(f"Angle with same sine: θ = {same_sin}°")
            print(f"Angle with same cosine: θ = {same_cos}°")
        else:
            print("⚠️ Please enter an angle between 0° and 90° (non-inclusive).")
    if q == 7:
        print("")
        print("Find angles with same sine and cosine values as a given angle")
        print("--------------------------------------------------------------")
        theta = int(input("Enter angle θ (0° < θ < 360°): "))
        if 0 < theta < 360:
            if theta < 90:
                ref_angle = theta
                quadrant = 1
            elif theta < 180:
                ref_angle = 180 - theta
                quadrant = 2
            elif theta < 270:
                ref_angle = theta - 180
                quadrant = 3
            else:
                ref_angle = 360 - theta
                quadrant = 4

            if quadrant == 1 or quadrant == 2:
                same_sin = 180 - ref_angle
            else:  
                same_sin = 360 - ref_angle

            if quadrant == 1 or quadrant == 4:
                same_cos = 360 - ref_angle
            else: 
                same_cos = 180 - ref_angle

            print("------ Results ------")
            print(f"Original angle: {theta}°")
            print(f"Reference angle: {ref_angle}°")
            print(f"Angle with same sine: θ = {same_sin}°")
            print(f"Angle with same cosine: θ = {same_cos}°")
        else:
            print("⚠️ Please enter an angle strictly between 0° and 360°.")
    if q == 8:
        import math
        print("")
        print("Find coordinates on a circle of radius r for a given angle θ")
        print("------------------------------------------------------------")
        radius = int(input("Enter given radius: "))
        theta = float(input("Enter angle θ (0° ≤ θ < 360°): "))
        if 0 <= theta < 360:
            radians = math.radians(theta)
            x = radius * math.cos(radians)
            y = radius * math.sin(radians)
            print("------ Results ------")
            print(f"Radius: {radius}")
            print(f"Angle: {theta}°")
            print(f"Coordinates: (x, y) = ({x:.3f}, {y:.3f})")
        else:
            print("⚠️ Please enter an angle between 0° and 360° (inclusive of 0°, exclusive of 360°).")
    if q == 9:
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

POCUSAC()


