import asyncio
import json

async def test_channel_frame(host, port):
    try:
        reader, writer = await asyncio.open_connection(
        host, port)

        print(f"Testing port {port}")
    except:
        return

    data = await reader.readuntil(b"}")
    parsed = json.loads(data)
    decoded = bytes.fromhex(parsed["encoded"])

    if b"flag" in decoded:
        print(f"Raw frame contents found for port {host}:{port} - {decoded}")
        print(f"Len: {len(decoded)}")
    else:
        # print(f"No raw frame contents found for {port}")
        pass

    # print('Close the connection')
    writer.close()
    await writer.wait_closed()

async def main():
    # ports = [2554, 2555]

    hosts = ["34.235.112.89", "54.86.219.63"]
    ports = range(2000, 3000)

    # Reference
    # hosts = ["34.229.214.171"]
    # ports = range(2000, 2005)

    async with asyncio.TaskGroup() as tg:
        for host in hosts:
            for port in ports:
                tg.create_task(test_channel_frame(host, port))

    print("Checked all hosts and ports")


if __name__ == "__main__":
    asyncio.run(main())
