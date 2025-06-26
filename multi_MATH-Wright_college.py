def MULTI():

    import math
    import MATH_summerWrightcollege
    print("")
    print("what would you like to do?")
    print("chapter_5 = 1")
    print("chapter_6 = 2")
    print("chapter_7 = 3")
    print("chapter_8 = 4")
    Q = int(input(":"))
    if Q == 1:
        print("")
        print("what would you like to do?")
        print("circles |=1")
        print("angles |=2")
        print("Points on Circles using Sine and Cosine |=3")
        print("The Other Trigonometric Functions |=4")
        print("Right Triangle Trigonometry |=5")
        q = int(input(":"))
        if q == 1:
            import MATH_summerWrightcollege.circles
            print("")
            MATH_summerWrightcollege.circles()
            quit
        if q == 2:
            import MATH_summerWrightcollege.angles
            print("")
            MATH_summerWrightcollege.angles()
            quit
        if q == 3:
            import MATH_summerWrightcollege.P_O_C_U_S_A_C
            print("")
            MATH_summerWrightcollege.P_O_C_U_S_A_C()
            quit
        if q == 4:
            import MATH_summerWrightcollege.T_O_T_F
            print("")
            MATH_summerWrightcollege.T_O_T_F()
            quit
        if q == 5:
            import MATH_summerWrightcollege.right_triangle_trigonometry
            print("")
            MATH_summerWrightcollege.right_triangle_trigonometry()
            quit
    if Q == 2:
        print("")
        print("what would you like to do?")
        print("Sin Graphs |=1")
        print("Graphs of the Other trig Functions |=2")
        print("Inverse Trig Functions |=3")

        q = int(input(":"))
        if q == 1:
            import MATH_summerWrightcollege.sin_graphs
            print("")
            MATH_summerWrightcollege.sin_graphs()
            quit 
        if q == 2:
            import MATH_summerWrightcollege.G_O_T_O_T_F
            print("")
            MATH_summerWrightcollege.G_O_T_O_T_F()
            quit
        if q == 3:
            import MATH_summerWrightcollege.inverse_trig_functions
            print("")
            MATH_summerWrightcollege.inverse_trig_functions()
            quit


MULTI()

RUN = int(input("again? Yes=1|No=0"))

if RUN ==1:
    MULTI()
    while RUN == 1:
        RUN = int("again? Yes=1|No=0")
        if RUN ==1:
            MULTI()
        elif RUN ==0:
            print("DONE")
elif RUN ==0:
    print("DONE")