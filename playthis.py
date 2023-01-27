from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import PhotoImage
from PIL import Image, ImageTk


class Media_Player:
    def __init__(self):
        # chrome_service = Service(usr/bin/local)
        # chrome_service.start()
        options = webdriver.ChromeOptions()
        # Execute script without launching any browser windows (headless)
        options.add_argument("--headless")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        # set TKinter window geometry
        self.window = Tk()
        self.window.rowconfigure(0, weight=4)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.rowconfigure(4, weight=1)
        self.window.rowconfigure(5, weight=1)
        self.window.rowconfigure(6, weight=1)
        self.window.columnconfigure(5, weight=2)
        self.window.columnconfigure(4, weight=2)
        self.window.columnconfigure(3, weight=2)
        self.window.columnconfigure(2, weight=2)
        self.window.columnconfigure(1, weight=2)
        self.window.columnconfigure(0, weight=2)
        

        self.window.geometry("400x400")

        # set background color
        self.window.grid_propagate(0)
        self.window.configure(bg='maroon')

        # create a top menu bar
        menubar = Menu(self.window)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.window.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        self.window.config(menu=menubar)

        # Create a top heading label widget with text "My Media Player"
        top_header = Label(self.window, text="My Media Player", font=("Arial", 24), fg="white", bg="maroon", pady=20, highlightbackground="maroon", highlightthickness=0)
        # Pack the label widget
        top_header.pack()
        

 # TKinter Buttons for each of the radio stations to play and pause / stop

# ============================ KUSC Buttons 
        # Button to play KUSC classical
        self.play_button_kusc_classical = Button(self.window, text="Play KUSC", command=self.play_kusc_classical, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.play_button_kusc_classical.grid(row=1, column=1, ipadx=0, ipady=0, sticky="ne")

        kusc_image = Image.open("images/kusccal.png")
        kusc_image = kusc_image.resize((60, 30), Image.ANTIALIAS)
        self.kusc_image = ImageTk.PhotoImage(kusc_image)
        self.kusc_image_label = Label(self.window, image=self.kusc_image, borderwidth=0, highlightthickness=0)
        self.kusc_image_label.grid(row=1, column=2, ipadx=0, ipady=0, sticky="n")
      

        # Button to stop KUSC Classical
        self.stop_button_kusc_classical = Button(self.window, text="Stop KUSC", command=self.stop_kusc_classical, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.stop_button_kusc_classical.grid(row=1, column=3, ipadx=0, ipady=0, sticky="nw")

# ============================ MN Buttons 
         # Button to play MN Classical
        self.play_button_mn_classical = Button(self.window, text="Play MN", command=self.play_mn_classical, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.play_button_mn_classical.grid(row=2, column=1, ipadx=0, ipady=0, sticky="ne")

# Load the image
        mn_image = Image.open("images/yourclassical1.png")
        mn_image = mn_image.resize((60, 30), Image.ANTIALIAS)
        self.mn_image = ImageTk.PhotoImage(mn_image)
        self.mn_image_label = Label(self.window, image=self.mn_image, borderwidth=0, highlightthickness=0)
        self.mn_image_label.grid(row=2, column=2, ipadx=0, ipady=0, sticky="n")

        # Button to stop MN Classical
        self.stop_button_mn_classical = Button(self.window, text="Stop MN", command=self.stop_mn_classical, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.stop_button_mn_classical.grid(row=2, column=3, ipadx=0, ipady=0, sticky="nw")

# ============================ NPR Buttons  
    
        # Button to play NPR
        self.play_button_npr = Button(self.window, text="Play NPR", command=self.play_npr, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.play_button_npr.grid(row=3, column=1, ipadx=0, ipady=0, sticky="ne")

# Load the image
        npr_image = Image.open("images/npr.png")
        npr_image = npr_image.resize((60, 30), Image.ANTIALIAS)
        self.npr_image = ImageTk.PhotoImage(npr_image)
        self.npr_image_label = Label(self.window, image=self.npr_image, borderwidth=0, highlightthickness=0)
        self.npr_image_label.grid(row=3, column=2, ipadx=0, ipady=0, sticky="n")
        
        # Button to stop NPR
        self.stop_button_npr = Button(self.window, text="Stop NPR", command=self.stop_npr, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.stop_button_npr.grid(row=3, column=3, ipadx=0, ipady=0, sticky="nw")

# ============================ BBC Buttons  
    
        # Button to play BBC
        self.play_button_bbc = Button(self.window, text="Play BBC", command=self.play_bbc, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.play_button_bbc.grid(row=4, column=1, ipadx=0, ipady=0, sticky="ne")

# Load the image
        bbc_image = Image.open("images/bbc.png")
        bbc_image = bbc_image.resize((60, 30), Image.ANTIALIAS)
        self.bbc_image = ImageTk.PhotoImage(bbc_image)
        self.bbc_image_label = Label(self.window, image=self.bbc_image, highlightthickness=0)
        self.bbc_image_label.grid(row=4, column=2, ipadx=0, ipady=0, sticky="n", )

        # Button to stop BBC
        self.stop_button_bbc = Button(self.window, text="Stop BBC", command=self.stop_bbc, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.stop_button_bbc.grid(row=4, column=3, ipadx=0, ipady=0, sticky="nw")
        
 # ============================ CNN Buttons  
    
        # Button to play CNN
        self.play_button_cnn = Button(self.window, text="Play CNN", command=self.play_cnn, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.play_button_cnn.grid(row=5, column=1, ipadx=0, ipady=0, sticky="ne")

# Load the image
        cnn_image = Image.open("images/cnn.png")
        cnn_image = cnn_image.resize((60, 30), Image.ANTIALIAS)
        self.cnn_image = ImageTk.PhotoImage(cnn_image)
        self.cnn_image_label = Label(self.window, image=self.cnn_image, highlightthickness=0)
        self.cnn_image_label.grid(row=5, column=2, ipadx=0, ipady=0, sticky="n")

       # Button to stop CNN
        self.stop_button_cnn = Button(self.window, text="Stop CNN", command=self.stop_cnn, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.stop_button_cnn.grid(row=5, column=3, ipadx=0, ipady=0, sticky="nw")


 # Button to quit with command "self.close_browser" with function to close the browser window

        self.quit_button = Button(self.window, text="Quit", command=self.close_browser, bg="maroon", highlightbackground="maroon", highlightthickness=0)
        self.quit_button.grid(row=6, column=2, ipadx=0, ipady=0, sticky="n")

 # TKinter event loop is started with "mainloop()"
        self.window.mainloop()


# ====================== Webscraping online media players

# Live streaming radio station websites to interact with play and stop or pause buttons

# KUSC
# KUSC Classical Station Play Button
    def play_kusc_classical(self):
        if self.driver.current_url != "https://www.kusc.org/":
            self.driver.get("https://www.kusc.org/")
        play_button_kusc_classical = self.driver.find_element(By.CLASS_NAME, "icon-play")
        play_button_kusc_classical.click()
# KUSC Classical Station Stop Button        
    def stop_kusc_classical(self):
        if self.driver.current_url != "https://www.kusc.org/":
            self.driver.get("https://www.kusc.org/")
        stop_button_kusc_classical = self.driver.find_element(By.CLASS_NAME, "play-button")
        stop_button_kusc_classical.click()


# MN
# Your Classical MN Classical Station Play Button        
    def play_mn_classical(self):
        if self.driver.current_url != "https://www.yourclassical.org/playlist/classical-24":
            self.driver.get("https://www.yourclassical.org/playlist/classical-24")
        play_button_mn_classical = self.driver.find_element(By.CLASS_NAME, "PlaylistPage_buttonCircle__P_VGW")
        play_button_mn_classical.click()
# Your Classical MN Classical Station Stop Button         
    def stop_mn_classical(self):
        if self.driver.current_url != "https://www.yourclassical.org/playlist/classical-24":
            self.driver.get("https://www.yourclassical.org/playlist/classical-24")
        stop_button_mn_classical = self.driver.find_element(By.CLASS_NAME, "PlaylistPage_buttonCircle__P_VGW")
        stop_button_mn_classical.click()


# NPR
# RadioStationUSA NPR Station Play Button
    def play_npr(self):
        if self.driver.current_url != "https://radiostationusa.fm/online/npr-news":
            self.driver.get("https://radiostationusa.fm/online/npr-news")
        play_button_npr = self.driver.find_element(By.CLASS_NAME, "play")
        play_button_npr.click()


# RadioStationUSA NPR Station Stop Button       
    def stop_npr(self):
        if self.driver.current_url != "https://radiostationusa.fm/online/npr-news":
            self.driver.get("https://radiostationusa.fm/online/npr-news")
        stop_button_npr = self.driver.find_element(By.CLASS_NAME, "pause")
        stop_button_npr.click()



# BBC
# RadioStationUSA BBC World Service Station Play Button

    def play_bbc(self):
        if self.driver.current_url != "https://radiostationusa.fm/online/bbc-world-service":
            self.driver.get("https://radiostationusa.fm/online/bbc-world-service")
        play_button_npr = self.driver.find_element(By.CLASS_NAME, "play")
        play_button_npr.click()


# RadioStationUSA BBC World Service Station Stop Button       
    def stop_bbc(self):
        if self.driver.current_url != "https://radiostationusa.fm/online/bbc-world-service":
            self.driver.get("https://radiostationusa.fm/online/bbc-world-service")
        stop_button_npr = self.driver.find_element(By.CLASS_NAME, "pause")
        stop_button_npr.click()



# CNN
# RadioStationUSA CNN Station Play Button

    def play_cnn(self):
        if self.driver.current_url != "https://radiostationusa.fm/online/cnn":
            self.driver.get("https://radiostationusa.fm/online/cnn")
        play_button_npr = self.driver.find_element(By.CLASS_NAME, "play")
        play_button_npr.click()


# RadioStationUSA CNN Station Stop Button       
    def stop_cnn(self):
        if self.driver.current_url != "https://radiostationusa.fm/online/cnn":
            self.driver.get("https://radiostationusa.fm/online/cnn")
        stop_button_npr = self.driver.find_element(By.CLASS_NAME, "pause")
        stop_button_npr.click()




# TKinter Gui Quit Button to close browser        
    def close_browser(self):
        self.driver.quit()
        # chrome_service.stop()

# Instantiate Class
player = Media_Player()


