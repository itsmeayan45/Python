#functions with outputs
def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "please enter valid input"
    f_f_name=f_name.title()
    f_l_name=l_name.title()
    return f"{f_f_name} {f_l_name}"
print(format_name(input("What is your first name? "),input("What is your last name? ")))