import tkinter as tk
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

        # Create a button to generate the random video link
        generate_button = tk.Button(self.root, text="Generate Random Video Link", bg='gray', fg="white", command=self.show_random_link)
        generate_button.pack(pady=20)
        # Label to display the generated video link
        self.link_label = tk.Label(self.root, text="adf", wraplength=400, bg='#00050F', fg="white")
        self.link_label.pack()

        # Start the GUI event loop
        self.root.mainloop()

    def show_random_link(self):
        link = self.youtube_instance.get_random_video()
        self.link_label.config(text=link)

        # Open the link in a web browser
        if link:
            webbrowser.open_new(link)
