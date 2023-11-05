#Freesic 2023
#The main function
#Umesh Kumaar

from tkinter import Tk
from playback import create_application

if __name__ == "__main__":
    root = Tk()
    root.title("Freesic")
    create_application(root)
    root.mainloop()