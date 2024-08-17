import tkinter as tk


# Function to handle the first and second clicks
def on_click(event):
    global start_x, start_y, click_count

    # First click (define start point)
    if click_count == 0:
        start_x, start_y = event.x, event.y
        click_count = 1

    # Second click (define end point and draw line)
    elif click_count == 1:
        end_x, end_y = event.x, event.y
        canvas.create_line(start_x, start_y, end_x, end_y)
        click_count = 0  # Reset click count to allow drawing another line


# Create the main window
root = tk.Tk()
root.title("Draw Line on Canvas")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Initialize variables
click_count = 0
start_x = start_y = 0

# Bind left mouse button click event to the on_click function
canvas.bind("<Button-1>", on_click)

# Start the Tkinter main loop
root.mainloop()