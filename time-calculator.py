start = "11:30 AM"
duration = "2:32"
day= "mOnDaY"

def add_time(start, duration, day=None):

  days = ["sunday", 'monday', "tuesday", "wednesday", "thursday", "friday", "saturday"]

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
  intfmins = intsmins + intdmins

  #get the number of minutes on the final time, add 1 hr to starthrs
  if intfmins > 60:
      intfmins = (intfmins) - 60
      intshrs += 1

  #getting the final hr and switching from am to pm
  #convert pm numbers to 24 hour time
  chrs = intshrs
  if ampm == "PM":
      chrs += 12

  chrs += intdhrs #add the duration hours to the 24 hr time
  intfhrs = chrs % 24 #converting the time passed to 24 hr time into intfhrs
  if intfhrs >= 12: #if it is greater than 12 then it is a pm time
      ampm = "PM"
      intfhrs-=12
  else:
      ampm = "AM"
  if intfhrs == 0: #if the time is 0 then its 12
      intfhrs = 12

  #calculate number of days that have passed
  ndays=0
  while chrs >= 24:
      chrs-=24
      ndays += 1

  #formatting minutes to print 
  strmin=""
  strmin = str(intfmins)
  if len(strmin) != 2:
      strmin = "0"+strmin

  #completed string for time stringtime
  stringtime = str(intfhrs) + ":"  + strmin + " " + ampm

  #completed string for n days later or next day dayslater
  dayslater = ""
  if ndays > 0:
      if ndays == 1:
          dayslater = " (next day)"
      else:
          dayslater = " (" + str(ndays) + " days later)"

  #remove any case from the day if day exists
  fday = ""
  if day != None: 
      day = day.lower()
      #find out the day of the week
      sday = days.index(day)
      cday = sday + ndays
      cday = cday % 7
      fday = days[cday]
      fday = ", " + fday.capitalize()

  new_time = stringtime + fday + dayslater

  return new_time