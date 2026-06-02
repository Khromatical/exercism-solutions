def leap_year(year):
    extra_day = False
    year_4 = year % 4 == 0
    year_100 = year % 100 == 0
    year_400 = year % 400 == 0
    if year_4:
        extra_day = True
    if year_100:
        if year_400:
            extra_day = True
        else:
            extra_day = False
    return extra_day