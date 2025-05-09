import speech_recognition as sr
import time

def format_srt_time(seconds):
    return time.strftime('%H:%M:%S', time.gmtime(seconds)) + ',000'

def recognize_and_generate_srt(filename="output.srt", chunk_duration=5):
    r = sr.Recognizer()
    mic = sr.Microphone()
    print("Calibrating microphone for ambient noise... Please wait.")
    
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=2)
    
    print("Recording and transcribing. Press Ctrl+C to stop.")
    
    subtitle_index = 1
    start_time = time.time()
    
    with open(filename, "w", encoding="utf-8") as srt_file:
        try:
            while True:
                with mic as source:
                    print(f"\n[{subtitle_index}] Listening for {chunk_duration} seconds...")
                    audio = r.listen(source, phrase_time_limit=chunk_duration)

                end_time = time.time()
                
                try:
                    text = r.recognize_google(audio)
                    print("Transcribed:", text)

                    # Write to SRT
                    srt_file.write(f"{subtitle_index}\n")
                    srt_file.write(f"{format_srt_time(start_time)} --> {format_srt_time(end_time)}\n")
                    srt_file.write(f"{text}\n\n")

                    subtitle_index += 1
                    start_time = end_time
                except sr.UnknownValueError:
                    print("Could not understand audio.")
                except sr.RequestError:
                    print("API unavailable or quota exceeded.")
        except KeyboardInterrupt:
            print("\nStopped transcription.")

# Run the function
recognize_and_generate_srt()