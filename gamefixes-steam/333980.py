"""Game fix for Akiba's Trip: Undead & Undressed"""

from protonfixes import util


def main() -> None:
    # BGM doesn't seem to play with winedmo for now, so let's use gst.
    util.set_environment('PROTON_MEDIA_USE_GST', '1')

    # Disable the devs' workarounds.
    # Otherwise audio is disabled and videos are flipped.
    util.protontricks('hidewineexports=enable')
