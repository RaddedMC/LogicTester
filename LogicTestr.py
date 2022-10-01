# JamesN / Radded
# LogicTestr.py

# Generates truth tables for given logical expressions.
# Used to speed up my lab work in ECE 2277.


# --- USER-ACCESSIBLE --- #
# Names of each INPUT variable
variable_names = ["w", "x", "y", "z"]

# Logic Expression 1
def logic_expr_1(variables):
    # variables[0-n] for each variable
    w = variables[0]
    x = variables[1]
    y = variables[2]
    z = variables[3]

    return ( ((not w) and (not x) and (not z) ) or ( (not w) and (x) and (y) ) or ( (w) and (not x) ) )

def logic_expr_2(variables):
    # variables[0-n] for each variable
    w = variables[0]
    x = variables[1]
    y = variables[2]
    z = variables[3]

    # have fun with this one
    return ( ( (not w) and (not x) and (not y) and (not z) ) or ( (not w) and (not x) and (y) and (not z) ) or ( (not w) and (x) and (y) and (not z) ) or ( (not w) and (x) and (y) and (z) ) or ( (w) and (not x) and (not y) and (not z) ) or ( (w) and (not x) and (not y) and (z) ) or ( (w) and (not x) and (y) and (not z) ) or ( (w) and (not x) and (y) and (z) ) )



# Figure out number of binary combinations
from math import pow
combos_to_test = round(pow(2,len(variable_names)))


# Generate list of values for each combo
# [combination number -- 0 to combos_to_test-1] [variable number -- 0 to len(variable_names)-1]
input_variable_values = []

for i in range(0,combos_to_test):

    # Create sublist
    input_variable_values.append([])

    # Convert the number to binary
    binary_i = format(i, '0{len_variables}b'.format(len_variables=len(variable_names)))

    # Split the binary number into characters or 1/0 values
    for index_character in enumerate(binary_i):
        # index_character[0] = index
        # index_character[1] = value

        # [combination] [variable]                             (Gets the character from the string)
                                                        #  (Converts the character to an int, 0 = False, 1 = True)
                                                    #  (Converts the int into a boolean)
        input_variable_values[i].append(            bool(int(index_character[1])))


# Evaluate each expression and add it to list
for in_vars in enumerate(input_variable_values):
    input_variable_values[in_vars[0]].append(logic_expr_1(in_vars[1]))
    input_variable_values[in_vars[0]].append(logic_expr_2(in_vars[1]))


# Print the truth table!
# Start by printing the header

# w    x    y    z    f_1   f_2
# True True True True False False
from tabulate import tabulate
with open("output.html", "w") as f:
    f.write("<!DOCTYPE html> <html> <head> <link rel=\"stylesheet\" href=\"style.css\"> </head> <body>")
    f.write(tabulate(input_variable_values, headers=[*variable_names, "my_work", "given_soln"], tablefmt="html"))
    f.write("<script src=\"coloration.js\"></script></body> </html>")