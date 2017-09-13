import array
import pulseio
import board
import time

# A lookup table of morse codes and characters.
MORSE_CODE_LOOKUP = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
}


VALID_VALUES = (1000, 2000, 4000, 8000)


def normalise(raw):
    """
    A generator function that yields normalised items from the raw input.
    """
    for val in raw:
        rounded_val = round(val/1000) * 1000
        if rounded_val in VALID_VALUES:
            yield rounded_val


def get_character(tokens):
    """
    Given a list of tokens (Morse code dahs and dits represented as "-" and
    "."), return the related character or "?" if there's no match.
    """
    return MORSE_CODE_LOOKUP.get(''.join(tokens), "?")


def decode_message(normalised):
    """
    Given a source of normalised incoming values, returns a string
    representation of the message contained therein.
    """
    # Split the incoming normalised values into words, characters and tokens.
    words = []
    characters = [] 
    tokens = [] 
    for val in normalised:
        if val == 8000:
            # A new word.
            # Store away the old tokens and characters and reset state.
            if tokens:
                characters.append(get_character(tokens))
            if characters:
                words.append(''.join(characters))
            tokens = []
            characters = []
        elif val == 4000:
            # A new character.
            # Store away and reset the tokens of the previous character.
            if tokens:
                characters.append(get_character(tokens))
            tokens = []
        elif val == 2000:
            # A dah (represented as '-')
            tokens.append('-')
        elif val == 1000:
            # A dit token (represented as '.')
            tokens.append('.')
    return ' '.join(words).strip()


ir_in = pulseio.PulseIn(board.REMOTEIN, maxlen=512, idle_state=False)


while True:
    while len(ir_in) == 0:
        time.sleep(1)
    ir_in.pause()
    raw = [ir_in[i] for i in range(len(ir_in))]
    normalised = normalise(raw)
    msg = decode_message(normalised)
    if msg:
        print(msg)
    ir_in.clear()
    ir_in.resume()
