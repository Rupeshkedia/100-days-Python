import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Simple Tkinter Window")

# Set the window size (Width x Height)
root.geometry("400x300")

# Disable window resizing (fixed size)
root.resizable(False, False)

# Start the Tkinter event loop
root.mainloop()