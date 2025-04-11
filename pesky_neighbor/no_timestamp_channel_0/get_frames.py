import sys

sys.path.append("../../")

from utils.get_frame import get_frame
import json
import argparse
import asyncio


async def retrieve_frames(team: str):
    team_channels = {}
    with open("../../utils/team_channels.json", "r") as f:
        team_channels = json.loads(f.read())

    if team not in team_channels:
        raise Exception(f"Team name '{team}' not found in team channels JSON!")

    team_info = team_channels[team]
    host = team_info["host"]
    ch0_port = team_info["base_port"]

    # Get a channel 1 frame
    ch0_frame1 = await get_frame(host, ch0_port)

    # Wait for a bit
    await asyncio.sleep(0.5)

    # Get a later channel 0 frame
    ch0_frame2 = await get_frame(host, ch0_port)

    assert ch0_frame2["timestamp"] > ch0_frame1["timestamp"]

    content = json.dumps({"ch0_frame2": ch0_frame1, "ch0_fram1": ch0_frame2})

    with open("frames.json", "w") as file:
        file.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pesky Neighbor Channel Frame Retriever"
    )
    parser.add_argument(
        "-t", "--team", type=str, required=True, help="Name of the team"
    )
    args = parser.parse_args()

    asyncio.run(retrieve_frames(args.team))


# Get an earlier channel 1 frame
