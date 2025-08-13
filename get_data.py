import asyncio
from pysnmp.hlapi.v3arch.asyncio import *
from utils import oids_data, format_time, get_wib_time

async def get_oid_data(snmp_server: str, oids: list[str]) -> dict[str, str]:
    snmp_engine = SnmpEngine()
    transport = await UdpTransportTarget.create((snmp_server, 161))
    result = oids_data.copy()

    args = [ObjectType(ObjectIdentity(oid)) for oid in oids]

    errorIndication, errorStatus, _, varBinds = await get_cmd(
        snmp_engine,
        CommunityData("public", mpModel=1),  # SNMP v2c
        transport,
        ContextData(),
        *args
    )

    if errorIndication:
        print("Error:", errorIndication)
        raise Exception(errorIndication)
    elif errorStatus:
        print("SNMP error:", errorStatus.prettyPrint())
        raise Exception(errorStatus.prettyPrint())
    else:
        for name, val in varBinds:
            for key, oid in oids_data.items():
                if str(name) == oid:
                    result[key] = str(val)

    snmp_engine.close_dispatcher()
    return result

if __name__ == "__main__":
    oids = list(oids_data.values())
    data = asyncio.run(get_oid_data(oids))
    for key, value in data.items():
        print(f"{key}: {value}")
