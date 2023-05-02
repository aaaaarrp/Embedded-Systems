import time
import board
import adafruit_dht as af
import mysql.connector
dhtDevice = af.DHT22(board.D4, use_pulseio=False)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)
print(mydb)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE TEMP")
cursor.execute("USE TEMP")
cursor.execute("""CREATE TABLE IF NOT EXISTS 
               log(id INT AUTO_INCREMENT,
                   temp VARCHAR(255),
                   humidity VARCHAR(255),
                   PRIMARY KEY(id))"""
               )
while True:
    try:
        tc = dhtDevice.temperature
        tf = tc * (9 / 5) + 32
        humid = dhtDevice.humidity
        print(f"Temp: {tc:0.2f}C - {tf:0.2f}F")
        sql = f"""INSERT INTO 'logs' (temp, humidity) VALUES ('{tc:0.2f}','{humid:0.2f}')"""
        cursor.execute(sql)
        mydb.commit()
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)
    
# 3.3V GPIO GND
