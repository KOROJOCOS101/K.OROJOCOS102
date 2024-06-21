import cmath
import numpy as np

while True:
    # Display the menu options
    print("1. Calculate the roots of a quadratic equation")
    print("2. Calculate the roots of a cubic equation")
    print("3. Calculate the roots of a quartic equation")

    # User input for the option
    option = int(input("Enter the option you want (1, 2, or 3): "))

    # User input for coefficients
    if option == 1:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        # Calculate the discriminant
        discriminant = b**2 - 4*a*c

        # Calculate the roots
        if discriminant > 0:
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
            print("The roots of the quadratic equation are: ", root1, root2)
        elif discriminant == 0:
            root1 = -b / (2*a)
            print("The quadratic equation has a repeated root: ", root1)
        else:
            real_part = -b / (2*a)
            imaginary_part = cmath.sqrt(abs(discriminant)) / (2*a)
            root1 = complex(real_part, imaginary_part)
            root2 = complex(real_part, -imaginary_part)
            print("The roots of the quadratic equation are complex: ", root1, root2)

    # User input for coefficients
    if option == 2:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        d = float(input("Enter coefficient d: "))

        # Calculate the discriminant
        discriminant = (b**2 - 3*a*c)**2 - 4*(b**3 - 4*a*b*c + a**2*d)**2

        # Calculate the roots
        if discriminant > 0:
            root1 = (-b/3/a + cmath.cube((-b**2 + 3*a*c + cmath.sqrt(discriminant))/(2*(b**3 - 4*a*b*c + a**2*d)))).real
            root2 = (-b/3/a + cmath.cube((-b**2 + 3*a*c - cmath.sqrt(discriminant))/(2*(b**3 - 4*a*b*c + a**2*d)))).real
            root3 = -b/3/a
        elif discriminant == 0:
            root1 = (-b/3/a + ((-b**2 + 3*a*c)**(1/3))/cmath.sqrt(a)).real
            root2 = root1
            root3 = -2*root1
        else:
            temp1 = -(b**2 - 3*a*c)/(2*(b**3 - 4*a*b*c + a**2*d))
            temp2 = cmath.sqrt(-discriminant) ** (1/3)
            root1 = temp1 + temp2
            root2 = cmath.polar(1)[0]*(cmath.sqrt(3)/2)*temp2 - temp1
            root3 = -2*temp1

        # Print the roots
        print("The roots of the cubic equation are: ", root1, root2, root3)

    elif option == 3:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        d = float(input("Enter coefficient d: "))
        e = float(input("Enter coefficient e: "))

        # Calculate the discriminant
        discriminant = (8*b*c*d - 4*b**2*e - 4*c**3 - 27*a**2*e**2 + 9*a*b*c*e)**2 - 4*(3*b**2*c**2 - b**3*d - c**4 + 4*b*c*d*e - a*c**2*e - 27*a**2*d**2)**3

        # Calculate the roots
        if discriminant > 0:
            temp1 = (-b + cmath.sqrt(discriminant))**(1/3)
            temp2 = (-b - cmath.sqrt(discriminant))**(1/3)
            root1 = (temp1 - temp2 + e/(3*a))*2
            temp3 = (-b + cmath.sqrt(1/2)*(1 + cmath.sqrt(3))*cmath.sqrt(discriminant))**(1/3)
            temp4 = (-b + cmath.sqrt(1/2)*(1 - cmath.sqrt(3))*cmath.sqrt(discriminant))**(1/3)
            root2 = temp3 - temp4 - e/(3*a)
            temp5 = (-b - cmath.sqrt(1/2)*(1 + cmath.sqrt(3))*cmath.sqrt(discriminant))**(1/3)
            temp6 = (-b + cmath.sqrt(1/2)*(1 + cmath.sqrt(3))*cmath.sqrt(discriminant))**(1/3)
            root3 = -1/2 * (temp3 + temp4) - e/(3*a) + 1j*(cmath.sqrt(3)/2) * (temp5 - temp6)
        elif discriminant == 0:
            root1 = -1/2 * (2*b**3 - 9*a*b*c + 27*a**2*d + cmath.sqrt(4*(b**2 - 3*a*c)**3 + (2*b**3 - 9*a*b*c + 27*a**2*d)**2))**(1/3) - (b**2 - 3*a*c)/(3*a)
            root2 = -(b**2 - 3*a*c)/(3*a) - 1/4 * (1 + 3j * cmath.sqrt(3)) * (2*b**3 - 9*a*b*c + 27*a**2*d + cmath.sqrt(4*(b**2 - 3*a*c)**3 + (2*b**3 - 9*a*b*c + 27*a**2*d)**2))**(1/3)
            root3 = -(b**2 - 3*a*c)/(3*a) - 1/4 * (1 - 3j * cmath.sqrt(3)) * (2*b**3 - 9*a*b*c + 27*a**2*d + cmath.sqrt(4*(b**2 - 3*a*c)**3 + (2*b**3 - 9*a*b*c + 27*a**2*d)**2))**(1/3)
        else:
            temp1 = cmath.sqrt((3*c/a - (b**2)/(a**2)) / 3)
            temp2 = cmath.acos((9*a*b*c - 2*b**3 - 27*a**2*d) / (2 * (temp1**3)))
            root1 = -2 * temp1 * cmath.cos(temp2/3) - b/(3*a)
            root2 = -2 * temp1 * cmath.cos((temp2 + 2*np.pi)/3) - b/(3*a)
            root3 = -2 * temp1 * cmath.cos((temp2 + 4*np.pi)/3) - b/(3*a)

        # Print the roots
        print("The roots of the quartic equation are: ", root1, root2, root3)
    
    else:
        print("Invalid option selected!")

    # Ask user if they want to continue or end
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
       
