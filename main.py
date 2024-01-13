import queue
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

device = 0 # 0 is the default audio device of the system
window = 1000 # window for the data
downsample = 1 # how much samples to drop
channels = [1] # a list of audio channels
interval = 30 # this is update interval in miliseconds for plot

q = queue.Queue()

device_info =  sd.query_devices(device, 'input')
samplerate = device_info['default_samplerate']
length  = int(window*samplerate/(1000*downsample))

print("Sample Rate: ", samplerate)

plotdata =  np.zeros((length,len(channels))) # samples
print("plotdata shape: ", plotdata.shape) # shape of array

# next is to make fig and axis of matplotlib plt
fig, ax = plt.subplots(figsize=(8,4))
ax.set_title("DeCoder")

lines = ax.plot(plotdata,color = (0,1,0)) # green lines

# Function below will automatically called when new audio data arrives and add it to queue

def audio_callback(indata,frames,time,status):
	q.put(indata[::downsample,[0]])

# It will take frame of audio samples from the queue and update to the lines
"""This function is responsible for drawing the audio waveform on the plot.
It continuously checks the queue for new audio data.
When it finds data, it shifts the existing data to the left and adds the new data to the end, creating the scrolling effect.
It then updates the line on the plot to match the new data."""

def update_plot(frame):
	global plotdata # will get updated from outside the function
	while True:
		try: 
			data = q.get_nowait() # checks for new audio data
		except queue.Empty:
			break
		shift = len(data)
		plotdata = np.roll(plotdata, -shift,axis = 0) # Shifts the existing plotdata to the left by the amount of new data
		plotdata[-shift:,:] = data # appends the new data to the end of the shifted plotdata
	for column, line in enumerate(lines):
		line.set_ydata(plotdata[:,column]) # updates the y-axis to match the new data
	return lines

ax.set_facecolor((0,0,0)) # background
ax.set_yticks([0]) # Restrict the y-axis to value 0 only, instead of 5 values matching x-axis
ax.yaxis.grid(True) # grid along the y-axis to visualize better

# Sound device stream to get Input from mic
stream  = sd.InputStream( device = device, channels = max(channels), samplerate = samplerate, callback  = audio_callback)

# Creating screen
ani  = FuncAnimation(fig, update_plot, interval=interval, blit=True) # Creating animation using matplotlib's FuncAnimation function
with stream:
	plt.show()
