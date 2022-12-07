alert_failure_count = 0

def network_alert(celcius):
    if celcius <= 200:
        return 200
    else:
        return 500
    
      
def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert(celcius)
    
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 1
