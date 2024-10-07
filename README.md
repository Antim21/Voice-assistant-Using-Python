# Voice-assistant-Using-Python

Install all libraries such as speech recognition, smtplib, pyttsx3

Make sure to test this code in an appropriate environment where microphone access is available.

This Python-based Voice Assistant, named Sky, utilizes various libraries to provide a hands-free interface for performing tasks through voice commands. The assistant can execute a variety of functions such as searching Wikipedia, opening websites, playing music, telling the time, and sending emails.

Features
Voice Recognition: Uses the speech_recognition library to capture and process voice commands.
Text-to-Speech: Utilizes the pyttsx3 library to convert text responses into audible speech.
Web Browsing: Opens popular websites (e.g., Google, YouTube, Facebook) based on voice commands.
Information Retrieval: Searches and summarizes information from Wikipedia.
Email Functionality: Sends emails through a Gmail SMTP server (requires user credentials).
Music Playback: Plays songs from a specified local directory.
Time Reporting: Announces the current time.
Technologies Used
Python
pyttsx3
SpeechRecognition
Wikipedia API
Webbrowser
SMTP (for email)

//
pip install pyttsx3 SpeechRecognition wikipedia
//

Usage
Clone this repository.
Open the script in your preferred Python IDE.
Update the email credentials in the sendEmail function.
Run the script and interact with the assistant using voice commands.
Note
This project demonstrates the integration of various libraries to create a functional voice assistant. Feel free to extend its capabilities by adding more features or improving existing ones!

