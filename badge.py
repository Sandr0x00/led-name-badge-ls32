
from dataclasses import dataclass
from lednamebadge import SimpleTextAndIcons, LedNameBadge, split_to_ints
from enum import Enum
from array import array

creator = SimpleTextAndIcons()


class Blink:
    YES = 1
    NO = 0

class Ant:
    YES = 1
    NO = 0

class Mode:
    SCROLL_LEFT = 0
    SCROLL_RIGHT = 1
    SCROLL_UP = 2
    SCROLL_DOWN = 3
    CENTERED = 4
    ANIMATION = 5
    DROP_DOWN = 6
    CURTAIN = 7
    LASER = 8

@dataclass
class Data:
    message: tuple[array, int]
    speed: int = 1
    mode: int = Mode.CENTERED
    blink: int = Blink.NO
    ant: int = Ant.NO


sandr0 = [
    0b00000000000000000000000000000000000000000000,
    0b00000000000000000000000000110000000000111110,
    0b00000000000000000000000000110000000001100011,
    0b00000000000000000000000000110000000001100111,
    0b01111100011100110111000111110110111101101111,
    0b11000110000110011001101100110011101101111011,
    0b01110000011110011001101100110011000001110011,
    0b00011100100110011001101100110011000001100011,
    0b11000110100110011001101100110011000001100011,
    0b01111100011011011001100111011011100000111110,
    0b00000000000000000000000000000000000000000000,
]

a = [
    0b10101010101010101010101010101010101010101010,
    0b01010101010101010101010101010101010101010101,
    0b10101010101010101010101010101010101010101010,
    0b01010101010101010101010101010101010101010101,
    0b10101010101010101010101010101010101010101010,
    0b01010101010101010101010101010101010101010101,
    0b10101010101010101010101010101010101010101010,
    0b01010101010101010101010101010101010101010101,
    0b10101010101010101010101010101010101010101010,
    0b01010101010101010101010101010101010101010101,
    0b10101010101010101010101010101010101010101010,
]

a = [
    0b11001100110011001100110011001100110011001100,
    0b11001100110011001100110011001100110011001100,
    0b00110011001100110011001100110011001100110011,
    0b00110011001100110011001100110011001100110011,
    0b11001100110011001100110011001100110011001100,
    0b11001100110011001100110011001100110011001100,
    0b00110011001100110011001100110011001100110011,
    0b00110011001100110011001100110011001100110011,
    0b11001100110011001100110011001100110011001100,
    0b11001100110011001100110011001100110011001100,
    0b00110011001100110011001100110011001100110011,
]

a = [
    0b11100011100011100011100011100011100011100011,
    0b11100011100011100011100011100011100011100011,
    0b11100011100011100011100011100011100011100011,
    0b00011100011100011100011100011100011100011100,
    0b00011100011100011100011100011100011100011100,
    0b00011100011100011100011100011100011100011100,
    0b11100011100011100011100011100011100011100011,
    0b11100011100011100011100011100011100011100011,
    0b11100011100011100011100011100011100011100011,
    0b00011100011100011100011100011100011100011100,
    0b00011100011100011100011100011100011100011100,
]



# a = [
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
#     0b00000000000000000000000000000000000000000000,
# ]

pacman_open = [
    0b00000000,
    0b00011100,
    0b00100010,
    0b01001001,
    0b10000010,
    0b10000100,
    0b10000010,
    0b01000001,
    0b00100010,
    0b00011100,
    0b00000000,
]

pacman_closed = [
    0b00000000,
    0b00011100,
    0b00100010,
    0b01001001,
    0b10000001,
    0b10000111,
    0b10000001,
    0b01000001,
    0b00100010,
    0b00011100,
    0b00000000,
]

dot = [
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00010000,
    0b00101000,
    0b00010000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
]


# scene = []

# p = False
# pos = 0
# scenes = 4
# for row in range(11):
#     val = 0
#     for s in range(scenes):
#         for a in range(44, 2, -2):
#             pac = pacman_open if p else pacman_closed
#             p = not p
#             val = pac[row] << a

#     scene.append(val)

# a = [
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
#     0b11111111111111111111000000000000000000000000,
# ]

data = [
    Data(creator.bitmap_img("gfx/sandr0.png")),
    # Data(creator.bitmap_bits(a, 44)),
    Data(creator.bitmap_img("gfx/pacman.png"), speed=8),
    # Data(creator.bitmap("4")),
    # Data(creator.bitmap("5")),
    # Data(creator.bitmap("6")),
    # Data(creator.bitmap("7")),
    # Data(creator.bitmap("8")),
]

# assert len(data) == 8

lengths = [d.message[1] for d in data]
speeds = [d.speed for d in data]
modes = [d.mode for d in data]
blinks = [d.blink for d in data]
ants = [d.ant for d in data]
brightness = 100

buf = array('B')
buf.extend(LedNameBadge.header(lengths, speeds, modes, blinks, ants, brightness))

for d in data:
    buf.extend(d.message[0])

LedNameBadge.write(buf, "libusb")