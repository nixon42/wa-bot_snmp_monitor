from whatsapp_api_client_python import API
from get_data import get_oid_data
from utils import get_wib_time, format_time, MSG, oids_data
import os


# Load environment variables
SNMP_SERVER = os.getenv('SNMP_SERVER')
ID_INSTANCE = os.getenv('ID_INSTANCE')
API_TOKEN_INSTANCE = os.getenv('API_TOKEN_INSTANCE')
CHAT_ID = os.getenv('CHAT_ID')
if not SNMP_SERVER or not ID_INSTANCE or not API_TOKEN_INSTANCE or not CHAT_ID:
    raise ValueError(
        "Environment variables SNMP_SERVER, ID_INSTANCE, API_TOKEN_INSTANCE, and CHAT_ID must be set.")

greenAPI = API.GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


async def main():
    oids = list(oids_data.values())
    current_time = get_wib_time()

    try:
        data = {
            "PON1_Total": "10",
            "PON2_Total": "NULL",
            "PON1_Online": "1",
            "PON1_Offline": "9",
            "PON2_Online": "NULL",
            "PON2_Offline": "NULL",
        }
        # data = await get_oid_data(SNMP_SERVER, oids)
        print("Data retrieved:", data)
        # Simulate an error for testing
        # raise Exception("Simulated error for testing purposes")
    except Exception as e:
        print("Error retrieving SNMP data:", e)
        message = "Error retrieving SNMP data, OLT offline."
        msg = MSG.format(
            'N/A',
            'N/A',
            'N/A',
            'N/A',
            message,
            format_time(current_time)
        )
        try:
            greenAPI.sending.sendMessage(CHAT_ID, msg)
            return  # Exit the function after sending the error message
        except Exception as e:
            print(f"Failed to send WhatsApp message: {e}")

    if int(data['PON1_Offline']) >= 0.8 * int(data['PON1_Total']):
        message = "PON1 Offline 80%."
        msg = MSG.format(
            data.get('PON1_Online', 'NULL'),
            data.get('PON1_Offline', 'NULL'),
            data.get('PON2_Online', 'NULL'),
            data.get('PON2_Offline', 'NULL'),
            message,
            format_time(current_time)
        )
        try:
            greenAPI.sending.sendMessage(CHAT_ID, msg)
        except Exception as e:
            print(f"Failed to send WhatsApp message: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
