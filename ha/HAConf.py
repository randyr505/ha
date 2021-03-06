##################################################################
# configuration
##################################################################

import os

running = True

# Environment
rootDir = os.path.dirname(os.path.realpath(__file__))+"/../../"
configDir = rootDir+"conf/"
keyDir = rootDir+"keys/"
stateDir = rootDir+"state/"
sysLogging = True

# Localization
latLong = (34.149044, -118.401994)
elevation = 620 # elevation in feet
tempScale = "F"

# Notification
smsSid = keyDir+"twilio.sid"
smsToken = keyDir+"twilio.tkn"
notifyFromNumber = keyDir+"notifyFromNumber"

# General debugging
debugEnable = False
debugConf = False
debugObject = False
debugState = False
debugStateChange = False
debugThread = False
debugInterrupt = False

# REST interface
debugRest = False
debugRestResources = False
debugRestGet = False
debugRestPut = False
debugRestStates = False

# Scheduler
debugEvent = False
debugSched = False

