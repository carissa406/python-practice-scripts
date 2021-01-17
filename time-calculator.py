start = "11:43 AM"
duration = "24:20"
day=True

#split the start time
hrsmins = start.split(":")
shrs = hrsmins[0] #hour
minsampm = hrsmins[1]
minsampm2 = minsampm.split(" ")
smins = minsampm2[0] #min
ampm = minsampm2[1] #Am or Pm

#split the duration
durationhrsmins = duration.split(":")
dhrs = durationhrsmins[0] #duration hours
dmins = durationhrsmins[1] #duration minutes

#convert string to ints
intshrs = int(shrs)
intsmins = int(smins)
intdhrs = int(dhrs)
intdmins = int(dmins)
intfhrs = 0
intfmins = 0

#add duration to the start time
#finalhrs = intshrs + intdhrs
#totalmins = intsmins + intdmins
#finalmins = 0 #final minutes after adding any overlapping hours below

days = ["sunday", 'monday', "tuesday", "wednesday", "thursday", "friday", "saturday"]

#get the number of minutes on the final time, add 1 hr to starthrs
if intdmins + intsmins > 60:
    intfmins = (intdmins + intsmins) - 60
    intshrs += 1

i = True
halfdays = 0
while i == True:
    if intdhrs > 12:
        intdhrs -= 12
        halfdays += 1
    else:
        i = False


print(intshrs)
print(intfmins)
print(halfdays)






#def add_time(start, duration, day=False):
    
    #return new_time