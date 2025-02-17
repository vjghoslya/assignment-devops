import psutil
import time

# Set the threshold for CPU usage
threshold = 80

# Start monitoring the CPU usage
print("Starting to monitor CPU usage...")

while True:
    # Get the current CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)  # Interval of 1 second to check the CPU usage
    #print(f"CPU Usage: {cpu_usage}%")

    # Check if CPU usage exceeds the threshold
    if cpu_usage > threshold:
        print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

    time.sleep(1)  # Wait for 1 second before checking again