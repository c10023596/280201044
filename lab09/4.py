import time


def alarm(t):
  t = int(t)
  if t == 0:
    return "Time is up!"
  else:
    print(str(t)+" seconds left.")
    time.sleep(1)
    return alarm(t-1) 

t = input("Input the time for the alarm: ")
timer = alarm(t)
print(timer)
