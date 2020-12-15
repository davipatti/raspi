#!/usr/bin/env python3

# sonos-play.py

import argparse
import soco

parser = argparse.ArgumentParser("Press play on a Sonos speaker")
parser.add_argument("--name", default="Bedroom", help="Speaker name. Default='Bedroom'")
args = parser.parse_args()

device = soco.discovery.by_name(args.name)

if not device:
    print("No device called '{}'".format(args.name))
    available = [device.player_name for device in soco.discover()]
    print("Available devices: {}".format(", ".join(available)))
    exit(1)

is_playing = device.get_current_transport_info()["current_transport_state"] == "PLAYING"

if not is_playing:
    device.play()