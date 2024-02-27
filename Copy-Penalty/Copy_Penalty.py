import pyperclip
print("\n Tool Copy Penalty")

c = input("Sentence: ")
n = int(input("Times: "))
ans = ""

for i in range(n):
    ans+= (c+"\n")

pyperclip.copy(ans)
print("\n Finish")
