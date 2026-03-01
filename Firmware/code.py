#KMK - by gethin101
from kmk.bootcfg import bootcfg

bootcfg(
    usb_id={'manufacturer': "Gethin101", 'product': "Gethin-75"},
)


import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC, make_key

MAC1 = make_key("MAC1")  # (back)
MAC2 = make_key("MAC2")  # (pause/play)
MAC3 = make_key("MAC3")  # (next)
MAC5 = make_key("MAC5")  # (vol down)
MAC6 = make_key("MAC6")  # (vol up)
MAC7 = make_key("MAC7")  # (lock)
MAC8 = make_key("MAC8")  # (file explorer)
MAC9 = make_key("MAC9")  # (task manager)


def handle_macro(keycode, keyboard):
    if keycode == MAC1:
        keyboard.tap_key(KC.MPRV)

    elif keycode == MAC2:
        keyboard.tap_key(KC.MPLY)

    elif keycode == MAC3:
        keyboard.tap_key(KC.MNXT)

    elif keycode == MAC5:
        keyboard.tap_key(KC.VOLD)

    elif keycode == MAC6:
        keyboard.tap_key(KC.VOLU)

    elif keycode == MAC7:
        keyboard.tap_key(KC.LGUI, KC.L)

    elif keycode == MAC8:
        keyboard.tap_key(KC.LGUI, KC.E)

    elif keycode == MAC9:
        keyboard.tap_key(KC.LCTRL, KC.LSHIFT, KC.ESC)


class Gethin75(KMKKeyboard):
    row_pins = (
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
    )

    col_pins = (
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
        board.GP20,
        board.GP21,
        board.GP22,
        board.GP26,
        board.GP27,
    )

    #switch if diodes wrong way
    diode_orientation = DiodeOrientation.COL2ROW


keyboard = Gethin75()



keyboard.keymap = [
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4,
        KC.F5, KC.F6, KC.F7, KC.F8,
        KC.F9, KC.F10, KC.F11, KC.F12,
        MAC1, MAC2, MAC3, KC.NO,
    ],

    [
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8,
        KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.INS, KC.HOME, KC.PGUP,
    ],

    [
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I,
        KC.O, KC.P, KC.LBRC, KC.RBRC,
        KC.ENTER, KC.DEL, KC.END, KC.PGDN,
    ],

    [
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K,
        KC.L, KC.SCLN, KC.QUOT, KC.NUHS,
        MAC5, MAC6, MAC7, KC.NO,
    ],

    [
        KC.LSFT, KC.NUBS, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M,
        KC.COMMA, KC.DOT, KC.SLSH, KC.RSFT,
        MAC8, KC.UP, MAC9, KC.NO,
    ],

    [
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC,
        KC.RALT, KC.RGUI, KC.APP, KC.RCTL,
        KC.LEFT, KC.DOWN, KC.RIGHT,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ],
]


@keyboard.hook
def macro_hook(key, keyboard):
    handle_macro(key, keyboard)


if __name__ == '__main__':
    keyboard.go()
