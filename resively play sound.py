
import glob 

path = r"/usr/share/scratch/"

directory = "/usr/share/scratch"
pathname = directory + "/**/*.mp3"
files = glob.iglob(pathname, recursive=True)
print(files)
print(pathname)
for filename in glob.iglob('/usr/share/scratch/**/*.mp3', recursive=True):
    print(filename)
    