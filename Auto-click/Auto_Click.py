import pyautogui, time
print("\n Tool Auto Click")
count = int(input("Click: "))
d = float(input("Delay: "))

print ("\n Prepare for auto click: ")
for i in range(5,0,-1):
    print(i,end=" ", flush = True)
    time.sleep(1)

print("\n Start")
x,y = pyautogui.position()
for _ in range(count):
    pyautogui.click(x,y)
    time.sleep(d)
print("\n Finish")
