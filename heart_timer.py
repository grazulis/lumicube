# Isaac wrote this for Lumicube

import datetime
display.set_all(black)
r = pink
heart = [
    [0,0,0,0,0,0,0,0],
    [0,r,r,0,0,r,r,0],
    [r,r,r,r,r,r,r,r],
    [r,r,r,r,r,r,r,r],
    [0,r,r,r,r,r,r,0],
    [0,0,r,r,r,r,0,0],
    [0,0,0,r,r,0,0,0],
    [0,0,0,0,0,0,0,0]
]

display.set_panel("top",heart)
while True:
    time_text = datetime.datetime.now().strftime("%H:%M")
    display.scroll_text(time_text, pink)
    time.sleep(60)
