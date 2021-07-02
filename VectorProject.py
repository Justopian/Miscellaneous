import math as m

#Define Variables
vectors = [] #Each vector will be stored as a (x,y) tuple
resultant_vector = (0.0, 0.0)
polar_resultant_vector = (0.0, 0.0)
resultant_vector_string = ""
units = ""

main_prompt = """
Please choose an option or type "-1" to exit:
[0]: Input vector
[1]: Display vectors as x/y
[2]: Display vectors as r/\u03F4
[3]: Calculate resultant vector
"""

cartesian_or_polar_prompt = """
Please choose a vector format:
[0]: Cartesian (x,y)
[1]: Polar (r,\u03F4)
[2]: Cancel
"""

#Define Functions
def convert_polar_to_cartesian(radius, angle): #Converts polar (r,theta) to cartesian (x,y)
    x = radius * m.cos(m.radians(angle))
    y = radius * m.sin(m.radians(angle))
    return (x,y)

def convert_cartesian_to_polar(x, y):
    r = m.sqrt(x**2 + y**2)
    theta = m.degrees(m.atan2(y,x))
    while theta < 0:
        theta += 360
    if theta >= 360:
        theta %= 360
    return (r,theta)

def display_vectors(is_polar):
    if len(vectors) <= 0: #Vectors have not been added yet!
        print("\nPlease input at least one vector first!")
        return
    else:
        global units
        print("\nVectors:")
        for c in range(0,len(vectors)):
            v_name = chr(c + ord('a')) + "\u20D7"
            v = vectors[c]
            if is_polar:
                v = convert_cartesian_to_polar(v[0],v[1])
                print(" {vn} = {r:.2f} {u} @ {theta:.2f}\u00B0".format(vn = v_name, r = v[0], theta = v[1], u = units))
            else:
                print(" {vn} = ({x:.1f} {u})i\u0302 + ({y:.2f} {u})j\u0302".format(vn = v_name, x = v[0], y = v[1], u = units))

def calculate_resultant_vector():
    global resultant_vector, resultant_vector_string
    sum_x = 0.0
    sum_y = 0.0
    for v in vectors:
        sum_x += v[0]
        sum_y += v[1]
    resultant_vector = (sum_x, sum_y)
    resultant_vector_string = "({:.1f} ft.)i\u0302 + ({:.1f} ft.)j\u0302".format(sum_x, sum_y)

def calculate_polar_resultant_vector():
    global resultant_vector, polar_resultant_vector, resultant_vector_string
    calculate_resultant_vector()
    polar_resultant_vector = convert_cartesian_to_polar(resultant_vector[0], resultant_vector[1])
    resultant_vector_string = "{:.1f} ft. @ {:.1f}\u00B0".format(polar_resultant_vector[0], polar_resultant_vector[1])
    
#Start UI
print("Welcome to Group 19's Vector Program!")
units = input("\nUnits of length: ")
print("Note: All measurements of angles are in degrees")

i = 0
while(i != -1):
    i = int(input(main_prompt))
    if i == -1: #Leave immediately!
        break
    elif i == 0: #Input Vector
        j = int(input(cartesian_or_polar_prompt))
        while True:
            if j == 0: #Cartesian
                print()
                x = float(input("x = "))
                y = float(input("y = "))
                u = (x,y)
                vectors.append(u)
                break
            elif j == 1: #Polar
                print()
                r = float(input("r = "))
                theta = float(input("\u03F4 = "))
                u = convert_polar_to_cartesian(r,theta)
                vectors.append(u)
                break
            elif j == 2: #Cancel
                break
            else: #Not an option!
                print("\nPlease choose a valid option!\n")
                continue
    elif i == 1: #Display vectors as x/y
        display_vectors(False)
    elif i == 2: #Display vectors as r/theta
        display_vectors(True)
    elif i == 3: #Calculate resultant vector
        n = int(input(cartesian_or_polar_prompt)) #Ask for format
        while True:
            if n == 0: #Cartesian
                calculate_resultant_vector()
                break
            elif n == 1: #Polar
                calculate_polar_resultant_vector()
                break
            elif n == 2: #Cancel
                break
            else: #Not an option!
                print("\nPlease choose a valid option!\n")
                continue
        print("\nR = " + resultant_vector_string)
    else: #Not an option!
        print("Please choose a valid option!")
print("Have a nice day!")
