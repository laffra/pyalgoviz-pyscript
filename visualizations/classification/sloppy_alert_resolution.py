"""
 Sloppy Alert Resolution 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sloppy Alert Resolution"
__author = "francis.moloney@zalando.ie"

def __algorithm():
    def isFailure(num):
        return num != 0

    def value_series(count):
        return [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1]

    desired_sample_count = 20
    historical_values = value_series(desired_sample_count)
    loop_limit = min(len(historical_values), desired_sample_count)

    alert_condition = False
    count = 0
    for i in range(loop_limit):
        failed = isFailure(historical_values[i])
        if failed:
            count = count - 3
        else:
            count = count + 1

        if count <= -3:
            alert_condition = True
            break
        elif i >= 2 and count >= 2:
            break

def __visualization():
    X, Y, D = 50, 150, 40

    # Alog Description
    rect(X, 42, 415, 40, '#333')
    text(X+15, 72, 'Sloppy Alert Resolution', 30, color='lightblue')

    # Input Data Title
    rect(18, 115, 400, 20, 'black')
    text(20, 130, 'Historical Data Set (0 is Pass, 1 is Fail)', 15, color='lightblue')

    for j in range(len(historical_values)):
        gx = X+(j*21)
        gy = Y
        color = 'black'
        if j == i: color = 'pink'
        rect(gx, gy, 30, 30, color)
        text(gx+2, gy+22, historical_values[j], 25, color='aqua')

    # Current Fail Count
    thresholdColor = 'black'
    if alert_condition:
        thresholdColor = 'red'
    rect(18, 230, 400, 20, thresholdColor)
    text(20, 245, "Count: {}".format(count), 15, color='lightblue')

    # Overall Result
    rect(18, 260, 400, 20, 'black')
    text(20, 275, "Alert Result: {}".format(alert_condition), 15, color='lightblue')

    # Operation Explained
    if count > -3:
        operation = "Evaluating if history trends to success or failure"
    else:
        operation = "Too many recent failures, alert should remain active."
    rect(18, 200, 400, 20, 'brown')
    text(20, 215, operation, 15, color='lightblue')