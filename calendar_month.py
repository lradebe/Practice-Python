def calendar_month():
    """This function returns the calendar for a user given Year and Month"""
    import calendar

    year, month = int(input("YEAR: ")), int(input("MONTH: "))
    print(calendar.month(year, month))
calendar_month()
