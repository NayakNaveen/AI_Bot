**AI - Voice Assistant**

This Python-based voice assistant mimics basic functionalities similar to Alexa. It can perform various tasks, including telling time, date, searching Wikipedia, managing Chrome searches, providing jokes, and more. It uses several libraries, including pyttsx3 for text-to-speech, SpeechRecognition for speech-to-text, wikipedia for fetching information, and psutil for monitoring system stats like CPU usage and battery status.

**Requirements**

Before running the script, you need to install the following Python packages:
1. pyttsx3 - For converting text to speech (TTS).
2. SpeechRecognition - For recognizing speech input.
3. wikipedia - For retrieving information from Wikipedia.
4. psutil - For monitoring system performance (CPU usage, battery status).
5. pyjokes - For providing jokes.

**Features**

1. Greeting and Time/Date Reporting - The assistant greets the user and provides the current time and date.
2. Speech Recognition - The assistant listens to voice commands and performs actions based on recognized speech. Commands include asking for the time, date, searching Wikipedia, and more.
3. Wikipedia Search - The assistant can search Wikipedia for a topic and summarize the result.
4. System Status - The assistant can check and report the current CPU usage and battery percentage.
5. Jokes - The assistant can tell random jokes using the pyjokes library.
6. Browser Search - The assistant can open Chrome and search a specific term on the web.
7. Reminders - The assistant can store user-provided data in a text file (data.txt) and retrieve it later upon request.
8. Shutdown/Logout - The assistant can log out the current user from the system using the logout command.
9. Exit Command - The assistant can be terminated by saying "offline."
