import nfc
import time
import requests

def on_startup(targets):
    return targets

def on_connect(tag):
    print(tag.identifier.encode('hex_codec'))
    # print(tag)

rdwr_options = {
    'targets': ['106A'],
    'on-startup': on_startup,
    'on-connect': on_connect,
}

CLASS_ID = 1;

def read():
    with nfc.ContactlessFrontend('usb:072f:2200') as clf:
        tag = clf.connect(rdwr=rdwr_options)

        json = {
            "rfid" : tag.identifier.encode('hex_codec'),
            "ruangan_id": CLASS_ID
        };

        response = requests.post('http://127.0.0.1:8000/api/absen', json);
        print(response.status_code)
        if(response.status_code == 500):
            for i in range(3):
                nfc.clf.acr122.Device.turn_on_led_and_buzzer(clf.device)
            time.sleep(0.2)
            print(response.json().pesan)
            
        elif(response.status_code == 404):
            for i in range(4):
                nfc.clf.acr122.Device.turn_on_led_and_buzzer(clf.device)
                time.sleep(0.02)
            
        elif(response.status_code == 200):
            responseJSON = response.json()
            if(responseJSON['status'] == False):
                nfc.clf.acr122.Device.turn_on_led_and_buzzer(clf.device)
                time.sleep(0.2)
                nfc.clf.acr122.Device.turn_on_led_and_buzzer(clf.device)
                print(responseJSON)
            
            else:
                nfc.clf.acr122.Device.turn_on_led_and_buzzer(clf.device)
                
        time.sleep(1)
        
        
        # print(tag)
        # if tag.ndef:
            # print(tag.ndef.message.pretty())
