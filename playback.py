#Freesic 2023
#The code for Tkinter interface for homescreen and Playback controls are inculded here.
#Umesh Kumaar

from tkinter import *
from ctypes import windll
import os
import pygame
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from download_song import add_song


def create_application(root):

    global close_button
    global expand_button
    global minimize_button

    root.overrideredirect(True)
    root.iconbitmap("Freesic\\images\\Freesic_logo.ico") 

    root.minimized = False # only to know if root is minimized
    root.maximized = False # only to know if root is maximized

    LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
    DGRAY = '#25292e' # window background color               (Hex color)
    RGRAY = '#10121f' # title bar color                       (Hex color)

    root.config(bg="#25292e")
    title_bar = Frame(root, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)


    def set_appwindow(mainWindow):
        # Some WindowsOS styles, required for task bar integration
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080

        # Magic
        hwnd = windll.user32.GetParent(mainWindow.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    
        mainWindow.wm_withdraw()
        mainWindow.after(10, lambda: mainWindow.wm_deiconify())
        
    # so you can't see the window when is minimized
    def minimize_me():
        root.attributes("-alpha",0)
        root.minimized = True       

    # so you can see the window when is not minimized
    def deminimize(event):
        root.focus() 
        root.attributes("-alpha",1) 
        if root.minimized == True:
            root.minimized = False                              
            

    def maximize_me():
        # if the window was not maximized
        if root.maximized == False: 
            root.normal_size = root.geometry()
            expand_button.config(text=" 🗗 ")
            #This option is disabled, to enable uncomment the below line
            # root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
            root.maximized = not root.maximized 
            # now it's maximized
            
        else: 
            # if the window was maximized
            expand_button.config(text=" 🗖 ")
            root.geometry(root.normal_size)
            root.maximized = not root.maximized
            # now it is not maximized

    # put a close button on the title bar
    close_button = Button(title_bar, text='  ×  ', command=root.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
    expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
    minimize_button = Button(title_bar, text=' 🗕 ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
    title_bar_title = Label(title_bar, text="Freesic", bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

    # a frame for the main area of the window, this is where the actual app will go
    window = Frame(root, bg=DGRAY,highlightthickness=0)

    # pack the widgets
    title_bar.grid(row=0, column=0, sticky="ew", columnspan=5)
    close_button.grid(row=0, column=7, ipadx=7, ipady=1)
    expand_button.grid(row=0, column=6, ipadx=7, ipady=1)
    minimize_button.grid(row=0, column=5, ipadx=7, ipady=1)
    title_bar_title.grid(row=0, column=0, padx=(10, 194))
    window.grid(row=1, column=0, sticky="nsew")
    #xwin=None
    #ywin=None
    # bind title bar motion to the move window function

    def changex_on_hovering(event):
        global close_button
        close_button['bg']='red'
        
    def returnx_to_normalstate(event):
        global close_button
        close_button['bg']=RGRAY
        
    def change_size_on_hovering(event):
        global expand_button
        expand_button['bg']=LGRAY
        
    def return_size_on_hovering(event):
        global expand_button
        expand_button['bg']=RGRAY

    def changem_size_on_hovering(event):
        global minimize_button
        minimize_button['bg']=LGRAY
        
    def returnm_size_on_hovering(event):
        global minimize_button
        minimize_button['bg']=RGRAY

    def get_pos(event): # this is executed when the title bar is clicked to move the window
        if root.maximized == False:
    
            xwin = root.winfo_x()
            ywin = root.winfo_y()
            startx = event.x_root
            starty = event.y_root

            ywin = ywin - starty
            xwin = xwin - startx

            def move_window(event): 
                # runs when window is dragged
                root.config(cursor="fleur")
                root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

            def release_window(event): 
                # runs when window is released
                root.config(cursor="arrow")
                
            title_bar.bind('<B1-Motion>', move_window)
            title_bar.bind('<ButtonRelease-1>', release_window)
            title_bar_title.bind('<B1-Motion>', move_window)
            title_bar_title.bind('<ButtonRelease-1>', release_window)
        else:
            expand_button.config(text=" 🗖 ")
            root.maximized = not root.maximized

    title_bar.bind('<Button-1>', get_pos) # so you can drag the window from the title bar
    title_bar_title.bind('<Button-1>', get_pos) # so you can drag the window from the title 

    # button effects in the title bar when hovering over buttons
    close_button.bind('<Enter>',changex_on_hovering)
    close_button.bind('<Leave>',returnx_to_normalstate)
    expand_button.bind('<Enter>', change_size_on_hovering)
    expand_button.bind('<Leave>', return_size_on_hovering)
    minimize_button.bind('<Enter>', changem_size_on_hovering)
    minimize_button.bind('<Leave>', returnm_size_on_hovering)

    # resize the window width
    resizex_widget = tk.Frame(window, bg=DGRAY, cursor='sb_h_double_arrow')
    resizex_widget.grid(row=1, column=5, padx=2, sticky="ns")


    def resizex(event):
        xwin = root.winfo_x()
        difference = (event.x_root - xwin) - root.winfo_width()
        
        if root.winfo_width() > 150 : # 150 is the minimum width for the window
            try:
                root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
            except:
                pass
        else:
            if difference > 0: # so the window can't be too small (150x150)
                try:
                    root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
                except:
                    pass
                
        resizex_widget.config(bg=DGRAY)

    resizex_widget.bind("<B1-Motion>",resizex)

    # resize the window height
    resizey_widget = tk.Frame(window, bg=DGRAY, cursor='sb_v_double_arrow')
    resizey_widget.grid(row=2, column=0, pady=2, sticky="ew")


    def resizey(event):
        ywin = root.winfo_y()
        difference = (event.y_root - ywin) - root.winfo_height()

        if root.winfo_height() > 150: # 150 is the minimum height for the window
            try:
                root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
            except:
                pass
        else:
            if difference > 0: # so the window can't be too small (150x150)
                try:
                    root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
                except:
                    pass

        resizex_widget.config(bg=DGRAY)

    resizey_widget.bind("<B1-Motion>",resizey)

    # some settings
    root.bind("<FocusIn>",deminimize) # to view the window by clicking on the window icon on the taskbar
    root.after(10, lambda: set_appwindow(root)) # to see the icon on the task bar


    #The code for title bar customization is over, and my code goes below
    # ===================================================================================================

    folder_path = "Freesic\\Playlist"
    pygame.init()
    audio_arr = []
    root.iconbitmap("Freesic\\images\\Freesic_logo.ico")

    # Create a vertical scrollbar for the listbox
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)

    # Increase the width and height of the listbox
    listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=5, yscrollcommand=scrollbar.set, bg = "#25292e", fg = "white", borderwidth=3)

    def select_folder(folder_path):
        if folder_path:
            audio_files = []
            audio_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp3', '.wav', '.ogg', '.aac')) and f not in audio_files]
            listbox.delete(0, tk.END)
            for audio in audio_files:
                if audio not in audio_arr:
                    audio_arr.append(audio)
                listbox.insert(tk.END, audio)

    scrollbar.config(command=listbox.yview, bg = "#25292e", borderwidth=0)
    scrollbar.grid(row=4, column=4, sticky="ns", rowspan=1,padx=(5,0) ,pady= (60,10))
    listbox.grid(row=4, column=0, pady=(60,10), columnspan=5)

    select_folder("Freesic\\Playlist")

    def display_image(image_path):
        try:
            if image_path !=  "Freesic\\images\\Freesic_pic.png":
                image_path = "Freesic\\songs_pic\\" + image_path[:-3] + "jpg"

            image = Image.open(image_path)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(root, image=photo)
            label.photo = photo
            label.grid(row=1, column=0, pady=(20, 20), columnspan=5)

        except Exception as e:
            print(f"Error displaying the image: {str(e)}")
    display_image("Freesic\\images\\Freesic_pic.png")

    output_text = tk.Text(root, wrap=tk.WORD, width=30, height=1,bg = "#25292e", fg = "white", borderwidth=3)
    output_text.grid(row=2, column=0, padx=(50, 0), pady = (0,10), columnspan=4)
    
    #Playback controls start here:

    def play_clicked(selected_audio):
        selected_audio = listbox.get(tk.ACTIVE)
        current_index = audio_arr.index(selected_audio)
        play(current_index)

    def toggle_play_pause():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            play_pause_button.config(text="▶")
        else:
            pygame.mixer.music.unpause()
            play_pause_button.config(text="||")

    def display_output(text_to_display):
        output_text.delete("1.0", tk.END)
        text_to_display = "Now Playing " + text_to_display[:-4] +"!"
        output_text.insert(tk.END, text_to_display)

    def play_selected_audio(signal=0):
        global current_song_index
        if signal == 1:
            current_song_index -= 1
        elif signal == 2:
            current_song_index += 1
        play(current_song_index)

    def play(current_index):
        global current_song_index

        if current_index >= len(audio_arr):
            current_index = 0

        if current_index < 0:
            current_index = len(audio_arr) - 1

        current_song_index = current_index

        selected_audio = audio_arr[current_index]
        display_image(selected_audio)
        audio_path = os.path.join(folder_path, selected_audio)
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        text_to_display= selected_audio
        display_output(text_to_display)

    def manage_add_fn():
        manage_add = tk.Toplevel(root)
        manage_add.config(bg="#25292e")
        manage_add.title("Add Song")

        input_field = tk.Entry(manage_add, bg = "#25292e", fg = "white", borderwidth=5)
        input_field.grid(row=0, column=0, padx=10, pady=25, columnspan=3)

        def add_protocol():
            add_song(input_field.get())
            manage_add.destroy()
            select_folder(folder_path)

        # Create and position the "Add" button
        add_button = tk.Button(manage_add, text="Add", command=add_protocol, bg = "#25292e", fg = "white", borderwidth=5)
        add_button.grid(row=0, column=3, padx=1)

    #Homescreen Buttons
    play_button = tk.Button(root, text="Play", command=lambda: [play_clicked(listbox.get(tk.ACTIVE))], borderwidth =3, width= 4)
    play_button.configure(bg='#25292e', fg='white')
    play_button.grid(row=6, column=2, padx=(0, 0), pady=(10, 5))

    add_button = tk.Button(root, text="Add", command=manage_add_fn, bg = "#25292e", fg = "white", borderwidth=3, width=4)
    add_button.grid(row=6, column=0, padx=(50, 0), pady=(10, 5))

    prev_button = tk.Button(root, text="⏮️", command=lambda: [play_selected_audio(1)], width=5, relief="flat", borderwidth=0)
    prev_button.configure(bg='#25292e', fg='white')
    prev_button.grid(row=3, column=0, padx=(85, 5), pady=10)

    play_pause_button = tk.Button(root, text="■", command=toggle_play_pause, width=5,relief="flat", borderwidth=0)
    play_pause_button.configure(bg='#25292e', fg='white')
    play_pause_button.grid(row=3, column=1, padx=5, pady=10)

    next_button = tk.Button(root, text="⏭️", command=lambda: [play_selected_audio(2)], width=5, relief="flat", borderwidth=0)
    next_button.configure(bg='#25292e', fg='white')
    next_button.grid(row=3, column=2, padx=5, pady=10)

    #Additional feature: Volume control
    # def set_volume(volume):
    #     pygame.mixer.music.set_volume(volume)
    # volume_scale = tk.Scale(root, from_=1.0, to=0.0, resolution=0.1, orient=tk.VERTICAL, bg="#272626", fg="white", label="", command=lambda vol: set_volume(float(vol)))
    # volume_scale.set(1.0)
    # volume_scale.grid(row=1, column=0, padx=10, pady=10, columnspan=1, rowspan=1)

    # Set the root dimensions to fullscreen
    root.geometry("400x600")
    root.resizable(False, False)

    #Freesic by Umesh Kumaar 
    # ===================================================================================================`