import os
import array
import textwrap
import random
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from pydub import AudioSegment

# Function to convert WAV to raw 8-bit PCM
def convert_wav_to_raw(wav_file):
    audio = AudioSegment.from_wav(wav_file)
    audio = audio.set_sample_width(1)  # Set to 8-bit
    audio = audio.set_frame_rate(16384)  # Set frame rate as suggested
    raw_file = wav_file.replace(".wav", ".raw")
    audio.export(raw_file, format="raw")
    return raw_file

# Function to convert the raw file to .h file for Mozzi
def char2mozzi(infile, tablename, samplerate=16384):
    fin = open(os.path.expanduser(infile), "rb")
    uint8_tstoread = os.path.getsize(os.path.expanduser(infile))
    valuesfromfile = array.array('b')  # Array of signed int8_t ints
    try:
        valuesfromfile.fromfile(fin, uint8_tstoread)
    finally:
        fin.close()

    values = valuesfromfile.tolist()
    directory, filename = os.path.split(infile)
    tablename = tablename.replace(" ", "_")  # Ensure no spaces in table name
    outfile = os.path.join(directory, tablename + ".h")
    
    fout = open(os.path.expanduser(outfile), "w")
    fout.write('#ifndef ' + tablename + '_H_' + '\n')
    fout.write('#define ' + tablename + '_H_' + '\n \n')
    fout.write('#include <Arduino.h>'+'\n')
    fout.write('#include "mozzi_pgmspace.h"'+'\n \n')
    fout.write('#define ' + tablename + '_NUM_CELLS '+ str(len(values))+'\n')
    fout.write('#define ' + tablename + '_SAMPLERATE '+ str(samplerate)+'\n \n')
    outstring = 'CONSTTABLE_STORAGE(int8_t) ' + tablename + '_DATA [] = {'
    try:
        for i in range(len(values)):
            if (values[i] == 33) and (values[i+1] == 33) and (values[i+2] == 33):
                values[i+2] = random.choice([32, 34])  # Avoid 33, 33, 33
            outstring += str(values[i]) + ", "
    finally:
        outstring +=  "};"
        outstring = textwrap.fill(outstring, 80)
        fout.write(outstring)
        fout.write('\n\n#endif /* ' + tablename + '_H_ */\n')
    fout.close()
    print(f"Converted {infile} to {outfile}")

# Function to handle drag and drop
def drop(event):
    filepath = event.data.strip('{}')  # Remove curly braces added by tkinterDnD
    if os.path.isfile(filepath) and filepath.lower().endswith(".wav"):
        raw_file = convert_wav_to_raw(filepath)
        tablename = os.path.splitext(os.path.basename(filepath))[0]
        char2mozzi(raw_file, tablename)
        status_label.config(text=f"Converted: {tablename}.h created in the same directory")

# Set up the Tkinter window with DnD support
root = TkinterDnD.Tk()
root.title("Mozzi .h Converter")
root.geometry("400x200")

# Instructions label
label = tk.Label(root, text="Drag and drop a WAV file here to convert to Mozzi .h file")
label.pack(pady=20)

# Status label to show conversion status
status_label = tk.Label(root, text="Waiting for file...")
status_label.pack(pady=20)

# Make the label accept drag and drop
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()
