# Arduino Oscilloscope

A simple Arduino-based oscilloscope that reads analog signals from a potentiometer and visualizes them on your computer using Python and matplotlib.

## Demo

![Demo Video](media/IMG_4815.mov)

## Hardware
- Arduino Uno/Nano
- Potentiometer
- Jumper wires & breadboard

## Software
- Arduino IDE
- Python (with `pyserial`, `matplotlib`)
- macOS or any OS with USB serial support

## Files
- `arduino_code/sketch_aug6a.ino` — Arduino code
- `python_visualizer/plot_serial.py` — Python real-time plotting script
- `docs/Oscilloscopes.pdf` — Notes on what an oscilloscope is
- `media/IMG_4815.mov` — Demo video

## Circuit
- GND → Potentiometer pin 1
- A0  → Potentiometer pin 2 (middle)
- 5V  → Potentiometer pin 3

## To Run
1. Upload Arduino code.
2. Run Python script.
3. View waveform.
