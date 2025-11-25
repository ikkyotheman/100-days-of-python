def is_leap_year(year):
    """
    Year divisible by 4 unless divisible by 100 (not including divisible by 400)
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


answer = is_leap_year(1989)
print(answer)

