import base64
from datetime import datetime

def get_timestamp():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime('%Y%m%d%H%M%s')

    return formatted_time

get_timestamp()