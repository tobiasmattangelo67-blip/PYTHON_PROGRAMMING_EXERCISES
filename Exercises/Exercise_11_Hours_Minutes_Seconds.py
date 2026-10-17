
"""
day: 86400
hour: 3600
minute: 60
"""

def getHoursMinutesSeconds(totalSeconds):
    day = 0
    hour = 0
    minute = 0
    seconds = 0

    if totalSeconds == 0:
        return (f"{totalSeconds}s")

    if totalSeconds >= 86400:
        day = totalSeconds // 86400
        totalSeconds -= 86400 * day

    hour = (totalSeconds % 86400) // 3600
    totalSeconds -= 3600 * hour

    minute = (totalSeconds % 3600) // 60
    totalSeconds -= 60 * minute

    seconds = totalSeconds % 60


    time = []

    if day > 0:
        time.append(f"{day}d")
    if hour > 0:
        time.append(f"{hour}h")
    if minute > 0:
        time.append(f"{minute}m")
    if seconds > 0:
        time.append(f"{seconds}s")

    return ' '.join(time)

    # strTime = ''

    # for index in time:
    #     strTime += (f"{index} ")

# assert getHoursMinutesSeconds(30) == '30s' 
# assert getHoursMinutesSeconds(60) == '1m' 
# assert getHoursMinutesSeconds(90) == '1m 30s' 
# assert getHoursMinutesSeconds(3600) == '1h' 
# assert getHoursMinutesSeconds(3601) == '1h 1s'
# assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
# assert getHoursMinutesSeconds(90042) == '25h 42s'
# assert getHoursMinutesSeconds(0) == '0s'

# for index in (getHoursMinutesSeconds(90042)):
#     print(index, end=' ')


