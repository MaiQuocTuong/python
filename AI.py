import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""


while True:
	
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""

	print("You: ", you)


	if you == "":
		robot_brain = "I can't heart you, try again"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
	elif "hello" in you:
		robot_brain = "Hello Mai Quoc Tuong"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()	
	elif "bye" in you:
		robot_brain = "Bye Mai Quoc Tuong"
		print("Robot: " , robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break

	print("Robot: ", robot_brain)


