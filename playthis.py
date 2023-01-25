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
        self.window.geometry("400x400")

        # Create a menu bar
        menubar = Menu(self.window)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.window.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        self.window.config(menu=menubar)


        # Create a canvas to display the background image
        self.canvas = Canvas(self.window, bg="blue")
        self.canvas.pack(expand=YES, fill=BOTH)

        # Load the image
        img = Image.open("images/radio.png")
        # Resize the image
        img = img.resize((400, 400), Image.ANTIALIAS)
        # Convert the image to PhotoImage object
        self.bg_image = ImageTk.PhotoImage(img)

        # Set the background image of the canvas
        self.canvas.create_image(0, 0, image=self.bg_image, anchor=NW, tags="bg_img")
        self.canvas.lower("bg_img")



    # TKinter Buttons for each of the radio stations to play and pause / stop

        # Button to play and pause KUSC classical music
        self.play_button_kusc_classical = Button(self.window, text="Play", command=self.play_kusc_classical)
        self.play_button_kusc_classical.place(x=40, y=60)

        # Load the image
        img = Image.open("images/kusc.jpeg")
        # Resize the image
        img = img.resize((80, 50), Image.ANTIALIAS)
        # Convert the image to PhotoImage object
        self.bg_image = ImageTk.PhotoImage(img)
        self.image_label = Label(self.window, image=self.bg_image)
        self.image_label.place(x=120, y=50)

        self.stop_button_kusc_classical = Button(self.window, text="Stop ", command=self.stop_kusc_classical)
        self.stop_button_kusc_classical.place(x=240, y=60)

         # Button to play and pause MN Classical
        self.play_button_mn_classical = Button(self.window, text="Play MN", command=self.play_mn_classical)
        self.play_button_mn_classical.place(x=40, y=120)
        self.stop_button_mn_classical = Button(self.window, text="Stop MN", command=self.stop_mn_classical)
        self.stop_button_mn_classical.place(x=240, y=120)

        # Button to play and pause NPR.org NPR
        self.play_button_npr = Button(self.window, text="Play NPR", command=self.play_npr)
        self.play_button_npr.place(x=40, y=160)
        self.stop_button_npr = Button(self.window, text="Stop NPR", command=self.stop_npr)
        self.stop_button_npr.place(x=240, y=160)


        # Button to play and pause  BBC
        self.play_button_bbc = Button(self.window, text="Play BBC", command=self.play_bbc)
        self.play_button_bbc.place(x=40, y=200)
        self.stop_button_bbc = Button(self.window, text="Stop BBC", command=self.stop_bbc)
        self.stop_button_bbc.place(x=240, y=200)
       
        # Button to play and pause CNN
        self.play_button_cnn = Button(self.window, text="Play CNN", command=self.play_cnn)
        self.play_button_cnn.place(x=40, y=240)
        self.stop_button_cnn = Button(self.window, text="Stop CNN", command=self.stop_cnn)
        self.stop_button_cnn.place(x=240, y=240)


 # Button to quit with command "self.close_browser" with function to close the browser window
  

        self.quit_button = Button(self.window, text="Quit", command=self.close_browser)
        self.quit_button.place(x=120, y=300)

 # TKinter event loop is started with "mainloop()"
        self.window.mainloop()

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


