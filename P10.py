import threading
import urllib.request
import time

def download_file (file):
    start = time.perf_counter()
    print("Downloading "+str(file)+" is started.")
    data = urllib.request.urlopen(file)
    print("Downloading "+str(file)+" is finished with time: "+str(time.perf_counter()-start)+".")

files = ["https://images.unsplash.com/photo-1541233349642-6e425fe6190e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
         "https://images.unsplash.com/photo-1449034446853-66c86144b0ad?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80",
         "https://images.unsplash.com/photo-1522775559573-2f76d540932b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=675&q=80"]

threades = []
for f in files:
    t = threading.Thread(target=download_file, args=[f])
    t.start()
    threades.append(t)

for t in threades:
    t.join()

print("End")