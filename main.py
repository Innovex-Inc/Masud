import random
import pyttsx3 as pyttsx
import speech_recognition as sr
import requests

# Initialize text-to-speech engine
engine = pyttsx.init()

def get_rizz_line():
    try:
        response = requests.get("https://vinuxd.vercel.app/api/pickup")
        if response.status_code == 200:
            rizz_line = response.json()["pickup"]
            return rizz_line
        else:
            print("Failed to fetch Rizz line. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error fetching Rizz line:", e)
        return None

def get_insult():
    try:
        response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        if response.status_code == 200:
            insult = response.json()["insult"]
            return insult
        else:
            print("Failed to fetch insult. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error fetching insult:", e)
        return None

def speak_text(text):
    print("Bot:", text)  # Print the text to terminal
    engine.say(text)
    engine.runAndWait()

def text_interaction():
    while True:
        speak_text("What would you like, a Rizz line or a roast? Please respond with 'rizz' or 'roast'.")
        user_input = input("Rizz or roast? (rizz/roast): ").lower()
        if user_input == 'rizz':
            rizz_line = get_rizz_line()
            if rizz_line:
                print("Rizz Line:", rizz_line)
                speak_text(rizz_line)
            else:
                speak_text("Sorry, I couldn't fetch a Rizz line at the moment.")
        elif user_input == 'roast':
            insult = get_insult()
            if insult:
                print("Roast:", insult)
                speak_text(insult)
            else:
                speak_text("Sorry, I couldn't fetch a roast at the moment.")
        else:
            speak_text("Sorry, I didn't understand. Please choose 'rizz' or 'roast'.")
            continue
        
        while True:
            speak_text("Would you like another Rizz line or roast? Please respond with 'yes' or 'no'.")
            user_input = input("Another rizz or roast? (yes/no): ").lower()
            if user_input in ['yes', 'no']:
                break
            else:
                speak_text("Sorry, I didn't understand. Please respond with 'yes' or 'no'.")
        
        if user_input != 'yes':
            speak_text("Okay, goodbye!")
            break

def voice_interaction():
    # Function to handle voice interaction
    # Implementation remains the same as before
    pass

def main():
    speak_text("Welcome! Would you like to interact through text or speech? Please respond with 'text' or 'speech'.")
    user_choice = input("Your choice: ").lower()
    if user_choice == 'text':
        text_interaction()
    elif user_choice == 'speech':
        voice_interaction()
    else:
        speak_text("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
