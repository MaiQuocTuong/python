import speech_recognition 
import pyttsx3
from datetime import date, datetime
import os 
import webbrowser as wb 

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
voice = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voice[1].id)
robot_brain = ""

def speak(audio):
	print('Robot: '+ audio)
	robot_mouth.say(audio)
	robot_mouth.runAndWait()
def time():
	Time = datetime.now().strftime("%I:%M:%p")
	speak(Time)
def wecome():
	hour = datetime.now().hour
	if hour >= 6 and hour < 12:
		speak("Good Moring sri")
	elif hour >= 12 and hour < 18:
		speak("Good Afternoon sir")

	elif hour >= 18 and hour < 24:
		speak(" Good Night sir")
	speak('How can i help you')
def command():
		c = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as source:
			c.pause_threshold = 2
			audio = c.listen(source)
		try:
			you = c.recognize_google(audio,language = 'en')
			print("MQT:" + you)
		except speech_recognition.UnknownValueError:
			you = input('Your order is: ')
		return you

if __name__ =="__main__":
	wecome()
	while True:
		command()
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
		elif "hello" in you:
			robot_brain = "Hello Mai Quoc Tuong"
		elif "today" in you:
			today = date.today()
			robot_brain = today.strftime("%B %d, %Y")	
		if "google" in you:
			robot_brain = "What should I search sir?"
			url = f"https://www.google.com/search?query={search}"
			wb.get().open(url)
			if "youtube" in you:
				robot_brain = "What should I search sir?"
				url = f"https://www.youtube.com/search?query={search}"
				wb.get().open(url)
			elif "facebook" in you:
				robot_brain = "What should I search boss?"
				url = f"https://www.facebook.com/profile.php?id=100058252607474"
				wb.get().open(url)
			elif "github" in you:
				robot_brain = "What should I search boss?"
				url = f"https://github.com/"
				wb.get().open(url)
				if "open video" in you:
					video = r"C:\Users\User\Videos\Captures\nhac.mp4"
					os.stratfile(video)	
				elif "open picture" in you:
					img = r"C:\Users\User\Pictures\Camera Roll\anh.img"
					os.stratfile(img)
		elif "bye" in you:
			robot_brain = "Bye Mai Quoc Tuong"
			print("Robot: " , robot_brain)
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()		
			break
		else:
			robot_brain = "I'm fine thank you and you"

		print("Robot: ", robot_brain)


		robot_brain = "I can't hear you, try again"
		robot_mouth.say (robot_brain)
		robot_mouth.runAndWait()