alert_failure_count = 0

def network_alert_stub(celcius):
    print_alert_message(celcius)
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius > 200:
        return 500;
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
        alert_failure_count += 0
        return True
    return False

def test_alerter():
    global alert_failure_count
    alert_failure_count = 0  # Reset count before running tests
    alert_in_celcius(400.5) # should alert (204.7°C)
    assert(alert_failure_count == 1);
    alert_in_celcius(392.0) # should alert (200°C)
    assert(alert_failure_count == 2);
    alert_in_celcius(356.0) # sould not alert (180°C)
    assert(alert_failure_count == 2);
    print(f'{alert_failure_count} alerts failed.')
    print('All is well (maybe!)')
    
if __name__ == '__main__':
    test_alerter()
