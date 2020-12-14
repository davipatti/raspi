#!/usr/bin/env python3

"""
Set a sleep timer on a Sonos speaker.
Example:
    $ python sonos-sleep.py --name Bathroom --minutes 20
"""
import argparse

# 'Sonos controller' module
# pip install soco==0.20
import soco

parser = argparse.ArgumentParser("Set a sleep timer on a Sonos speaker")
parser.add_argument("--name", default="Bedroom", help="Speaker name. Default='Bedroom'")
parser.add_argument(
    "--minutes", default=30, type=float, help="Sleep timer length. Default=30"
)
args = parser.parse_args()

device = soco.discovery.by_name(args.name)

if not device:
    print("No device called '{}'".format(args.name))
    available = [device.player_name for device in soco.discover()]
    print("Available devices: {}".format(", ".join(available)))
    exit(1)

is_playing = device.get_current_transport_info()["current_transport_state"] == "PLAYING"

if not is_playing:
    print("{} not playing, doing nothing".format(args.name))
elif device.get_sleep_timer() is not None:
    print("Sleep timer on {} set already, doing nothing".format(args.name))
else:
    device.set_sleep_timer(args.minutes * 60)
