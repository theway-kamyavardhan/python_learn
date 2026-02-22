# Building a smart thermostat alert system
device_status = "active"
temp = 35

if device_status == "active":
    print("device online!")
    if temp > 35:
        print("device temp is very high")
    else :
        print("device is cool!")
else:
    print("the device is offline!")
    