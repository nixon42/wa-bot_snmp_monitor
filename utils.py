
from datetime import datetime
from pytz import timezone


def get_wib_time():
    """
    Return current time in WIB timezone or +7 GMT
    """
    jakarta_tz = timezone('Asia/Jakarta')
    wib_time = datetime.now(jakarta_tz)

    return wib_time


def format_time(time: datetime) -> str:
    """
    Format datetime object
    """
    return time.strftime("%Y-%m-%d %H:%M")


MSG = """
*******************************
    !!!!! NOTIFIKASI !!!!!     
*******************************
💻 *OLT*        : OLT-2 (Gayam)
📍 *PON1 On/Off*: {0}/{1}
📍 *PON2 On/Off*: {2}/{3}
🔧 *STATUS*     : {4}
⏰ *WAKTU*      : {5}

------------------------------
"""

oids_data = {
    "PON1_Total": "1.3.6.1.4.1.50224.3.2.3.1.3.16777472",
    "PON2_Total": "1.3.6.1.4.1.50224.3.2.3.1.3.16777728",
    "PON1_Online": "1.3.6.1.4.1.50224.3.2.3.1.4.16777472",
    "PON2_Online": "1.3.6.1.4.1.50224.3.2.3.1.4.16777728",
    "PON1_Offline": "1.3.6.1.4.1.50224.3.2.3.1.5.16777472",
    "PON2_Offline": "1.3.6.1.4.1.50224.3.2.3.1.5.16777728",
}
