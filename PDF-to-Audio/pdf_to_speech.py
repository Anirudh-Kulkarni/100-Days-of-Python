#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:52:35 2024

@author: anirudhkulkarni
"""
import os
import PyPDF2
from gtts import gTTS
import pygame
import signal
import sys

# Global variable to control playback state
is_playing = False

def pdf_to_text(pdf_path):
    """Extract text from PDF"""
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        # Extract text from each page
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        
    return text

def save_text_to_speech(text, audio_path):
    """Convert text to speech and save it to an audio file"""
    tts = gTTS(text=text, lang='en')
    tts.save(audio_path)
    print(f"Audio saved to {audio_path}")

def play_audio(audio_path):
    """Play the audio file using pygame"""
    global is_playing
    pygame.mixer.init()
    
    # Load the audio file
    pygame.mixer.music.load(audio_path)
    
    # Start playback
    pygame.mixer.music.play()
    is_playing = True
    
    # While the audio is playing, allow interruption
    while is_playing:
        if not pygame.mixer.music.get_busy():
            is_playing = False

def stop_playback(signum, frame):
    """Stop playback when the script is interrupted (Ctrl+C)"""
    global is_playing
    if is_playing:
        print("Stopping playback...")
        pygame.mixer.music.stop()
        is_playing = False
    sys.exit(0)

def main(pdf_path, audio_path):
    # Extract text from PDF
    text = pdf_to_text(pdf_path)
    
    if text:

        # Save text as audio
        print("Saving audio file ...")
        save_text_to_speech(text, audio_path)
        print('Done saving audio file.')


        # Play the audio file
        play_audio(audio_path)

    else:
        print("No text found in the PDF.")

if __name__ == "__main__":
    # Handle Ctrl+C gracefully
    signal.signal(signal.SIGINT, stop_playback)

    # Replace with the path to your PDF file
    pdf_path = 'Zimingzhong_tour.pdf'
    
    # Path to save the audio file
    audio_path = 'Zimingzhong_audio.mp3'
    
    main(pdf_path, audio_path)
