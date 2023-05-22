lista_bledów = []
alert_system = 'console'
error = 'critical'
error_message = "Stało sie coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'critical':
        lista_bledów.append('critical')

print(lista_bledów)
