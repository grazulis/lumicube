# Blow on the back of the cube to make the windmill animation turn.
# Start recording audio samples
import threading

# start listening
microphone.start_recording_for_frequency_analysis()

def worker():
    global level
    while True:
			# the buckets here can be changed for different types of noise
        level = list(microphone.get_frequency_buckets(4, 0, 1000).values())[2]
        time.sleep(0.05)

threading.Thread(target=worker, daemon=True).start()
def to_text(value):
    return str("{:.1f}".format(value))
    
def windmill_shader(x, y, blade_angle):
    theta = 360 * (0.5 + math.atan2(y, x) / (2 * math.pi))
    modulo = (3 * theta) % 360
    difference = abs(modulo - blade_angle)
    return hsv_colour(0, 0, 500 / difference ** 2 if difference > 0 else 1)

decay = 0.07
sample_period = 0.025
threshold = 0.15
previous_sample = 100
next_sample_time = time.monotonic() + sample_period
accumulator = 0
blade_angle = 0
rotational_velocity = 0
max_velocity = 70
sample = 0

while True:
    now = time.monotonic()
    if time.monotonic() > next_sample_time:
        sample = level
        if sample > 1200:
            accumulator = 3
        previous_sample = sample
        next_sample_time = now + sample_period
    
    #write values to screen 
    text = ("IP address: " + pi.ip_address() + "\n"
        + "CPU temp  : " + to_text(pi.cpu_temp()) + "\n"
        + "CPU usage : " + to_text(pi.cpu_percent()) + "\n"
        + "RAM usage : " + to_text(pi.ram_percent_used()) +"\n"
        + "Disk usage: " + to_text(pi.disk_percent()) + "\n"
        + "level     : " + to_text(sample))
    
    screen.write_text(10, 18, text, 1, green, black)
    
    rotational_velocity = max_velocity * min(accumulator, 1)
    blade_angle = (blade_angle + rotational_velocity) % 360
    canvas = {}
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x == 8 or y == 8 or z == 8:
                    projected_x = (x - z)
                    projected_y = (2 * y - x - z) / (3 ** 0.5)
                    canvas[(x,y,z)] = windmill_shader(projected_x, projected_y, blade_angle)
    display.set_3d(canvas, True)
    accumulator *= (1 - decay)
    time.sleep(1 / 25)
