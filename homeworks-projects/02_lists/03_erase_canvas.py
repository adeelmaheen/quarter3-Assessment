import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App with Eraser")

        # Initialize drawing settings
        self.color = "black"  # Default drawing color
        self.eraser_on = False  # Eraser is initially off

        # Create a canvas for drawing
        self.canvas = tk.Canvas(root, bg="white", width=500, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events to the canvas
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Create buttons to switch between drawing and erasing
        self.draw_button = tk.Button(root, text="Draw", command=self.set_draw)
        self.draw_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.erase_button = tk.Button(root, text="Erase", command=self.set_erase)
        self.erase_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.old_x = None
        self.old_y = None

    def set_draw(self):
        """Activate drawing mode."""
        self.eraser_on = False
        self.color = "black"

    def set_erase(self):
        """Activate eraser mode."""
        self.eraser_on = True
        self.color = "white"

    def paint(self, event):
        """Handle drawing and erasing on the canvas."""
        if self.eraser_on:
            # Erase by deleting items under the cursor
            x1, y1 = event.x - 10, event.y - 10
            x2, y2 = event.x + 10, event.y + 10
            items = self.canvas.find_overlapping(x1, y1, x2, y2)
            for item in items:
                self.canvas.delete(item)
        else:
            # Draw a line
            if self.old_x and self.old_y:
                self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                        width=2, fill=self.color, capstyle=tk.ROUND, smooth=True)
            self.old_x = event.x
            self.old_y = event.y

    def reset(self, event):
        """Reset the starting point for drawing."""
        self.old_x = None
        self.old_y = None

    def clear_canvas(self):
        """Clear all items from the canvas."""
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


