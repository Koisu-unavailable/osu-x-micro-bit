import pyautogui



def on_button_pressed_a():
    pyautogui.dragRel(0, 10)
input.on_button_pressed(Button.A, on_button_pressed_a)