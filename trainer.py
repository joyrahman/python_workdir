#program to process file 

def sanitize(time_string):
    if '-' in time_string:
        separator = '-'
    elif ':' in time_string:
        separator = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(separator)
    return (mins + '.' + secs)

def get_file_data(filename):
    try:
        with open(filename) as f:
            data = f.readlines()
            return(str(data).strip().split(','))
    except IOError as ioerr:
        print ('File Error:' +str(ioerr))
        return (None)

sarah =  get_file_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
fastest_times = sorted(set([sanitize(t) for t in sarah]))
print (sarah_name + "sarahs_times are:"+ str((fastest_times)[0:3]))


