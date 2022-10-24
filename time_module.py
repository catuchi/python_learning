# epoch = a date and time from which a computer measures system time
#         (when your computer thinks time began (reference point))

import time

# to check my computer's epoch
# print(time.ctime(0))                  # convert a time expressed in seconds since epoch to a readable string

# print(time.time())                    # returns current seconds since epoch

# print(time.ctime(time.time()))        # get current date and time

# time_object = time.localtime()        # creates a time object of current date and time
# time_object_UTC = time.gmtime()       # time object in UTC
# # print(time_object)
# print(time_object_UTC)
# format = "%B %d %Y %H:%M:%S"                           # from python docs for strftime
# local_time = time.strftime(format, time_object)    # formats the time object to a readable string
# print(local_time)


# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y")         # parses a string representation of a time/date and return a time object
# print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)                        # accepts a time tuple object and creates a time string
print(time_string)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)                        # accepts a time tuple object and converts it to secs since epoch
print(time_string)
