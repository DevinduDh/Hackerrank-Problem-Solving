s = "02:00:00PM"

x = s.split(":")
# print(s)
# print(x)

seconds = []
seconds_final = ""
hour = x[0]
minutes = x[1]

seconds = x[-1]
# print(seconds)
seconds_new = list(seconds)
# print(seconds_new)

seconds_new_1 = seconds_new[0:2]
# print(seconds_new_1)
for item in seconds_new_1:
    seconds_final += item
# print(seconds_final)


if seconds_new[-2] == 'P':
    if hour != '12':
        hour_new = int(hour) + 12
        hour_new1 = str(hour_new)
        print("{}:{}:{}".format(hour_new1, minutes, seconds_final))
    elif hour == '12':
        hour_new1 = '12'
        print("{}:{}:{}".format(hour_new1, minutes, seconds_final))
elif seconds_new[-2] == 'A':
    if hour == '12':
        hour_new1 = '00'
        print("{}:{}:{}".format(hour_new1, minutes, seconds_final))
    else:
        hour_new1 = hour
        print("{}:{}:{}".format(hour_new1, minutes, seconds_final))

# print("{}:{}".format(hour, minutes))
