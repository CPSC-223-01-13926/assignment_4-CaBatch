import json
import calendar


def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def max_temperature(data, date):
    x = 0
    for key in data:
        if key[0:8] == date:
            if data[key]['t'] > x:
                x = data[key]['t']
    
    return x


def min_temperature(data, date):
    x = 9999
    for key in data:
        if key[0:8] == date:
            if data[key]['t'] < x:
                x = data[key]['t']

    return x


def max_humidity(data, date):
    x = 0
    for key in data:
        if key[0:8] == date:
            if data[key]['h'] > x:
                x = data[key]['h']

    return x


def min_humidity(data, date):
    x = 9999
    for key in data:
        if key[0:8] == date:
            if data[key]['h'] < x:
                x = data[key]['h']

    return x


def tot_rain(data, date):
    sum = 0
    for key in data:
        if key[0:8] == date:
            sum += data[key]['r']

    return sum


def report_daily(data, date):
    report =          "========================= DAILY REPORT ========================\n"
    report = report + "Date                      Time  Temperature  Humidity  Rainfall\n"
    report = report + "====================  ========  ===========  ========  ========\n"

    for key in data:
        if key[0:8] == date:
            m = calendar.month_name[int(key[4:6])] + " " + str(int(key[6:8])) + ", " + str(int(key[0:4]))
            time = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            temp = data[key]['t']
            humidity = data[key]['h']
            rainfall = data[key]['r']
            
            report += f'{m:22}{time:8}{temp:13}{humidity:10}{rainfall:10.2f}' + '\n'
    return report


def report_historical(data):
    report =          "============================== HISTORICAL REPORT ===========================\n"
    report = report + "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    report = report + "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    report = report + "====================  ===========  ===========  ========  ========  ========\n"

    h = ''

    for key in data:
        if h == key[0:8]:
            continue
        else:
            h = key[0:8]
            m = calendar.month_name[int(h[4:6])] + " " + str(int(h[6:8])) + ", " + str(int(h[0:4]))
            min_temp = min_temperature(data, h)
            max_temp = max_temperature(data, h)
            min_humid = min_humidity(data, h)
            max_humid = max_humidity(data, h)
            rain = tot_rain(data, h)

            report += f'{m:20}{min_temp:13}{max_temp:13}{min_humid:10}{max_humid:10}{rain:10.2f}' + "\n"

    return report