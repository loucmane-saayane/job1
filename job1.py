def draw_rectangle(width,height):
    print("|"+"-"*(width-1)+"|")
    for in range(height-2):
    print("|"+""*(width*2-1)+"|")
    if height>1:
        print("|"+"-"*(width-1)+"|")
    draw_rectangle(10,3)

 



