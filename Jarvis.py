import speech_recognition as sr
import webbrowser
import pyttsx3
import pyjokes
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open github" in command:
        webbrowser.open("https://www.github.com")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif command.startswith("play"):
        song = command.split(" ", 1)[1]
        # Add your music library here
        musicLibrary = {
            "laal pari": "https://www.youtube.com/watch?v=KGn-erOG-Bs",
            "Desi Kalakar":"https://www.youtube.com/watch?v=KhnVcAC5bIM",
            "so high":"https://www.youtube.com/watch?v=GgmFC8y8q3k"
        }
        link = musicLibrary.get(song, "")
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in library.")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "kamal" in command:
        sr="""Kamal Hariramani is a highly motivated and intellectually curious individual with a strong passion for problem-solving and technology. He is currently pursuing a Bachelor of Engineering in Computer Science at the Government College of Engineering, Nagpur, where he is honing his skills in programming, data structures, algorithms, and software development. Kamal consistently seeks opportunities to deepen his understanding of computational thinking and real-world applications of computer science, often exploring complex challenges with creativity and persistence. His academic journey is shaped by a dedication to continuous learning, hands-on project work, and a forward-thinking mindset aimed at innovation. With a solid technical foundation and a natural drive to explore, Kamal aspires to make a meaningful impact in the tech industry by contributing to solutions that improve lives and advance technology."""
        speak(sr)
    elif "himanshu" in command:
        intro='''Himanshu Hariramani is a committed Chartered Accountant (CA) known for his meticulous approach to financial management and taxation. With a robust academic background and professional experience, he specializes in areas such as income tax, GST compliance, and corporate financial advisory. Himanshu's expertise extends to handling complex tax matters, including transfer pricing and international tax planning, offering strategic solutions to individuals and businesses alike. His dedication to continuous learning and professional development ensures that he stays abreast of the latest regulatory changes and industry best practices. Whether it's providing insightful financial analysis or guiding clients through intricate tax scenarios, Himanshu exemplifies professionalism and reliability in the field of accounting.'''
        speak(intro)
    elif "gautam" in command:
        intro2='''Gautam Hariramani is a distinguished individual who seamlessly integrates his legal expertise with entrepreneurial acumen. As a practicing lawyer, he has demonstrated a profound understanding of legal principles, offering insightful counsel and representation across various sectors. Complementing his legal career, Gautam is also a successful businessman, adept at navigating the complexities of the corporate world. His ventures span multiple industries, showcasing his versatility and strategic foresight. Holding a Bachelor of Commerce (BCom) degree, Gautam possesses a solid foundation in business and finance, which has been instrumental in his professional endeavors. Beyond his academic and professional pursuits, he has achieved numerous accolades, reflecting his commitment to excellence and continuous growth. Gautam's ability to balance his legal practice with business ventures underscores his dynamic approach to professional development and his unwavering dedication to making a significant impact in both fields.
        '''
        speak(intro2)
    elif "tushar" in command:
        intro3='''Tushar Hariramani is a driven young businessman who has seamlessly blended his academic foundation with entrepreneurial ventures. Holding a Bachelor of Commerce (BCom) degree, he possesses a solid understanding of business principles and financial management. Tushar's entrepreneurial spirit is evident in his active involvement in various business initiatives, where he applies his knowledge to drive growth and innovation. His commitment to continuous learning and adaptability in the ever-evolving business landscape underscores his potential for success in the competitive market'''
        speak(intro3)
if __name__ == "__main__":
     speak("Initializing Virtual")
     while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)

                if word.lower() == "virtual":
                    speak("Hey Kamal, welcome again. What can I help you with today?")
                    print("Virtual Activated.")
                    speak("Listening for your command...")

                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)

        except sr.UnknownValueError:
            # Do not respond to noise; just pass silently
            pass
        except sr.RequestError:
            speak("Sorry, the service is currently unavailable.")
        except sr.WaitTimeoutError:
            # When no voice is detected within the timeout
            pass
