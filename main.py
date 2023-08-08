from customtkinter import filedialog as fd
from methods import encode, decode
import customtkinter 


# Define functions

def file_select():
        file_ = fd.askopenfilename(title="Select a file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        print(file_ + " was selected!") 

if __name__ == "__main__":
    
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    # Initialzing window
    app = customtkinter.CTk()
    app.iconbitmap("favicon.ico")
    app.geometry("800x480")
    app.resizable(False, False)
    app.title("ASCII")
    
    #############################################


    button = customtkinter.CTkButton(master=app, text="Select File", command=file_select)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        


    app.mainloop()  