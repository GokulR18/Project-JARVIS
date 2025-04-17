# Jarvis Voice Assistant 🗣️🤖

Welcome to **Jarvis**, your personal voice assistant! This Python script lets you interact with your computer using voice commands. It can open websites, provide news, search Wikipedia, and tell you the current time and date. Let's dive into the features! 🚀

---

## Features 🌟

- **Voice Commands** 🗣️: Speak to interact with Jarvis
- **Web Browsing** 🌐: Open popular websites like YouTube, Google, GitHub, Instagram, etc.
- **Time & Date** ⏰📅: Get the current time and date
- **Wikipedia Search** 📚: Search for topics and get brief summaries from Wikipedia
- **News Headlines** 📰: Get the latest top headlines from the US
- **Error Handling** ⚠️: Handles common errors like network issues or unrecognized commands

---

## Prerequisites 🛠️

Before running the script, ensure you have the following libraries installed:

- **speech_recognition** 🎙️: To recognize voice input
- **pyttsx3** 🗣️: For text-to-speech functionality
- **wikipedia** 📖: To search Wikipedia
- **requests** 🌐: To fetch news from an API
- **json** 📦: For JSON data handling
- **webbrowser** 🌍: To open websites in your browser

You can install the necessary packages using `pip`:

```bash
pip install SpeechRecognition pyttsx3 wikipedia requests
```

---

## Setup 🔧

1. **API Key for News** 📰: 
   - You'll need to get your own **NewsAPI** key from [newsapi.org](https://newsapi.org/).
   - Replace the placeholder in the script with your own key:  
     ```python
     newsapi_key = "YOUR_NEWSAPI_KEY"
     ```

2. **Running the Script** ▶️:
   - Simply run the script in your terminal or IDE:
   ```bash
   python jarvis.py
   ```
   - Jarvis will greet you and wait for the activation word ("arise") to begin listening for commands.

---

## Available Commands 🎤

- **Open Websites** 🌐:
  - "open youtube" → Opens YouTube
  - "open google" → Opens Google
  - "open github" → Opens GitHub
  - "open instagram" → Opens Instagram
  - "open linkedin" → Opens LinkedIn
  - "open spotify" → Opens Spotify

- **Time & Date** ⏰📅:
  - "time" → Get the current time
  - "date" → Get today's date

- **News** 📰:
  - "news" → Get the latest top news headlines
  - "headlines" → Same as above

- **Wikipedia Search** 📖:
  - "search wikipedia for [topic]" → Get a summary of a topic from Wikipedia

- **Help** ❓:
  - "help" or "what can you do" → Get a list of available commands

- **Exit** 🚪:
  - "exit" or "quit" → Close the application

---

## Example Usage 🎤

- **You**: "arise"  
  **Jarvis**: "Hey sir, how may I help you?"
  
- **You**: "Open YouTube"  
  **Jarvis**: "Opening YouTube"

- **You**: "What time is it?"  
  **Jarvis**: "The time is 10:30 AM"

- **You**: "Search Wikipedia for Python programming"  
  **Jarvis**: "According to Wikipedia, Python is an interpreted high-level programming language..."

---

## Contributing 🤝

Feel free to fork the project and submit your own contributions! If you find any bugs or have suggestions for improvements, open an issue, and I'll be happy to help!


---

Enjoy interacting with **Jarvis**! 🤖💬

