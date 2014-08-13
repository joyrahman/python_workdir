class Athlete:
	def __init__(self,a_name,a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times 
	def pop3(self):
		return (sorted(set([sanitize(t) for t in self.times]))[0:3])

#sarah = Athlete('Joy Rahman','2002-6-17',['2.58','2.74','2.98'])
#james = Athlete('James Jones')

#print (sarah.name)


def sanitize(time_string):
    if '-' in time_string:
        separator = '-'
    elif ':' in time_string:
        separator = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(separator)
    return (mins + '.' + secs)

def get_coach_data (filename):
	try:
		with open(filename) as f:
			data = f.readline()
			templ = data.strip().split(',')
			return (Athlete(templ.pop(0),templ.pop(0),templ))
	except IOError as ioerr:
		print ('File error' + str(ioerr))
		return (None)	
		
james = get_coach_data('sarah2.txt')

print (james.name)	
print (str(james.pop3()))		
