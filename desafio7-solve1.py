from datetime import datetime
from sys import exit


def generateMonthlyPathList(year, month, day, url='https://importantdata@location.com.ar/'):
    """
    Devuelve una lista con todas las url de la forma url/year/month/days
    con todos los dias desde el primero hasta el pasado como parametro
    """
    if url[-1] != '/': url = f'{url}/'
    try:
        datetime.strptime(f'{year}/{month}/{day}', '%Y/%m/%d')
    except:
        exit('Incorrect date values')
    return [
        f'{url}{"{:4d}/{:02d}/{:02d}/".format(int(year),int(month),int(each_day))}'
        for each_day in range(1,int(day)+1) 
    ]


[ print(e) for e in (generateMonthlyPathList("2021","05","17")) ]
