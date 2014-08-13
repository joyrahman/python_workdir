import os
import sys

directory_name = "./"
file_extension = "txt"
if len(sys.argv) > 2:
    directory_name = sys.argv[1]
    file_extension = sys.argv[2]
elif len(sys.argv) > 1 and len(sys.argv)<2:
    directory_name = sys.argv[1]

list = os.listdir( directory_name )
counter = 0
for old_file in list:
    if file_extension in old_file:
        new_file = "test_"+ str( counter ) + ".txt"
        os.rename( directory_name + "/"+ old_file, directory_name + "/" + new_file )
        print "file renamed from {} to {}".format( old_file, new_file )
        counter += 1
