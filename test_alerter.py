import alerter

def run_test_cases_alerter():
    alerter.alert_in_celcius(303.6)
    assert(alerter.alert_failure_count == 0)
    alerter.alert_in_celcius(200)
    assert(alerter.alert_failure_count == 0)
    alerter.alert_in_celcius(450)
    assert(alerter.alert_failure_count == 1)
    alerter.alert_in_celcius(100)
    assert(alerter.alert_failure_count == 1)
    
if __name__ == '__main__':
    run_test_cases_alerter()

print("All is well (maybe!)\n")
