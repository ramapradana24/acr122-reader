import nfc
import time

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

def read():
    with nfc.ContactlessFrontend('usb:072f:2200') as clf:
        tag = clf.connect(rdwr=rdwr_options)
        nfc.clf.acr122.Device.turn_on_led_and_buzzer(clf.device)
        time.sleep(1)
        # print(tag)
        # if tag.ndef:
            # print(tag.ndef.message.pretty())
