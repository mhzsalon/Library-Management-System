# Function to get date
def date():
    import datetime
    now = datetime.datetime.now
    return str(now().date())


# Function to get Time
def time():
    import datetime
    time_now = datetime.datetime.now
    return str(time_now().time())

