import math
def circles():
    print("--------circles--------")
    print("")
    print("Find the distance between the points (X,Y) and (X2,Y2) |=1")
    print("")
    print("write the equation of a circle centered at (X,Y) with radius 1 |=2")
    print("")
    print("write the equation of the circle centered at (a,b) that passes through (x,y) |=3")
    print("")
    print("find point of intersection in 1st quadrant between y = mx + b and circle |=4")
    print("")
    print("Find the center and radius of the circle whose equation is x^2 -/+ #x + y^2 -/+ #y -/+ # = 0 |=5")
    print("")
    print("write the standard equations of the circle with a diameter with endpoints (X1,y1) and (X2,Y2) |=7")
    print("")
    print("Enter coefficients for the circle equation |=8")
    print("")
    q = int(input("what type?-"))
    if q == 1:
        print("------X number-------")
        x1 = int(input("({#},#): "))
        print("------Y number-------")
        y1 = int(input("(#,{#}): "))
        print("------X number-2-----")
        x2 = int(input("({#},#): "))
        print("------Y number-2-----")
        y2 = int(input("(#,{#}): "))
        print("------------------")
        dx = x2 - x1
        dy = y2 - y1
        print("dx = x2 - x1 =", dx)
        print("dy = y2 - y1 =", dy)
        dx2 = dx ** 2
        dy2 = dy ** 2
        print("dx^2 =", dx2)
        print("dy^2 =", dy2)
        d_sum = dx2 + dy2
        print("dx^2 + dy^2 =", d_sum)
        distance = math.sqrt(d_sum)
        print("Distance = sqrt("+str(d_sum)+") = ", distance)
    if q == 2:
        print("------------------")
        x = int(input("({#},#): "))
        y = int(input("(#,{#}): "))
        r = int(input("radius: "))
        if x < 0:
            x_sign = "+" + str(abs(x))
        else:
            x_sign = "-" + str(x)
        if y < 0:
            y_sign = "+" + str(abs(y))
        else:
            y_sign = "-" + str(y)
        EQ = "(x " + x_sign + ")^2 + (y " + y_sign + ")^2 = " + str(r**2)
        print("Center: (" + str(x) + "," + str(y) + ")")
        print("Radius: " + str(r))
        print("Equation: " + EQ)
    if q == 3:
        print("")
        import math
        h = float(input("center x (h): "))
        k = float(input("center y (k): "))
        x1 = float(input("point x: "))
        y1 = float(input("point y: "))

        r = math.sqrt((x1 - h) ** 2 + (y1 - k) ** 2)
        r_squared = round(r**2, 2)

        x_sign = f"+{-h}" if h < 0 else f"-{h}"
        y_sign = f"+{-k}" if k < 0 else f"-{k}"

        print("------------------")
        print("Center:", f"({h},{k})")
        print("Point it passes through:", f"({x1},{y1})")
        print("Radius:", round(r, 2))
        print("Equation: (x " + x_sign + ")^2 + (y " + y_sign + ")^2 = " + str(r_squared))
    if q == 4:
        import math
        print("Find the intersection of line y = mx + b and circle (x - h)^2 + (y - k)^2 = r^2")
        m = float(input("Enter the slope of the line (m): "))
        b = float(input("Enter the y-intercept of the line (b): "))
        h = float(input("Enter the x-coordinate of the circle's center (h): "))
        k = float(input("Enter the y-coordinate of the circle's center (k): "))
        r = float(input("Enter the radius of the circle (r): "))

        print("Step 1: Substitute y = mx + b into (x - h)^2 + (y - k)^2 = r^2")
        print(f"Equation becomes: (x - {h})^2 + ({m}x + {b} - {k})^2 = {r}^2")

        a = 1 + m**2
        b_quad = 2*m*(b - k) - 2*h
        c = h**2 + (b - k)**2 - r**2

        print("Step 2: Expand into quadratic form ax^2 + bx + c = 0")
        print(f"a = 1 + m^2 = {a}")
        print(f"b = 2m(b - k) - 2h = {b_quad}")
        print(f"c = h^2 + (b - k)^2 - r^2 = {c}")

        discriminant = b_quad**2 - 4*a*c
        print(f"Step 3: Discriminant = b^2 - 4ac = {discriminant}")

        if discriminant < 0:
            print("No intersection")
        else:
            sqrt_disc = math.sqrt(discriminant)
            x1 = (-b_quad + sqrt_disc) / (2*a)
            y1 = m*x1 + b
            x2 = (-b_quad - sqrt_disc) / (2*a)
            y2 = m*x2 + b

            print("Step 4: Solve for x using quadratic formula")
            print(f"x1 = {x1:.3f}, y1 = {y1:.3f}")
            print(f"x2 = {x2:.3f}, y2 = {y2:.3f}")

            print("\nPoints of intersection:")
            found = False
            if x1 > 0 and y1 > 0:
                print(f"First quadrant: x = {x1:.3f}, y = {y1:.3f}")
                found = True
            if x2 > 0 and y2 > 0:
                print(f"First quadrant: x = {x2:.3f}, y = {y2:.3f}")
                found = True
            if not found:
                print("No point in first quadrant")
    if q == 5:
        import math

        print("Find the center and radius of the circle whose equation is x^2 -/+ #x + y^2 -/+ #y -/+ # = 0")
        print("--------------------")
        print("x^2 -/+ {#}x + y^2 -/+ #y -/+ # = 0")

        number1 = int(input("enter first #:"))  # Coefficient of x
        print("--------------------")
        print("x^2 -/+ " + str(number1) + "x + y^2 -/+ {#}y -/+ # = 0")

        number2 = int(input("enter second #:"))  # Coefficient of y
        print("--------------------")
        print("x^2 -/+ " + str(number1) + "x + y^2 -/+ " + str(number2) + "y -/+ {#} = 0")

        number3 = int(input("enter third #:"))  # Constant term
        print("--------------------")
        print("x^2 -/+ " + str(number1) + "x + y^2 -/+ " + str(number2) + "y -/+ " + str(number3) + " = 0")
        print("--------------------")

        number3 = number3 * -1
        print("x^2 -/+ " + str(number1) + "x + ____ + y^2 -/+ " + str(number2) + "y + ____ = " + str(number3) + " + ____ + ____")
        print("--------------------")

        print("(" + str(number1) + "/2)^2")
        number4 = (number1 / 2) ** 2
        print(str(number4))
        print("x^2 -/+ " + str(number1) + "x + " + str(number4) + " + y^2 -/+ " + str(number2) + "y + ____ = " + str(number3) + " + " + str(number4) + " + ____")
        print("--------------------")

        print("(" + str(number2) + "/2)^2")
        number5 = (number2 / 2) ** 2
        print(str(number5))
        print("x^2 -/+ " + str(number1) + "x + " + str(number4) + " + y^2 -/+ " + str(number2) + "y + " + str(number5) + " = " + str(number3) + " + " + str(number4) + " + " + str(number5))
        print("--------------------")

        total = number3 + number4 + number5
        print("Now rewrite in completed square form:")
        h = -number1 / 2
        k = -number2 / 2
        print("(x - " + str(h) + ")^2 + (y - " + str(k) + ")^2 = " + str(total))
        print("--------------------")

        print("Center: (" + str(h) + ", " + str(k) + ")")
        radius = math.sqrt(total)
        print("Radius: √" + str(total) + " ≈ " + str(round(radius, 2)))
    elif q == 6:
        print("General form: x² + y² + Dx + Ey + F = 0")
        D = float(input("Enter coefficient of x (D): "))
        E = float(input("Enter coefficient of y (E): "))
        F = float(input("Enter constant term (F): "))
        h = -D / 2
        k = -E / 2
        r_squared = h**2 + k**2 - F
        if r_squared < 0:
            print("No real circle (radius² < 0)")
        else:
            r = math.sqrt(r_squared)
            print(f"Center: ({h}, {k}), Radius: √{r_squared} ≈ {round(r, 3)}")
            print(f"Standard form: (x - {h})² + (y - {k})² = {round(r_squared, 3)}")
    elif q == 7:
        import math
        print("write the standard equations of the circle with a diameter with endpoints (X1,y1) and (X2,Y2)")
        print("------X number-------")
        x1 = int(input("({#},#): "))
        print("------Y number-------")
        y1 = int(input("(#,{#}): "))
        print("------X number-2-----")
        x2 = int(input("({#},#): "))
        print("------Y number-2-----")
        y2 = int(input("(#,{#}): "))
        print("------------------")
        X = x1+x2
        X = X/2 
        print("h="+str(X))
        print("------------------")
        Y = y1+y2
        Y = Y/2 
        print("k="+str(Y))
        print("------------------")
        D1 = (x1 - X)
        print(str(D1))
        D1 = D1**2
        print(str(D1))
        D2 = (y1 - Y)
        print(str(D2))
        D2 = D2**2
        print(str(D2))
        D = D1 + D2
        print(str(D))
        print("R=sqrt"+str(D))
        D = math.sqrt(D)
        print("------------------")
        print("(x - h:"+str(X)+")^2 + (y - k:"+str(Y)+")^2 ="+str(D))
    elif q == 8:
        import math
        print("Enter coefficients for the circle equation:")
        print("------------------")
        print("Format: x^2 + y^2 + Dx + Ey + F = 0")
        D = float(input("Enter coefficient D (for x): "))   
        print("------------------")
        E = float(input("Enter coefficient E (for y): "))   
        print("------------------")
        F = float(input("Enter constant F: "))         
        print("------------------")    
        h = -D / 2
        k = -E / 2
        r_squared = h**2 + k**2 - F
        if r_squared < 0:
            print("This equation does not represent a real circle (radius squared < 0).")
        else:
            r = math.sqrt(r_squared)
            print("------ Results ------")
            print(f"Center (h, k): ({h}, {k})")
            print(f"Radius r: {round(r, 3)}")

            print("------ Standard Form Equation ------")
            print(f"(x - {h})² + (y - {k})² = {round(r**2, 3)}")

    
circles()