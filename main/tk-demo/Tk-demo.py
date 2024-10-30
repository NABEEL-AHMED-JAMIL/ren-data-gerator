import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter Example")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Function to change the label text when the button is clicked
def change_text():
    label.config(text="Button Clicked!")

# Create a button widget
button = tk.Button(root, text="Click Me", command=change_text)
button.pack(pady=10)

# Run the application
root.mainloop()
