from irsender import IRSender

# Test program to send some simple commands using an infrared emitter
# Requires irsender.py in the same directory 
# and a codes file in the constructor call to IRSender.

codes = ["on", "flash"]

irs = IRSender("/home/pi/infrared/light_codes")

if not irs.connected:
    print ("Unable to setup infrared connection - is pigpiod running?")
    exit (0)

for this_code in codes:
    print ("Sending code "+this_code)
    irs.send_code (this_code)

irs.close()