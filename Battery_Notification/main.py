import psutil, time
from plyer import notification

def battery_notifier():
    while True:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        
        if plugged:
            status = "Charging"
        else:
            status = "Discharging"
            
        mess = f"Battery is {status}. ({percent}% charged)"
        
        notification.notify(
            title = "Battery Status",
            message = mess,
            timeout = 10
        )
        
        time.sleep(60)
        
if __name__ == "__main__":
    battery_notifier()