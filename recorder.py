from pynput import mouse, keyboard
from datetime import datetime

class Monitor:
    def __init__(self):
        self.clk_cnt = 0
        self.kbd_str = ''
        self.begin = datetime.now()

    def on_click(self,x,y,button,pressed):
        if pressed:
            self.clk_cnt += 1
    
    def on_press(self, key):
        try:
            self.kbd_str += key.char
        except AttributeError:
            self.kbd_str += ' '

    def genarate_result(self):
        self.rst = '\n------------------------------\n'

        self.rst += 'From ' + str(self.begin)[:-7]
        self.rst += ' to ' + str(self.end)[:-7] + '\n'

        self.rst += 'duration: ' 
        self.rst += str(int((self.end - self.begin).total_seconds()))
        self.rst += ' sec \n'

        self.rst += 'clicks: ' + str(self.clk_cnt) + '\n'
        self.rst += 'key board hits: ' + str(len(self.kbd_str)) + '\n'
        self.rst += 'words: ' + str(len(self.kbd_str.split())) + '\n'

        self.rst += self.kbd_str

    def print_result(self):
        print(self.rst)

    def write_result(self):
        with open("mouse_kebord_record.txt", "a") as f:
            f.write(self.rst)

    def finish(self):
        self.end = datetime.now()
        self.genarate_result()
        # self.print_result()
        self.write_result()

    def Listen(self):
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.mouse_listener.start()
        try:
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
        except KeyboardInterrupt:
            self.finish()
        finally:
            print('Exit')

if __name__=='__main__':
    m = Monitor()
    m.Listen()
