from datetime import datetime



def Get_Houer():

    """ return current houer    """

    now = datetime.now()
    h = str(now.hour)
    m = str(now.minute)
    s = str(now.second)

    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    if len(s) == 1:
        s = '0' + s

    hour = h + ":" + m + ":" + s
    return hour
