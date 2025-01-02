"""
    .DESCRIPTION
        This library is used to display a message with a timestamp. The message can be an alert, warning, or error.

    .NOTES
        [Original Author]
            o Michael Arroyo
        [Original Build Version]
            o 1.0.0.20240822 (Major.Minor.Patch.Date<YYYYMMDD>)
        [Latest Author]
            o Michael Arroyo
        [Latest Build Version]
            o 1.0.0.20240822 (Major.Minor.Patch.Date<YYYYMMDD>)
        [Comments]
            o
        [Python Compatibility / Tested On]
            o Python 3.10.14
        [Forked Project]
            o
        [Dependencies]
            o datetime # The datetime module supplies classes for manipulating dates and times
            o time # The time module provides various time-related functions

	.Build Notes
		o 1.0.0.20240822 -
			[Michael Arroyo] Initial Build
        o 2.0.0.20241217
            [Michael Arroyo] Change the function name to timestamp
            [Michael Arroyo] Add time lib
            [Michael Arroyo] Add a file logging option

    .EXAMPLE
        Command: timestamp('This is a warning message for X', 'warning')
        Description: This will display a Warning message with a timestamp.
        Notes:
        Output: [!] 2024-08-22 10:18:35: This is a warning message for X

    .EXAMPLE
        Command: timestamp('This is a warning message for X', 'warning', 'logs/app.log')
        Description: The timestamp message will also be appended to the logs/app.log file
        Notes:
        Output: [!] 2024-08-22 10:18:35: This is a warning message for X
"""


import datetime # The datetime module supplies classes for manipulating dates and times
from time import gmtime, strftime # The time module provides various time-related functions

def timestamp(message, message_type='alert', logfile=None):
    message_types = ['alert', 'warning', 'error']
    if message_type not in message_types:
        raise ValueError("Invalid message type. Expected one of: %s" % message_types)
    if message_type == 'alert':
        current_message = "[+] %s: %s" % (strftime("%Y-%m-%d %H:%M:%S %z"), message)
    if message_type == 'warning':
        current_message = "[!] %s: %s" % (strftime("%Y-%m-%d %H:%M:%S %z"), message)
    if message_type == 'error':
        current_message = "[-] %s: %s" % (strftime("%Y-%m-%d %H:%M:%S %z"), message)

    print(current_message)
    if not logfile is None:
        f = open(logfile, "a")
        f.write(f"{current_message}\n")
        f.close()