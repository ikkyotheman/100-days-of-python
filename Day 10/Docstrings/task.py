def format_name(f_name, l_name):
    """

    :param f_name: This is for the first name
    :param l_name: This is for the second
    :return: This is the return
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)
print(formatted_name)
