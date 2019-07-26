from emoji.unicode_codes import EMOJI_UNICODE
import random

chars = [v for v in EMOJI_UNICODE.values() if len(v) == 1] # limit to single code-point emojis

def generate_identifier(length=3):
    """Generates an identifier of a given length for an image. Not guaranteed to be unique."""
    return "".join([random.choice(chars) for x in range(length)])
