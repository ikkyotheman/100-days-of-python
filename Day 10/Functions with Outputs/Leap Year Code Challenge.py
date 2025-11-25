def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return print(True)
    else: return print(False)



leap_year(year=int(input("Enter a year: ")))
