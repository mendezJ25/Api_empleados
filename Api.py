import requests as requests


def lista_empleados(url):
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Chrome/114.0.0.0',
    })
    response= requests.get(url, headers=headers)
    if response.status_code == 200 :
        data = response.json()

    # print(data)


        #LA CANTIDAD DE EMPLEADOS
        total_empleados = len(data['data'])
        print("Total de empleados:",total_empleados)

        #EL PROMEDIO DE SALARIO DE EMPLEADOS
        total_salario = sum(float(empleado['employee_salary']) for empleado in data['data'])
        promedio_salario = round(total_salario / total_empleados,2)
        print("El promedio de salario de empleados es:",promedio_salario)

        #EL PROMEDIO DE EDAD DE EMPLEADOS
        total_edades = sum(int(empleado['employee_age'])for empleado in data['data'])
        promedio_edades = total_edades/total_empleados
        print("El promedio de edades de los empleados es:",promedio_edades)

        #SALARIO MINIMO y MAXIMO
        salarios = [float(empleado['employee_salary']) for empleado in data['data']]
        min_salario = min(salarios)
        max_salario = max(salarios)
        print("El salario minimo es:", min_salario ,"y el salario maximo es: ", max_salario)

        #EDAD MINIMA Y MAXIMA
        edad = [int(empleado['employee_age']) for empleado in data['data']]
        min_edad = min(edad)
        max_edad = max(edad)
        print("La menor edad entre los empleados es:",min_edad, "y la mayor edad entre los empleados es:",max_edad)


if __name__ == '__main__':
    url = 'https://dummy.restapiexample.com/api/v1/employees'
    lista_empleados(url)

