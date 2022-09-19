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
    [g3,g2,g1,g4,g4,g,g3,g1],
    [g2,g1,g3,g1,g2,g1,g,g3],
    [g,g2,g,g3,g1,g,g1,g2],
    [g1,g,g1,g2,g1,g,g3,g]
]
display.set_panel("left", creeper_face)
display.set_panel("right", creeper)
display.set_panel("top", creeper)
