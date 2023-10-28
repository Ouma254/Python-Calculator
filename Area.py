# program to find area of various shapes
class Area:
    def control_unit(self):
        while True:
            print("Welcome to Digital Calculator..\n")
            print("Choose on the shapes to find their areas, perimeter & Volumes")
            print("\n Options")
            print("1. Circle")
            print("2. Square")
            print("3. Traingle")
            print("4. Rhombus")
            print("0. Quit")

            # if-else statement to control on the choices made by the user
            choice_input = int(input("Enter Your Choice: \n"))
            if choice_input == 1:
                calc.circle_shape()
                # action
            elif choice_input == 2:
                calc.square_shape()
                # action 
            elif choice_input == 3:
                  calc.triangle_shape()
            elif choice_input == 4:
                print("")
                # action
            elif choice_input == 5:
                print()
                 # actioncategory
            elif choice_input == 0:
                print("Thank you for using the calculator")
                break  
            else:
                print("Invalid Input!! Error") 

    def area_circle(self):
        circle_radius = int(input("Enter the radius of the Circle: \n"))
        # formula to find the area of the circle
        result_area = PIE * circle_radius ** 2
        print(f"The area of the Circle is: ")
        # the output
        print(f"The Radius is {circle_radius}\n & AREA is {result_area}")
        # yield f"AREA IS: {result_area} square units\n Radius is : {circle_radius}"

    def perimeter_circle(self):
        # find the perimeter of the cicle 
        radius_input = int(input("Enter the Radius"))
        # formula for the perimeter
        perimeter = PIE * radius_input * 2 
        # yield f"Radius is : {radius_input} and the Perimeter is {perimeter}"  
        print(f"Radius of the Circle is {radius_input} \n Perimeter is {int(perimeter)} units")               

    def circle_shape(self):
        global PIE
        PIE= 3.14
        # user to input the radius  0r Area of the circle
        print("Please input Either area or Radius of Circle")
        while True:
            print("Perimeter or Area?")
            print("OPTIONS\n")
            print("a. Area")
            print("b. Perimeter")
            print("q. Exit")

            user_selection = input("Enter Operation to carry out:\n")
            if user_selection == 'area' or user_selection == 'Area':
                calc.area_circle()
            elif user_selection == 'perimeter' or user_selection == 'Periemter':
                calc.perimeter_circle()
            elif user_selection == 'exit' or user_selection == 'Exit':
                print("Thank you, Keep using the Calc")
                break
            else:
                print("Error Incorrect Input")

    # the square shape properties
    def square_shape(self):
        print("Find Area or Perimeter?")
         # while loop to control
        while True:
            print("OPTIONS\n")
            print("1. Perimeter")
            print("2. Area")
            print("3. Length of one side")
            print("0. Exit")
            
            # check on the user input for validity
            user_choice = int(input("Selection?\n"))
            if user_choice == 1:
                # action
                calc.perimeter_square()
                print("")
            elif user_choice == 2:
                # action
                calc.area_square()
                print("")
            elif user_choice == 3:
                # action
                calc.find_length()
                print("")
            elif user_choice == 0:
                # action
                calc.control_unit() 
                break 
            else:
                print("Error Invalid Choice!")

    def area_square(self):
        print("Let's Go..")
        # user data input
        length_side = int(input("Enter the length of one side:\n"))
        # formular
        area_sq = length_side ** 2
        print("Results Are:\n")
        print(f"Length of one side: {length_side}" )
        print(f"Area of the Square: {area_sq}")

    def perimeter_square(self):
        print("Yes Go on..")
        # user_data
        one_side = int(input("Enter the length of one side: \n"))
        # formula
        perimeter = one_side * 4
        # output
        print("Results:\n")
        print(f"Side of the Square is: {one_side}")
        print(f"Perimeter of the Square is: {perimeter}")

    def find_length(self):
        print("Again get moving..")
        user_data = int(input("Enter the area of the Square:\n"))
        # formula
        length_of_square = user_data ** 0.5

        # output
        print(f"The Area of the Square was {user_data}")
        print(f"Length of one-side is: {length_of_square}")

    # triangle shape
    def triangle_shape(self):
        print("The Triangle Shape: ")
        
        while True:
            print("lIST OF OPERATION TO PERFORM\n")
            print("1. Area")
            print("2. Perimeter")
            print("0. Exit")

            user_info = int(input("Enter the choice:\n"))
            if user_info == 1:
                calc.area_triangle()
            elif user_info == 2:
                calc.perimeter_triangle()
            elif user_info == 0:
                calc.control_unit()
                print("")
                break
            else:
                print("Invalid!! Try Again")   

    def area_triangle(self):
        print("Find the area of triangle")
        height = int(input("Enter the Height of Traingle:\n"))
        width = int(input("Enter the Width of the Triangle:\n"))
        are_triangle = 0.5 * height * width
        print("results")
        print(f"The Width is {width} and Height is {height}")
        print(f"The area of the Triangle is {are_triangle}")                 

    def perimeter_triangle(self):
        print("The perimeter")
        width_tri = int(input("Enter Width is: \n"))
        hypotenous = int(input("Enter hypotenous: \n"))
        height = int(input("Enter height:\n"))
        peri = width_tri + height + hypotenous
        # output
        print("Results") 
        print(f"the height is {height}, width is {width_tri} and hypotenous is {hypotenous}")
        print(f"Perimeter is {peri}")   




# instance of the class
calc = Area()
calc.control_unit()

                            