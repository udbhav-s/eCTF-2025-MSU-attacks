from get_frame import get_frame
import json
import argparse
import asyncio
import os

async def dump_frames(team: str, out_path: str):
    team_channels = {}
    with open(os.path.join(os.path.dirname(__file__), "team_channels.json"), "r") as f:
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

    with open(out_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="All Channel Frame Retriever")
    parser.add_argument(
        "-t", "--team", type=str, required=True, help="Name of the team"
    )
    parser.add_argument(
        "-o", "--out_path", type=str, default="frames.json", help="Output path for frames JSON"
    )
    args = parser.parse_args()

    asyncio.run(dump_frames(args.team, args.out_path))