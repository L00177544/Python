import psutil

def cpu_load():
 # Return significant numbers relating to the CPU
 #print(f"Number of CPUs: {psutil.cpu_count()}" )
 #print(f"CPU load: {psutil.cpu_percent()}")
 return(psutil.cpu_count(), psutil.cpu_percent())

print(f"Number of CPUs: {psutil.cpu_count()}" )
print(f"CPU load: {psutil.cpu_percent()}")