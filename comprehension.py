import os, glob

metadata = [(f, os.stat(f)) for f in glob.glob('*.py')]
#print metadata[0]

#for k in metadata:
#    print k


metadata_dict = {f:os.stat(f) for f in glob.glob('*.py')}

print list(metadata_dict.keys())
