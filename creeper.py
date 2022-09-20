# Continually change the cube's colour.
display.set_all(black)
screen.draw_rectangle(0, 0, 280, 200, black)

# Draw a minecraft creeper. 
# TODO add moving the face based on gesture

from xml.etree.ElementPath import get_parent_map


g = green
g1 = hsv_colour(0.24, 0.5, 1)
g2 = hsv_colour(0.18, 0.7, 1)
g3 = hsv_colour(0.2, 0.7, 1)
g4 = hsv_colour(0.2, 0.9, 0.4)


creeper_face = [
    [g1,g,g2,g1,g3,g,g2,g],
    [g2,g,g1,g2,g,g2,g,g1],
    [g1,0,0,g,g1,0,0,g2],
    [g,0,0,g1,g2,0,0,g1],
    [g3,g2,g1,g4,g4,g,g3,g1],
    [g2,g1,g4,0,0,g4,g2,g3],
    [g,g2,0,0,0,0,g1,g2],
    [g1,g,g4,g2,g1,g4,g3,g]
]
creeper = [
    [g1,g,g2,g1,g3,g,g2,g],
    [g2,g,g1,g2,g,g2,g,g1],
    [g1,g2,g3,g,g1,g3,g,g2],
    [g,g1,g3,g1,g2,g1,g3,g1],
    [g3,g2,g1,g1,g2,g,g3,g1],
    [g2,g1,g3,g1,g2,g1,g,g3],
    [g,g2,g,g3,g1,g,g1,g2],
    [g1,g,g1,g2,g1,g,g3,g]
]
display.set_panel("left", creeper_face)
display.set_panel("right", creeper)
display.set_panel("top", creeper)

while True:
    time.sleep(90)
    # you will need to upload mp3 of creeper noise for this to work
    speaker.play("creeper.mp3")
    # otherwise you can comment out the above and use this
    #speaker.tone(500, 0.1, 0.1, function=white_noise)
    #time.sleep(0.02)

# pig
""" 
a = pink
b = hsv_colour(0.9, 0.4, 1)
c = hsv_colour(0.9, 0.2, 1)
d = hsv_colour(0.92, 0.5, 1)
e = hsv_colour(0.9, 0.3, 1)
f = hsv_colour(0.07, 0.6, 1)
w = white

creeper_face = [
    [b,a,d,b,c,d,c,e],
    [d,a,d,d,a,a,e,e],
    [a,e,c,d,b,b,e,e],
    [0,w,b,b,d,d,w,0],
    [e,e,c,c,c,b,c,e],
    [e,e,f,b,b,f,c,c],
    [e,b,c,c,c,b,c,c],
    [e,e,d,d,b,d,c,c]
]
creeper = [
    [b,a,d,b,c,d,c,e],
    [d,a,d,d,a,a,e,e],
    [a,e,a,d,b,b,e,e],
    [d,b,a,d,d,d,a,c],
    [a,e,a,d,c,b,c,e],
    [c,e,f,b,b,f,c,c],
    [a,e,c,c,c,b,a,c],
    [e,e,d,d,b,d,c,a]
]
 """