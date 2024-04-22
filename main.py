import pynput.keyboard
import keyboard
import json
import time

# 用于暂存输入的转义字符
current_input = ""

with open("symbols.json", encoding="utf8") as file:
    s = file.read()
    symbols = json.loads(s)


def symbol_input(input_char):
    if input_char in symbols:
        return symbols[input_char]
    else:
        return input_char


def on_press(key):
    global current_input
    try:
        if key.char == "\\":
            if current_input != "\\":
                current_input = "\\"
            else:
                current_input = ""
                keyboard.send("backspace")
        elif current_input:
            if key.char:
                current_input += key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            return
        if key == pynput.keyboard.Key.backspace:
            current_input = current_input[:-1]
        elif key in [pynput.keyboard.Key.esc, pynput.keyboard.Key.enter]:
            current_input = ""


def on_release(key):
    global current_input
    if key == pynput.keyboard.Key.space:
        if current_input in symbols:
            for i in range(len(current_input) + 1):
                keyboard.send("backspace")
            keyboard.write(symbols[current_input])
        current_input = ""
        return True


def main():
    print("running ...")
    th = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
    th.start()
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        th.stop()
        exit(0)


if __name__ == "__main__":
    main()
