#BREAK : used to terminate the loop when encountered
#CONTINUE : used to skip the current iteration and continue with the next iteration. terminates execution in the current itternation & contnues execution of the loop
#PASS : used to skip the current iteration , pass is a null statement that does nothing. It is used as a placeholder for future code
#RETURN : used to exit the function

i = 1

while i<=5:
    if i == 3:
        i = i + 1
        continue # it will skip the current iteration and continue with the next iteration
    print(i)
    i = i + 1

print("out of loop")

