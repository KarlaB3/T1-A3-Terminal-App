# Call today's date
def today_date():
    from datetime import date
    date_today = date.today()
    return date_today.strftime('%d-%m-%y')

# Call yesterday's date
def yesterday_date():
    from datetime import date
    from datetime import timedelta
    date_today = date.today()
    date_yesterday = date_today - timedelta(days = 1)
    return date_yesterday.strftime('%d-%m-%y')