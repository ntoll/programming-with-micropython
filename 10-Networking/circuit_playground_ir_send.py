import array
import pulseio
import board

# A lookup table of morse codes and characters.
MORSE_CODE_LOOKUP = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def encode_message(msg):
    words = msg.split(' ')
    message_buffer = []
    for word in words:
        message_buffer.extend([8000, 8000, ])  # Indicates a new word.
        for character in word:
            message_buffer.extend([4000])  # Indicates a new letter.
            for val in MORSE_CODE_LOOKUP[character]:
                if val == '-':
                    message_buffer.extend([2000])  # Indicates a dah.
                else:
                    message_buffer.extend([1000])  # Indicates a dit.
    if words:
        message_buffer.extend([8000, 8000, ])  # Indicates end of message
    return array.array('H', message_buffer)


ir_led = pulseio.PWMOut(board.REMOTEOUT, frequency=38000, duty_cycle=2**15)
ir_out = pulseio.PulseOut(ir_led)
message = encode_message("HELLO WORLD")
ir_out.send(message)
