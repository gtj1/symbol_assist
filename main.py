import pynput.keyboard
import keyboard
import json
import threading

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

def thread_job():
    print("running ...")
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def main():
    try:
        thread = threading.Thread(target=thread_job)
        thread.daemon = True
        thread.start()
        while thread.is_alive():
            thread.join(1)  # time out not to block KeyboardInterrupt
    except KeyboardInterrupt:
        print("exit ...")
        exit()


if __name__ == "__main__":
    main()
