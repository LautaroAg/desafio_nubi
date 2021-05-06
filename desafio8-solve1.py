from datetime import datetime, timedelta
from sys import exit


def generateLastDaysPaths(date, days, url='https://importantdata@location/'):
    """
    Resuelve el desafio 8. Primero valida los datos de entrada y luego retorna 
    la lista correspondiente,  para ello itera en el rango de los dias y los va restando
    de la fecha original. Finalmente invierte la lista obtenida
    """
    if url[-1] != '/': url = f'{url}/'
    if not isinstance(days,int) or days < 0: exit("whyareyoulikethis")
    try:
        validated_date = datetime.strptime(date, '%Y%m%d')
    except:
        exit('Date format must be YYYYmmdd')
    
    date_format = '%Y/%m/%d' # Es una variable porque tira syntax error sino *shrugs*
    return [
        f'{url}{datetime.strftime((validated_date - timedelta(days=i)), date_format)}/'
        for i in range(days)
        ][::-1]

f = generateLastDaysPaths('20200410',10)
([print(each) for each in f])
print(len(f))
