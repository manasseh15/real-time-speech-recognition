this Python script uses the speech_recognition library to record audio from a microphone in real time and generate corresponding subtitles in SRT format.

📌 Features
Real-time microphone input

Automatic speech recognition via Google Web Speech API

Subtitle generation in .srt format

Adjustable audio chunk duration

Simple and customizable codebase

🛠️ Requirements
Python 3.7+

Microphone device

Internet connection (for Google Speech Recognition API)

The script will:

Calibrate for ambient noise.

Continuously listen in chunk_duration second segments (default is 5s).

Transcribe each segment.

Save the transcriptions into output.srt with proper timecodes.
