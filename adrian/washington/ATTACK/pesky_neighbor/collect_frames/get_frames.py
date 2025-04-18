import asyncio
import logging
import json

hosts = ["34.235.112.89", "54.86.219.63"]
host = hosts[1]
ports = [*range(2550,2554+1)]

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

    print(data)

    writer.close()
    await writer.wait_closed()
    print('------')

async def main():

    async with asyncio.TaskGroup() as tg:
        for port in ports[0], ports[1]:
            tg.create_task(tcp_echo_client(host, port))

    print("Checked all hosts and ports")


if __name__ == "__main__":
    asyncio.run(main())
