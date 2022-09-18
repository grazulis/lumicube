# Draw some pixel art hearts.

r = green
b = purple
y = pink
heart = [
    [0,0,0,0,0,0,0,0],
    [0,r,r,0,0,r,r,0],
    [r,r,r,r,r,r,r,r],
    [y,y,y,y,y,y,y,y],
    [0,y,y,y,y,y,y,0],
    [0,0,b,b,b,b,0,0],
    [0,0,0,b,b,0,0,0],
    [0,0,0,0,0,0,0,0],
]
display.set_panel("left", heart)
display.set_panel("right", heart)
display.set_panel("top", heart)