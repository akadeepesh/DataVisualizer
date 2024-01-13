 # Real-Time Audio Visualizer

**Visualize audio signals from your microphone in real-time using Python!**

## Project Overview

This project creates a dynamic waveform display that visualizes audio captured from your microphone. It leverages the `sounddevice` library for efficient audio I/O and Matplotlib for plotting and animation.

## Installation

1. Install required libraries:

   ```bash
   pip install sounddevice numpy matplotlib
   ```

## Usage

1. Run the Python script:

   ```bash
   python pyshine.py
   ```

2. Allow microphone access and make sure that input and output devices are connected.

3. Observe the real-time audio waveform on the plot.

## Workflow

1. **Audio Capture:** The `sounddevice` library establishes an audio stream from the microphone.
2. **Data Processing:** Incoming audio data is processed and placed into a queue.
3. **Visualization:** Matplotlib creates a figure and a plot to display the audio waveform.
4. **Animation:** The `FuncAnimation` function continuously updates the plot, creating the real-time effect.
5. **Audio Callback:** A callback function handles incoming audio data efficiently.

## Customization

- **Audio Settings:** Adjust the audio device, channels, and sampling rate in the code.
- **Visualization:** Explore different plot styles, colors, and grid options in Matplotlib.
