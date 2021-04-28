import csv

def desafio3(source='./currenciesRaw', output='./currenciesDeserialized'):
    """
    Resuelve el desafio 3, toma como precondicion el formato del archivo provisto,
    especialmente el hecho de que la hora se encuentra en el tercer campo,
    se puede realizar para que chequee por cada campo si eso es una hora, pero me resulta un
    desperdicio de procesamiento.
    """
    with open(source, 'r') as raw_file:
        with open(output,'w') as deserialized:
            writer  = csv.writer(deserialized,delimiter=',',quotechar='"')
            writer.writerow(
                ['country','dateTrack','currency','dollarToLocal','localToDollar','site']
                )
            for line in raw_file.readlines():
                line = line.replace('\n','').split('\t')  # Parseo la linea
                del line[2]     # Elimino la fecha y hora
                line = list(filter(lambda field: field != '0', line))
                new_line = []
                [
                    new_line.append(field) 
                    for field in line if field not in new_line or field == '1'
                    ]
                # Elimino repetidos manteniendo el orden de la lista, 
                # mantengo el repetido del 1 por la conversion del dolar 1=1
                new_line[3] = round(float(new_line[3]),2)
                new_line[4] = round(float(new_line[4]),2) # redondeo a 2 decimales                 
                writer.writerow(new_line)

desafio3()