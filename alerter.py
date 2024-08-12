alert_failure_count = 0

def network_alert_stub(celcius):
    print_alert_message(celcius)
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    return 200

def print_alert_message(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    
def farenheit_to_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    return celcius
    
def alert_in_celcius(farenheit):
    celcius = farenheit_to_celcius(farenheit)
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1
        return True
    return False


alert_in_celcius(400.5)
alert_in_celcius(303.6)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
