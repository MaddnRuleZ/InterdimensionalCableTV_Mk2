import tkinter as tk
from datetime import datetime
from tkinter import ttk

from YoutubeApi import YoutubeApi
import webbrowser

class UI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube_instance = YoutubeApi(self.api_key)

    def generateUI(self):
        self.root = tk.Tk()
        self.root.title("Random YouTube Video Generator")
        self.root.geometry("1200x800")
        self.root.configure(bg='#00050F')

        current_year = datetime.now().year

        # Create a Scale widget for selecting minimum year
        self.min_year_label = tk.Label(self.root, text="Select Min Year", bg='#00050F', fg="white")
        self.min_year_label.pack()
        self.min_year_scale = tk.Scale(self.root, from_=2002, to=current_year, orient=tk.HORIZONTAL, bg='gray',
                                       fg="white")
        self.min_year_scale.pack()

        # Create a Scale widget for selecting maximum year
        self.max_year_label = tk.Label(self.root, text="Select Max Year", bg='#00050F', fg="white")
        self.max_year_label.pack()
        self.max_year_scale = tk.Scale(self.root, from_=2002, to=current_year, orient=tk.HORIZONTAL, bg='gray',
                                       fg="white")
        self.max_year_scale.set(current_year)  # Set the maximum value to the current year
        self.max_year_scale.pack()

        # Create a TextBox for entering the keyword
        self.keyword_label = tk.Label(self.root, text="Enter Keyword", bg='#00050F', fg="white")
        self.keyword_label.pack()
        self.keyword_entry = tk.Entry(self.root, bg='gray', fg="white")
        self.keyword_entry.pack()

        # Create a dropdown menu for video states
        self.video_state_label = tk.Label(self.root, text="Select Video State", bg='#00050F', fg="white")
        self.video_state_label.pack()
        self.video_states = ['any', 'short', 'medium', 'long']
        self.video_state_combobox = ttk.Combobox(self.root, values=self.video_states, state="readonly")
        self.video_state_combobox.current(0)  # Set the default value to the first state ('any')
        self.video_state_combobox.pack()

        # Create a button to generate the random video link
        generate_button = tk.Button(self.root, text="Generate Random Video Link", bg='gray', fg="white",
                                    command=self.show_random_link)
        generate_button.pack(pady=20)

        # Label to display the generated video link
        self.link_label = tk.Label(self.root, text="", wraplength=400, bg='#00050F', fg="white")
        self.link_label.pack()

        # Start the GUI event loop
        self.root.mainloop()

    def show_random_link(self):
        min_year = self.min_year_scale.get()
        max_year = self.max_year_scale.get()
        keyword = self.keyword_entry.get()  # Get the keyword from the entry widget
        selected_state = self.video_state_combobox.get()  # Get the selected video state

        link = self.youtube_instance.get_random_video(min_year, max_year, keyword, selected_state)
        self.link_label.config(text=link)

        # Open the link in a web browser
        if link:
            webbrowser.open_new(link)
