import webbrowser
import pyautogui
import time
time.sleep(2)
url=f"https://www.facebook.com/profile.php?id=100082293283076"
webbrowser.open(url)
while True:
	pyautogui.hotkey("...")
	pyautogui.hotkey("Tìm hỗ trợ hoặc báo cáo")
	pyautogui.press("enter");
	pyautogui.hotkey("Tài khoản giả mạo")
	pyautogui.press("enter");
	pyautogui.press("enter");
	time.sleep(2)