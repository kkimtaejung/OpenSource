import tkinter
tk = tkinter.Tk()

canvas = tkinter.Canvas(width = 500, height = 350, bg = "white")
canvas.pack()

gameMap = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]
for y in range(7):
    for x in range(10):
        if gameMap[y][x] == 1:
            canvas.create_rectangle(x *50, y*50, x*50+50, y*50+50, fill="yellow")

tk.mainloop()