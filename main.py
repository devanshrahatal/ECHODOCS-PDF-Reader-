import os
import sys
import pyttsx3
from pdfminer.high_level import extract_text
from tkinter import Tk, messagebox, filedialog

# Function to get the PDF file
def get_pdf_path():
    Tk().withdraw() # Opens file dialog to select the PDF file
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        raise ValueError("No PDF file selected.")
    return file_path

#Function to extract text from PDF file
def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist.")
    return extract_text(pdf_path)

# Function to save audio file
def save_audio(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()

def main():
    try:
        pdf_path = get_pdf_path()

        text = extract_text_from_pdf(pdf_path)
        print("PDF Text:\n")
        print(text)

        # Initialize the TTS engine and convert text to audio
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

        # Asks' the user if they want to save the audio file
        save_audio_file = messagebox.askyesno("Save Audio", "Do you want to save the audio as an MP3 file?")
        if (save_audio_file):
            output_path = os.path.splitext(pdf_path)[0] + '.mp3'
            save_audio(text, output_path)
            print(f"Audio saved to {output_path}")
        else:
            print("Audio not saved.")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
    
    
    