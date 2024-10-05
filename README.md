# 🎵 WAV to Mozzi Sample Converter 🎵

Welcome to the **WAV to Mozzi Sample Converter**! This tool allows you to convert your `.wav` files into `.h` header files formatted specifically for the Mozzi library in Arduino. With a simple drag-and-drop interface, it's easy to integrate audio samples into your Arduino projects.


## 📝 Description

This project provides a user-friendly way to convert audio files into C++ array format for use in the Mozzi sound synthesis library. It's perfect for quickly generating `.h` files with your own custom sound samples.

## 🚀 Features
- **Drag-and-Drop Functionality**: Simply drop your WAV file into the GUI to convert it.
- **Easy-to-Use Interface**: No need to mess with command-line tools—just run and convert!
- **Arduino Compatibility**: The generated `.h` files can be used directly with Mozzi in your Arduino projects.

## 🛠️ Installation

To get started, clone the repository and install the required dependencies:

1. Clone the repository:

    ```bash
    git clone https://github.com/lenn-maker/wav_to_mozzi_sample.git
    cd wav_to_mozzi_sample
    ```

2. Install the required Python packages:

    ```bash
    pip install tkinterdnd2 pydub
    ```

3. Make sure you have `ffmpeg` installed, as it is required by the `pydub` library. You can [download and install ffmpeg here](https://www.ffmpeg.org/download.html).

## 📂 Usage

1. Run the script:

    ```bash
    python wav_to_h_converter.py
    ```

2. Drag and drop your `.wav` file onto the interface.

3. The `.h` file will be generated in the same directory as the original `.wav` file.

## 🔧 How It Works

The script processes your WAV file and converts it into a C++ array format compatible with the Mozzi library. This makes it easy to play custom audio samples directly from your Arduino!

## 💻 Requirements

- Python 3.6+
- `tkinterdnd2` library
- `pydub` library
- `ffmpeg` installed and configured


## 🤝 Contributing

You can make it faster if you want but this script is so specific i think no one needs to contribute.



---

Enjoy converting your WAV files for your next Arduino project!
