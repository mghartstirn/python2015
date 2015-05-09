#codeacademy Date + Time 
#datetime is a library that you have to import
#its function is to grab that exact date + time
#this program helps display it with the information we want, not all the information we get

from datetime import datetime
now = datetime.now()
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

#'%s/%s/%s' is a placeholder for the strings that will follow in parenthesis
#change the character between the %s to what makes sense for what you're asking for
