import pynput.keyboard
import keyboard
from symbols import symbols

# 用于暂存输入的转义字符
current_input = ""


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
                # keyboard.send("backspace")
        elif current_input:
            if key.char:
                current_input += key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            return
        elif key == pynput.keyboard.Key.backspace:
            current_input = current_input[:-1]
        elif key == pynput.keyboard.Key.shift:
            return
        else:
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
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
