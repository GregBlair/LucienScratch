
import glob

# path = r"/usr/share/scratch"
# 
# files = glob.glob("/usr/share/scratch", *.mp3,recursive = True)
# print(files)
# 
files = glob.iglob('/usr/share/scratch/**/*.mp3', recursive = True)
count = 0

for filename in glob.iglob('/usr/**/*.mp3', recursive = True): 
    print(filename)
    count += 1
print(count)

# fcuE78IWzV%Pl8lucl