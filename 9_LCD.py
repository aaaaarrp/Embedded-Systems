import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

lcd_columns = 16
lcd_rows = 2

lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_backlight = digitalio.DigitalInOut(board.D4)

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.cursor_position(0, 0)
lcd.message = "Hi"
lcd.cursor_position(3, 0)
lcd.message = "Hope you are"
lcd.cursor_position(0, 1)
lcd.message = "enjoying the"
time.sleep(5)
lcd.clear()

lcd.cursor_position(0, 0)
lcd.message = "Raspberry Pi"
lcd.cursor_position(0, 1)
lcd.message = "LCD Interfacing"
time.sleep(5)
lcd.clear()

# VSS(GND), VDD(5V), V0(Contrast), RS, RW(GND), E, D0, D1, D2, D3, D4, D5, D6, D7, A(Backlight +, 5V through Resistor), K(Backlight -, GND)
