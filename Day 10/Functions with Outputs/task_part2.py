def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_string = (format_name("AnGEla", "YU"))
print(formatted_string)

"""
What we did above on line 7 is that we stored the output of the function to "formatted_string"
so that the output could be used outside of the function. 
"""
