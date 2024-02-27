import pyautogui, pyperclip, time, random
print("\n Tool Spam")
msg = input("Content: ").split(", ")
n = int(input("Times: "))
m = float(input("Delay: "))

print ("\n Prepare for spam in: ")
for i in range(5,0,-1):
    print(i,end=" ", flush = True)
    time.sleep(1)

print("\n Start")
for j in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(m)

print("\n Finish")
