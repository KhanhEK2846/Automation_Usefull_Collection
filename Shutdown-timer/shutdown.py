import os
print("\nShutdown timer")
h = int(input("Hour: "))
m = int(input("Minute: "))
s = int(input("Second: "))
while True:
  mode = input("Shutdown (s) or Restart(r): ")
  if mode == "s" or mode == "r":
    break

h = h *60 *60
m = m * 60
s = s+m+h

os.system(f"shutdown -{mode} -t {s}")

print("\nEnter shutdown -a to cancel")
