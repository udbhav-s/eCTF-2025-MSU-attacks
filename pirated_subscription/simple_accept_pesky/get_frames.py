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

    frames = {}

    for i in range(5):
        # Get a frame
        ch_frame = await get_frame(host, ch0_port + i)
        frames[f"ch{i}_frame"] = ch_frame

    content = json.dumps(frames)

    with open("frames.json", "w") as file:
        file.write(content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="All Channel Frame Retriever"
    )
    parser.add_argument("-t", "--team", type=str, required=True, help="Name of the team")
    args = parser.parse_args()

    asyncio.run(retrieve_frames(args.team))


# Get an earlier channel 1 frame
