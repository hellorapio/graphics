import tkinter as tk

def midPointAlgo(centerX, centerY, radius):
    x = 0
    y = radius
    decisionParam = 1 - radius
    pointsArray = []

    while x <= y:
        x += 1
        if decisionParam <= 0:
            decisionParam = decisionParam + 2 * x + 3
        else:
            y -= 1
            decisionParam = decisionParam + 2 * (x - y) + 5

        pointsArray.append((x + centerX, y + centerY))
    
    return pointsArray

def getOctant(pointsArray, octantNumber):
    if octantNumber == 1:
        return pointsArray
    elif octantNumber == 2:
        return [(y, x) for x, y in pointsArray]
    elif octantNumber == 3:
        return [(y, -x) for x, y in pointsArray]
    elif octantNumber == 4:
        return [(x, -y) for x, y in pointsArray]
    elif octantNumber == 5:
        return [(-x, -y) for x, y in pointsArray]
    elif octantNumber == 6:
        return [(-y, -x) for x, y in pointsArray]
    elif octantNumber == 7:
        return [(-y, x) for x, y in pointsArray]
    elif octantNumber == 8:
        return [(-x, y) for x, y in pointsArray]
    else:
        raise ValueError("Invalid octant number. Must be between 1 and 8.")

def draw_circle(canvas, centerX, centerY, radius):
    pointsArray = midPointAlgo(centerX, centerY, radius)

    # Draw the circle in all 8 octants
    for octant in range(1, 9):
        octant_points = getOctant(pointsArray, octant)
        for x, y in octant_points:
            canvas.create_rectangle(x, y, x+1, y+1, outline="black")

class App:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        # Entry widgets for user input
        self.centerX_entry = tk.Entry(master, width=5)
        self.centerY_entry = tk.Entry(master, width=5)
        self.radius_entry = tk.Entry(master, width=5)

        # Button to draw the circle
        self.draw_button = tk.Button(master, text="Draw Circle", command=self.draw_circle)

        # Place widgets on the window
        tk.Label(master, text="Center X:").pack(side=tk.LEFT)
        self.centerX_entry.pack(side=tk.LEFT)
        tk.Label(master, text="Center Y:").pack(side=tk.LEFT)
        self.centerY_entry.pack(side=tk.LEFT)
        tk.Label(master, text="Radius:").pack(side=tk.LEFT)
        self.radius_entry.pack(side=tk.LEFT)
        self.draw_button.pack(side=tk.LEFT)

    def draw_circle(self):
        # Get user input for circle center and radius
        centerX = int(self.centerX_entry.get())
        centerY = int(self.centerY_entry.get())
        radius = int(self.radius_entry.get())

        # Draw the circle on the canvas
        draw_circle(self.canvas, centerX, centerY, radius)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()




# import tkinter as tk

# def midPointAlgo(centerX, centerY, radius):
# 	# 1. Initialization of variables
# 	x = 0
# 	y = radius
# 	decisionParam = 1 - radius
	
# 	pointsArray = []

# 	while x < y:
# 		x += 1
# 		# 2. decision making by checking the cases
# 		if(decisionParam <= 0):
# 			decisionParam = decisionParam + 2 * x + 3
# 		else:
# 			y -= 1
# 			decisionParam = decisionParam + 2 * (x - y) + 5
		
# 		pointsArray.append((x + centerX, y + centerY))
		
# 	return pointsArray
	
# def getOctant(pointsArray, octantNumber):
#     if octantNumber == 1:
#         return pointsArray
#     elif octantNumber == 2:
#         return [(y, x) for x, y in pointsArray]
#     elif octantNumber == 3:
#         return [(y, -x) for x, y in pointsArray]
#     elif octantNumber == 4:
#         return [(x, -y) for x, y in pointsArray]
#     elif octantNumber == 5:
#         return [(-x, -y) for x, y in pointsArray]
#     elif octantNumber == 6:
#         return [(-y, -x) for x, y in pointsArray]
#     elif octantNumber == 7:
#         return [(-y, x) for x, y in pointsArray]
#     elif octantNumber == 8:
#         return [(-x, y) for x, y in pointsArray]
#     else:
#         raise ValueError("Invalid octant number. Must be between 1 and 8.")							

# print(getOctant(midPointAlgo(0,0,100),6))

# def draw_circle(canvas, centerX, centerY, radius):
#     pointsArray = midPointAlgo(centerX, centerY, radius)

#     # Draw the circle in all 8 octants
#     for octant in range(1, 9):
#         octant_points = getOctant(pointsArray, octant)
#         for x, y in octant_points:
#             canvas.create_rectangle(x, y, x+1, y+1, outline="black")


# class App:
#     def __init__(self, master):
#         self.master = master
#         self.canvas = tk.Canvas(master, width=300, height=300)
#         self.canvas.pack()

#         # Entry widgets for user input
#         self.centerX_entry = tk.Entry(master, width=5)
#         self.centerY_entry = tk.Entry(master, width=5)
#         self.radius_entry = tk.Entry(master, width=5)

#         # Button to draw the circle
#         self.draw_button = tk.Button(master, text="Draw Circle", command=self.draw_circle_from_input)

#         # Place widgets on the window
#         tk.Label(master, text="Center X:").pack(side=tk.LEFT)
#         self.centerX_entry.pack(side=tk.LEFT)
#         tk.Label(master, text="Center Y:").pack(side=tk.LEFT)
#         self.centerY_entry.pack(side=tk.LEFT)
#         tk.Label(master, text="Radius:").pack(side=tk.LEFT)
#         self.radius_entry.pack(side=tk.LEFT)
#         self.draw_button.pack(side=tk.LEFT)

#     def draw_circle_from_input(self):
#         # Get user input for circle center and radius
#         centerX = int(self.centerX_entry.get())
#         centerY = int(self.centerY_entry.get())
#         radius = int(self.radius_entry.get())

#         # Draw the circle on the canvas
#         draw_circle(self.canvas, centerX, centerY, radius)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()