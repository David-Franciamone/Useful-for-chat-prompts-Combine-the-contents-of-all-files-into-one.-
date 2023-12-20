import os
import tkinter as tk
from tkinter import filedialog, messagebox

allContentsOfAllFiles = []

def select_input_directory():
    global input_directory
    input_directory = filedialog.askdirectory()
    input_directory_label.config(text=f"Input Directory: {input_directory}")

def select_output_directory():
    global output_directory
    output_directory = filedialog.askdirectory()
    output_directory_label.config(text=f"Output Directory: {output_directory}")

def search_files_in_directory(directory, file_extension):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            search_files_in_directory(item_path, file_extension)
        elif item.endswith(file_extension):
            with open(item_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()
                allContentsOfAllFiles.append(file_contents)

def save_to_text_file():
    global input_directory, output_directory
    file_extension = selected_file_type.get()  # Use selected_file_type to get the selected value

    if not input_directory or not output_directory:
        messagebox.showerror("Error", "Please make sure that the input directory and output directory have been chosen before continuing.")
        return

    start_button.config(text="Processing", state="disabled")
    status_label.config(text="Processing...")

    allContentsOfAllFiles.clear()
    search_files_in_directory(input_directory, file_extension)

    # Save the contents to a text file
    output_file_path = os.path.join(output_directory, f"allContentsOfAll{file_extension}Files.txt")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for content in allContentsOfAllFiles:
            output_file.write(content)

    start_button.config(text="Program Complete", state="normal")
    status_label.config(text=f"Text file saved to: {output_file_path}")

def show_info_form(event=None):  # Added 'event=None' to handle click event
    info_window = tk.Toplevel(root)
    info_window.title("Information")
    info_text = "Name: David Franciamone\nPhone Number: (442) 370-5470\nEmail: DavidFranciamone@gmail.com"
    
    info_text_widget = tk.Text(info_window, height=5, width=40)
    info_text_widget.insert(tk.END, info_text)
    info_text_widget.configure(state="disabled")  # Disable text widget for read-only
    info_text_widget.pack()

def close_program():
    root.quit()

# Create a GUI window
root = tk.Tk()
root.title("File Contents Extractor")

# Maximize the window
root.state('zoomed')

# Create buttons for selecting input and output directories
select_input_button = tk.Button(root, text="1.   Select Input Directory", command=select_input_directory)
select_output_button = tk.Button(root, text="2.   Select Output Directory", command=select_output_directory)
select_input_button.pack()
select_output_button.pack()

# Labels to display selected directories
input_directory_label = tk.Label(root, text="Input Directory: None")
output_directory_label = tk.Label(root, text="Output Directory: None")
input_directory_label.pack()
output_directory_label.pack()

# Add space between Select File Type label and components above it
space_label1 = tk.Label(root, text="", height=2)  # Adjust the height for space
space_label1.pack()

# Drop-down list for file types
file_types = [".txt", ".csv", ".json", ".xml", ".cs"]  # Add more file types as needed
selected_file_type = tk.StringVar(root, ".txt")
file_type_label = tk.Label(root, text="3.   Select File Type:")
file_type_label.pack()

file_type = tk.OptionMenu(root, selected_file_type, *file_types)
file_type.pack()

# Add space between Start button and components above it
space_label2 = tk.Label(root, text="", height=2)  # Adjust the height for space
space_label2.pack()

# Button to start the process
start_button = tk.Button(root, text="4.   Start", command=save_to_text_file)
start_button.pack()

# Status label to display messages
status_label = tk.Label(root, text="")
status_label.pack()

# Button to close the program
close_button = tk.Button(root, text="5.   Close Program", command=close_program)
close_button.pack()

# Create the "Programmer's Contact Info" label with underlined and bold text
contact_info_label = tk.Label(root, text="Programmer's Contact Info", fg="blue", cursor="hand2", anchor="se")
contact_info_label.config(font=("Arial", 12, "bold underline"))
contact_info_label.pack(side="bottom", padx=10, pady=10)
contact_info_label.bind("<Button-1>", show_info_form)  # Bind the click event to show_info_form function

root.mainloop()
