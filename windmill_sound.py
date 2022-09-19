# Blow on the back of the cube to make the windmill animation turn.

import threading

display.set_all(black)

# max_magnitude = 1 # Dynamically adjust the max as we go along

def to_text(value):
    return str("{:.1f}".format(value))

# Start recording audio samples
microphone.start_recording_for_frequency_analysis()

def windmill_shader(x, y, blade_angle):
    theta = 360 * (0.5 + math.atan2(y, x) / (2 * math.pi))
    modulo = (3 * theta) % 360
    difference = abs(modulo - blade_angle)
    return hsv_colour(0, 0, 500 / difference ** 2 if difference > 0 else 1)

decay = 0.07
sample_period = 1
threshold = 0
sample = 0
previous_sample = 0
next_sample_time = time.monotonic() + sample_period
accumulator = 0
blade_angle = 0
rotational_velocity = 0
max_velocity = 400
while True:
    now = time.monotonic()
    if time.monotonic() > next_sample_time:
        sample = list(microphone.get_frequency_buckets(1, 0, 800).values())[0]
        
        #write values to screen
        text = ("sample: " + to_text(sample) + "\n"
            + "accumulator : " + to_text(accumulator) + "\n"
            + "previous_sample : " + to_text(previous_sample) + "\n"
            + "rotational_velocity : " + to_text(rotational_velocity) + "\n") 
        screen.write_text(10, 18, text, 1, white, black)
        if sample > previous_sample + threshold:
            accumulator = 10
        previous_sample = sample
        next_sample_time = now + sample_period
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
