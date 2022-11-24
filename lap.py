import pyautogui
import pyperclip
import time

time.sleep(0.001)
for i  in range(1000):
	pyperclip.copy("Ảnh quá chất lượng" )
	pyautogui.hotkey("ctrl", "v")
	pyautogui.press("enter");
	pyperclip.copy("Up đê")
	pyautogui.hotkey("ctrl", "v")
	pyautogui.press("enter");
	time.sleep(0.001)