import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import wikipedia
import requests
import json

recognizer = sr.Recognizer()
talk = pyttsx3.init()
newsapi_key = "your_api_key "
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"

def speak(text):
    talk.say(text)
    talk.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Recognizing...")
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Speech service is unavailable right now.")
        return ""

def listen_for_activation():
    while True:
        speak("Please tell me the password for further information")
        command = take_command()
        if "arise" in command:
            speak("Hey sir, how may I help you")
            print("Hey sir, how may I help you")
            return True
        else:
            speak("Activation word not detected. Try again.")
            print("Activation word not detected. Try again.")

def get_news():
    try:
        response = requests.get(NEWS_URL)
        data = response.json()
        articles = data.get('articles')

        if not articles:
            speak("Sorry, I couldn't find any news right now.")
            return

        speak("Here are the top headlines:")
        for i, article in enumerate(articles[:5], start=1):
            title = article['title']
            news_line = f"Headline {i}: {title}"
            print(news_line)
            speak(news_line)
    except Exception as e:
        print("Error getting news:", e)
        speak("Sorry, I'm having trouble accessing the news.")
        
def process_commands():
    while True:
        command = take_command()

        if "exit" in command or "quit" in command:
            speak("Goodbye sir.")
            print("Goodbye sir.")
            break
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "open github" in command:
            speak("Opening GitHub")
            webbrowser.open("https://www.github.com")
        elif "open instagram" in command:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")
        elif "open linkedin" in command:
            speak("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")
        elif "open spotify" in command:
            speak("Opening Spotify")
            webbrowser.open("https://open.spotify.com")
        elif "time" in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_now}")
            print(f"The time is {time_now}")
        elif "date" in command:
            today = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {today}")
            print(f"Today is {today}")
        elif "what can you do" in command or "help" in command:
            speak("Here's what I can do:")
            speak("I can open websites like YouTube, Google, Instagram, Spotify, and more.")
            speak("I can tell you the current time and date.")
            speak("You can get news headlines.")
            speak("I can also search Wikipedia for you.")
            speak("Just say the command and I'll do it.")
        elif "wikipedia" in command or "search" in command or "who is" in command or "what is" in command:
            speak("Let me look that up on Wikipedia...")
            try:
                topic = command.replace("search wikipedia for", "").replace("wikipedia", "").replace("search", "").strip()
                summary = wikipedia.summary(topic, sentences=2)
                response = f"According to Wikipedia, {summary}"
                print(response)
                speak(response)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("That topic is too broad. Please be more specific.")
                print("Disambiguation Error:", e)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find anything on Wikipedia.")
                print("Page not found on Wikipedia.")
            except Exception as e:
                speak("Something went wrong while searching.")
                print("Error:", e)
        elif "news" in command or "headlines" in command:
            get_news()
        else:
            speak("Sorry, I didn't understand. Try again.")

if __name__ == "__main__":
    print("Initializing Jarvis......")
    speak("Initializing Jarvis")
    if listen_for_activation():
        process_commands()



