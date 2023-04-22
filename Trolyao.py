import speech_recognition
import pyttsx3
from datetime import date, datetime

while True:
    robot_ear = speech_recognition.Recognizer()
    robot_mouth = pyttsx3.init()
    robot = ""

    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)

    print("robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("you:" + you)

    if "my" in you:
        robot = "you don't have a girlfriend haha"
    elif "again" in you:
        robot = "ok repeat"
    elif "yourself" in you:
        robot = "Hello user, i am Python Assistant made by Mr.Long, Happy new year 2023"
    elif "created" in you:
        robot = "Mr. Long created me"
    elif "speak kimochi" in you:
        robot = "kimochiiii"
    elif "hello" in you:
        robot = "hi?"
    elif "today" in you:
        today = date.today()
        robot = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot = now.strftime("%H hours %M minutes %S seconds")
    elif "what is your name" in you:
        robot = "my name is nhatlong, what your name?"
    elif "my name is thinh" in you:
        robot = "ok, nice to meet you"
    elif" how are your" in you:
        robot = "i am fine thank you and bye"

        break
    else:
        robot = "I don't understand, you can repeat"

    print(robot)

    robot_mouth.say(robot)
    robot_mouth.runAndWait()
