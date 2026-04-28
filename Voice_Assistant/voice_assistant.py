import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def greet():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am your voice assistant. How can I help you?")

def processCommand(command):
    command = command.lower()
    
    if "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        
        if query == "":
            speak("Please tell me what to search on Wikipedia!")
        else:
            speak("Searching Wikipedia...")
            try:
                result = wikipedia.summary(query, sentences=2, auto_suggest=False)
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("Too many results, please be more specific!")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find anything on Wikipedia!")
            except Exception as e:
                print(f"Wikipedia Error: {e}")
                speak("Sorry, I couldn't fetch results right now!")
    
    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    
    elif "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Current time is {time}")
        speak(f"Current time is {time}")
    
    elif "date" in command:
        date = datetime.datetime.now().strftime("%B %d %Y")
        print(f"Today's date is {date}")
        speak(f"Today's date is {date}")
    
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    greet()
    
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=10)
            
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            processCommand(command)
        
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")