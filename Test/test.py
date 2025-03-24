import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tkinter Layout")
root.geometry("800x600")  # Set the size of the window

# Create a frame for the top container (similar to the "container" div in HTML)
top_frame = tk.Frame(root)
top_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Square with Image (use a label for image)
image_label = tk.Label(top_frame, text="Person Image", bg="lightgray", width=30, height=15)
image_label.grid(row=0, column=0, padx=10, pady=10)

# Side container (containing dropdown and blue box)
side_frame = tk.Frame(top_frame)
side_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Dropdown Menu
dropdown_label = tk.Label(side_frame, text="Dropdown Menu", bg="lightgreen", width=20, height=6)
dropdown_label.pack(padx=10, pady=10)

dropdown = ttk.Combobox(side_frame, values=["Option 1", "Option 2", "Option 3"])
dropdown.pack(padx=10, pady=10)

# Blue box
blue_box = tk.Label(side_frame, text="Content or Graph Here", bg="lightblue", width=20, height=6)
blue_box.pack(padx=10, pady=10)

# Create a frame for the bottom container (graph section)
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Bottom boxes with graphs
box1 = tk.Label(bottom_frame, text="Graph 1", bg="orange", width=30, height=5)
box1.grid(row=0, column=0, padx=10, pady=10)

box2 = tk.Label(bottom_frame, text="Graph 2", bg="purple", width=30, height=5)
box2.grid(row=1, column=0, padx=10, pady=10)

box3 = tk.Label(bottom_frame, text="Graph 3", bg="cyan", width=30, height=5)
box3.grid(row=2, column=0, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
