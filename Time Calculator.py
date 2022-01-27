def add_time(time, duration, day = None):
    day_map = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday":6
    }
    start_time, midday = time.split()
    t_hour, t_minutes = start_time.split(':')
    t_hour = int(t_hour)
    t_minutes = int(t_minutes)
    if midday == "PM":
        t_hour += 12
    d = duration.split()
    duration_hour_minutes = d[0].split(":")
    duration_hour = int(duration_hour_minutes[0])
    duration_minutes = int(duration_hour_minutes[1])
    total_minutes = t_minutes + duration_minutes
    actual_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    total_hour = t_hour + duration_hour + extra_hours
    actual_hour = (total_hour % 24) % 12
    if actual_hour == 0:
        actual_hour = 12
    actual_hour = str(actual_hour)
    total_day = (total_hour // 24)
    actual_midday = ""
    if (total_hour % 24) <= 11:
        actual_midday = "AM"
    else:
        actual_midday = "PM"
    if actual_minutes <= 9:
        actual_minutes = "0" + str(actual_minutes)
    else:
        actual_minutes = str(actual_minutes)
    time_stamp = actual_hour + ":" + actual_minutes + ' ' + actual_midday
    if day == None:
        if total_day == 0:
            return time_stamp
        if total_day == 1:
            return time_stamp + ' (next day)'
        return time_stamp + ' (' + str(total_day) + ' days later)'
    else:
        actual_day = (day_map[day.lower().capitalize()] + total_day) % 7
        for i, j in day_map.items():
            if j == actual_day:
                actual_day = i
                break
        if total_day == 0:
            return time_stamp + ', ' + actual_day
        if total_day == 1:
            return time_stamp + ', ' + actual_day + ' (next day)'
        return time_stamp + ', ' + actual_day + ' (' + str(total_day) + ' days later)'

print(add_time("11:06 PM", "120:54", "Saturday"))