import tkinter as tk
from datetime import datetime
from tkinter import ttk

from YoutubeApi import YoutubeApi
import webbrowser

class UI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube_instance = YoutubeApi(self.api_key)
        self.link_history = []  # List to store past links

    def generateUI(self):
        self.root = tk.Tk()
        self.root.title("Interdimensional Cable TV")
        self.root.geometry("1200x800")
        self.root.configure(bg='#00050F')

        current_year = datetime.now().year

        # Create a large label at the top with a custom font
        custom_font = ('Arial', 24, 'bold')
        title_label = tk.Label(self.root, text="Interdimensional Cable TV", font=custom_font, bg='#00050F',
                               fg="white")
        title_label.grid(row=0, column=1, pady=20)  # Row 0, Column 1 for title

        # Frame for link history
        history_frame = tk.Frame(self.root, bg='#00050F')
        history_frame.grid(row=1, column=0, rowspan=2, padx=10, pady=10)  # Row 1, Column 0 for link history

        history_label = tk.Label(history_frame, text="Link History", bg='#00050F', fg="white")
        history_label.pack()

        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.link_listbox = tk.Listbox(history_frame, yscrollcommand=scrollbar.set, bg='gray', fg="white", width=50,
                                       height=40)
        self.link_listbox.pack(fill='both', expand=True)
        self.link_listbox.bind('<Double-Button-1>', self.open_selected_link)  # Bind double-click event

        scrollbar.config(command=self.link_listbox.yview)

        # Frame for the rest of the elements
        main_frame = tk.Frame(self.root, bg='#00050F')
        main_frame.grid(row=1, column=1, padx=10, pady=10)  # Row 1, Column 1 for other elements

        # Create a Scale widget for selecting minimum year
        self.min_year_scale = tk.Scale(main_frame, from_=2002, to=current_year, orient=tk.HORIZONTAL, bg='gray',
                                       fg="white")
        self.min_year_scale.grid(row=0, column=0, padx=10, pady=10)

        # Create a Scale widget for selecting maximum year
        self.max_year_scale = tk.Scale(main_frame, from_=2002, to=current_year, orient=tk.HORIZONTAL, bg='gray',
                                       fg="white")
        self.max_year_scale.set(current_year)  # Set the maximum value to the current year
        self.max_year_scale.grid(row=0, column=1, padx=10, pady=10)

        # Create a TextBox for entering the keyword
        self.keyword_label = tk.Label(main_frame, text="Enter Keyword", bg='#00050F', fg="white")
        self.keyword_label.grid(row=1, column=0)

        self.keyword_entry = tk.Entry(main_frame, bg='gray', fg="white")
        self.keyword_entry.grid(row=1, column=1)

        # Create a dropdown menu for video states
        self.video_state_label = tk.Label(main_frame, text="Select Video State", bg='#00050F', fg="white")
        self.video_state_label.grid(row=2, column=0)

        self.video_states = ['any', 'short', 'medium', 'long']
        self.video_state_combobox = ttk.Combobox(main_frame, values=self.video_states, state="readonly")
        self.video_state_combobox.current(0)  # Set the default value to the first state ('any')
        self.video_state_combobox.grid(row=2, column=1, pady=20)  # Adding space below the combobox

        # Create a Frame for views sliders
        views_frame = tk.Frame(self.root, bg='#00050F')
        views_frame.grid(row=2, column=1, padx=10, pady=10)  # Row 2, Column 1 for views sliders

        # Create a slider for minimum views
        self.min_views_slider = tk.Scale(views_frame, from_=1, to=1000000, orient=tk.HORIZONTAL, length=300)
        self.min_views_slider.pack(pady=20)

        # Create a slider for maximum views
        self.max_views_slider = tk.Scale(views_frame, from_=1, to=1000000, orient=tk.HORIZONTAL, length=300)
        self.max_views_slider.pack(pady=20)

        # Create a button to generate the random video link
        generate_button = tk.Button(main_frame, text="Generate Random Video Link", bg='gray', fg="white",
                                    command=self.show_random_link)
        generate_button.grid(row=3, columnspan=2, pady=20)

        # Label to display the generated video link
        self.link_label = tk.Label(main_frame, text="", wraplength=400, bg='#00050F', fg="white")
        self.link_label.grid(row=4, columnspan=2)

        # Start the GUI event loop
        self.root.mainloop()


    def show_random_link(self):
        min_year = self.min_year_scale.get()
        max_year = self.max_year_scale.get()
        min_views = self.min_views_slider.get()
        max_views = self.max_views_slider.get()

        keyword = self.keyword_entry.get()  # Get the keyword from the entry widget
        selected_state = self.video_state_combobox.get()  # Get the selected video state

        link = self.youtube_instance.get_random_video(min_year, max_year, keyword, selected_state)
        self.link_label.config(text=link)

        # Open the link in a web browser
        if link:
            webbrowser.open_new(link)
            self.link_history.append(link)  # Add the link to the history
            self.update_link_history()  # Update the link history listbox

    def open_selected_link(self, event):
        selection = self.link_listbox.curselection()
        if selection:
            index = selection[0]
            link = self.link_listbox.get(index)
            webbrowser.open_new(link)

    def update_link_history(self):
        self.link_listbox.delete(0, tk.END)  # Clear the listbox
        for link in self.link_history:
            self.link_listbox.insert(tk.END, link)