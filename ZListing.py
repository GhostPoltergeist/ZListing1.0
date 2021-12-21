import time
import os
clear = lambda: os.system('cls')
#ZIG-ZAG LISTING PROPERTIES
'''
 >: ZigZag Listing is A wide exploration of value assignments
    This program engage "arrays" :<<
    #: Separation of Values are performed by different variables.
███████╗    ██╗     ██╗███████╗████████╗██╗███╗   ██╗ ██████╗
╚══███╔╝    ██║     ██║██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝
  ███╔╝     ██║     ██║███████╗   ██║   ██║██╔██╗ ██║██║  ███╗
 ███╔╝      ██║     ██║╚════██║   ██║   ██║██║╚██╗██║██║   ██║
███████╗    ███████╗██║███████║   ██║   ██║██║ ╚████║╚██████╔╝
╚══════╝    ╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝
    {Rows}>>{Columns}>>{Elements}
'''
"""
>>: SOURCE :<< 
#: CREDITS: https://byjus.com/math-formulas//
"""
def main():
    print("""
    ███████╗ __ ██╗_____██╗███████╗████████╗██╗███╗___██╗_██████╗
    ╚══███╔╝____██║_____██║██╔════╝╚══██╔══╝██║████╗__██║██╔════╝
    __███╔╝_____██║_____██║███████╗___██║___██║██╔██╗_██║██║__███╗
    _███╔╝______██║_____██║╚════██║___██║___██║██║╚██╗██║██║___██║
    ███████╗____███████╗██║███████║___██║___██║██║_╚████║╚██████╔╝
    ╚══════╝____╚══════╝╚═╝╚══════╝___╚═╝___╚═╝╚═╝__╚═══╝_╚═════╝
    вy: gнoѕтpolтergeιѕт
    """)
    # >>: CLASS 6 FORMULA'S
    print(" [ZL]>>: List Math Formulas")
    MF = [
        [" >>: √ab=√a√b"],
        [" >>: √a/b=√a/√b"],
        [" >>: (√a+√b)(√a−√b)=a−b"],
        [" >>: (a+√b)(a−√b)=a^2−b"],
        [" >>: (√a+√b)^2=a+2√ab+b"],
        [" >>: a^pa^q=a^p+q"],
        [" >>: (a^p)^q=a^pq"],
        [" >>: a^p/a^q=a^p−q"],
        [" >>: a^pb^p=(ab)^p"]
    ]

    __ST3__ = [
        [5.0],  [6.0],  [7.0],  [8.0],  [9.0],  [10.0],
        [11.0], [12.0], [13.0], [14.0], [15.0], [16.0],
        [18.0], [17.0], [18.0], [19.0], [20.0], [21.0],
        [22.0], [23.0], [24.0], [25.0], [26.0], [27.0],
        [28.0], [29.0], [30.0], [31.0], [32.0], [33.0],
        [34.0], [35.0], [36.0], [37.0], [38.0], [39.0],
        [40.0], [41.0], [42.0], [43.0], [44.0], [45.0],
        [46.0], [47.0], [48.0], [49.0], [50.0], [51.0],
        [52.0], [53.0], [54.0], [55.0], [56.0], [57.0]
    ]


    MF2 = [" >>: x=−b±√b2−4ac/2a"]

    Ques = int(input("""
    CHOOSE USING NUMBER[#]
    Number System Formulas[1]
    Mensuration Formulas for Two dimensional Figures[2]
    Basic Algebra Formula[3]
    Area Formulas[4]
    Area of a Triangle Formula[5]
    Area of a Right Angled Triangle[6]
    Area of an Equilateral Triangle[7] 
    Area of an Isosceles Triangle[8]
    Perimeter of a Triangle[9]
    Area of Triangle with Three Sides (Heron’s Formula)[10]
    Area of a Triangle Given Two Sides and the Included Angle(SAS)[11]
    
    SPECIFY YOUR CHOICE >>: """))
    if Ques == 1:
       print("""
       Addition of integers is commutative a + b = b + a
       Addition of integers is associative a + ( b + c ) = ( a + b) + c
       0 is the identity element under addition a + 0 = 0 + a = a
       Multiplication of integers is commutative. a x b = b x a
       1 is the identity element under multiplication 1 x a = a x 1 = a
       
       FORMULA'S ARE LISTED BELOW
       """)
       time.sleep(3)
       print(MF[0][0])
       print(MF[1][0])
       print(MF[2][0])
       print(MF[3][0])
       print(MF[4][0])
       print(MF[5][0])
       print(MF[6][0])
       print(MF[7][0])
       print(MF[8][0])

    if Ques == 2:
        print("""
        2-Dimensional Figures   Area (Sq.units)   Perimeter (Units)
        
    >>: Square                  (side)2            4 x side
    
    >>: Triangle                ½ ( b x h )        Sum of all sides
    
    >>: Rectangle             length x breadth     2 ( length + breadth )
    
    >>: Circle                    πr2                 2πr
    
    """)
    if Ques == 3:
        print(MF2[0])
    if Ques == 4:
        print("""
        
        Rectangle      Area = l $\ times$ w            l =  length
                                                       w  = width
                                                   
        Square         Area  = $a^{2}$                 a = sides of square
    
        Triangle       Area = $\ frac{1}{2}$bh         b = base
                                                       h = height
    
        Circle         Area = $\pi$$r^{2}$             r = radius of circle
        
        Trapezoid      Area =$\ frac{1}{2}$(a + b)h    a = base 1
                                                       b = base 2
                                                       h = vertical height
                                                       
        Ellipse        Area = $\pi$ab                  a = radius of major axis
                                                       b = radius of minor axis
    """)
    if Ques == 5:
        print(" >>: Area of a Triangle = A = ½ (b × h) square units")
    if Ques == 6:
        print(" >>: Area of a Right Triangle = A = ½ × Base × Height {Perpendicular distance}")
    if Ques == 7:
        print(" >>: Area of an Equilateral Triangle = A = (√3)/4 × side2")
    if Ques == 8:
        print(" >>: Area of an Isosceles Triangle = 1/4 b√(4a2 – b2)")
    if Ques == 9:
        print(" >>: The perimeter of a triangle = P = (a + b + c) units")
    if Ques == 10:
        print(" >>: Area = Square root of√s(s - a)(s - b)(s - c) where s is half the perimeter, or (a + b + c)/2.")
    if Ques == 11:
        print(""" >>: 
    
    Area (∆ABC) = ½ bc sin A
    
    Area (∆ABC) = ½ ab sin C
    
    Area (∆ABC) = ½ ca sin B
    
    These formulas are very easy to remember and also to calculate.
    
    For example, If, in ∆ABC,  A = 30° and b = 2, c = 4 in units. Then the area will be;
    
    Area (∆ABC) = ½ bc sin A
    
    = ½ (2) (4) sin 30
    
    = 4 x ½   (since sin 30 = ½)
    
    = 2 sq.unit.
    
    """)
    repeat = input("   >>: Would you like to Calculate Another Integer Value [y]/[n]: ").lower()
    if repeat == "y":
        clear()
        main()
    else:
        print("   >>: Thank you User")
        exit()
clear()
main()



