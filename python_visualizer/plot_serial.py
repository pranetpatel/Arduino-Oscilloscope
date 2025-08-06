import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# CONFIGURATION
port = '/dev/tty.usbserial-1420'  # NEW
baud = 115200
max_len = 500  # Number of points to display at once

# Set up serial connection
ser = serial.Serial(port, baud, timeout=1)

# Rolling buffer
data = deque([0]*max_len, maxlen=max_len)

# Setup plot
fig, ax = plt.subplots()
line, = ax.plot(data)
ax.set_ylim(0, 1023)  # Analog read range for Arduino

def update(frame):
    try:
        value = int(ser.readline().decode().strip())
        data.append(value)
        line.set_ydata(data)
    except:
        pass
    return line,

ani = animation.FuncAnimation(fig, update, interval=10)
plt.show()
