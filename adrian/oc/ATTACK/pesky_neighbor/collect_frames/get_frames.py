import asyncio
import logging
import json

# OC
hosts = ["34.235.112.89", "54.86.219.63"]
host = hosts[1]
base_port = 2850
ports = [*range(base_port,base_port+4+1)]

async def tcp_echo_client(host, port):
    try:
        reader, writer = await asyncio.open_connection(
        host, port)

        print(f"Testing port {port}")
    except:
        return

    logging.warn(f'{port} open')

    data = await reader.readuntil(b"}")
    parsed = json.loads(data)
    decoded = bytes.fromhex(parsed["encoded"])

    print(f'ch{port-base_port}_frame = {data.decode()}')

    writer.close()
    await writer.wait_closed()
    #print('#######')

async def main():

    async with asyncio.TaskGroup() as tg:
        for port in ports:
            tg.create_task(tcp_echo_client(host, port))

    print("Checked all hosts and ports")


if __name__ == "__main__":
    asyncio.run(main())
