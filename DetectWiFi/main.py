import subprocess, re

def detect_wifi():
    try:
        output = subprocess.check_output(['netsh','wlan','show','network'])
        output = output.decode('utf-8').split('\n')
        networks = []
        for line in output:
            if(re.match('^SSID',line)):
                network = line.split(':')[1].strip()
                networks.append(network)
        return networks
    except Exception as e:
        print(f'ERROR: {e}')
        return []
    
if __name__ == "__main__":
    networks = detect_wifi()
    
    if networks:
        print('WiFi Available:')
        for network in networks:
            print(network)
    else:
        print("No WiFi")