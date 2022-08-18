import kivy
from kivy.app import App
from kivy.metrics import dp
from kivy.config import Config
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.animation import Animation

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.core.window import Window

from kivy.properties import StringProperty, BooleanProperty, NumericProperty

Window.size = (650, 800)

class HuyNguyeen(RelativeLayout):
    
    # Main menu
    
        # Stop Watch
    sw_seconds = 0
    sw_started = False
    onStarted = False 
    sw_started2 = False
    
    def update_time(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        if self.sw_started2:
            self.Total += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        part_seconds = seconds * 100 % 100
        self.ids.stopWatch.text = f'{int(minutes):02}:{int(seconds):02},[size=40]{int(part_seconds):02}[/size]'
        
    def on_start(self):
        if self.onStarted == False:
            Clock.schedule_interval(self.update_time, 0)
    
    def startStop(self):
        if self.sw_started:
            self.ids.startStop.text = 'Bắt đầu'
        else:
            self.ids.startStop.text = 'Dừng'
        self.sw_started = not self.sw_started
        self.on_start()
        self.onStarted = True
    def reset(self):
        if self.sw_started:
            self.ids.startStop.text = 'Bắt đầu'
            self.sw_started = False
        self.sw_seconds = 0
    
        #Add time function
    current_secondsA = 0
    current_secondsB = 0
    current_secondsC = 0
    
    
    # Total Time
    
    Total = 0
    
    def addTotal(self):
        if self.Total == 0:
            minutes, seconds = divmod(self.sw_seconds, 60)
            part_seconds = seconds * 100 % 100
            self.ids.totalTime.text = f'{int(minutes):02}:{int(seconds):02},[size=14]{int(part_seconds):02}[/size]'
        else:
            newsw_seconds = self.sw_seconds + self.Total
            minutes, seconds = divmod(newsw_seconds, 60)
            part_seconds = seconds * 100 % 100
            self.ids.totalTime.text = f'{int(minutes):02}:{int(seconds):02},[size=14]{int(part_seconds):02}[/size]' 
        if self.Total == 0:
            self.Total = self.sw_seconds
        else:
            self.Total = newsw_seconds
    
    
        
    def addTimeA(self):
        if self.current_secondsA == 0:
            minutes, seconds = divmod(self.sw_seconds, 60)
            part_seconds = seconds * 100 % 100
            self.ids.timeA.text = f'{int(minutes):02}:{int(seconds):02},[size=40]{int(part_seconds):02}[/size]'
        else:
            newsw_seconds = self.sw_seconds + self.current_secondsA
            minutes, seconds = divmod(newsw_seconds, 60)
            part_seconds = seconds * 100 % 100
            self.ids.timeA.text = f'{int(minutes):02}:{int(seconds):02},[size=40]{int(part_seconds):02}[/size]' 
        if self.current_secondsA == 0:
            self.current_secondsA = self.sw_seconds
        else:
            self.current_secondsA = newsw_seconds
        self.addTotal()
        self.reset()
    def addTimeB(self):
        if self.current_secondsB == 0:
            minutes, seconds = divmod(self.sw_seconds, 60)
            part_seconds = seconds * 100 % 100
            self.ids.timeB.text = f'{int(minutes):02}:{int(seconds):02},[size=40]{int(part_seconds):02}[/size]'
        else:
            newsw_seconds = self.sw_seconds + self.current_secondsB
            minutes, seconds = divmod(newsw_seconds, 60)
            part_seconds = seconds * 100 % 100
            self.ids.timeB.text = f'{int(minutes):02}:{int(seconds):02},[size=40]{int(part_seconds):02}[/size]' 
        if self.current_secondsB == 0:
            self.current_secondsB = self.sw_seconds
        else:
            self.current_secondsB = newsw_seconds
        self.addTotal()
        self.reset()
    def addTimeC(self):
        if self.current_secondsC == 0:
            minutes, seconds = divmod(self.sw_seconds, 60)
            part_seconds = seconds * 100 % 100
            self.ids.timeC.text = f'{int(minutes):02}:{int(seconds):02},[size=40]{int(part_seconds):02}[/size]'
        else:
            newsw_seconds = self.sw_seconds + self.current_secondsC
            minutes, seconds = divmod(newsw_seconds, 60)
            part_seconds = seconds * 100 % 100
            self.ids.timeC.text = f'{int(minutes):02}:{int(seconds):02},[size=40]{int(part_seconds):02}[/size]' 
        if self.current_secondsC == 0:
            self.current_secondsC = self.sw_seconds
        else:
            self.current_secondsC = newsw_seconds
        self.addTotal()
        self.reset()
    
    # Reset All
    def resetAll(self):
        self.current_secondsA = 0
        self.current_secondsB = 0
        self.current_secondsC = 0
        self.Total = 0
        self.ids.timeA.text = '00:00,[size=40]00[/size]'
        self.ids.timeB.text = '00:00,[size=40]00[/size]'
        self.ids.timeC.text = '00:00,[size=40]00[/size]'
        self.ids.totalTime.text = '00:00,[size=14]00[/size]'
        
        
    # Change timer name
    applied = BooleanProperty(False)
    
    buttonStatus = BooleanProperty(True)
    
    def apply(self):
        self.applied = True
        self.buttonStatus = False
        self.ids.subjectName.text = self.ids.subject.text
    def change(self):
        self.applied = False
        self.buttonStatus = True
        self.resetAll()
        self.ids.subjectName.text = 'Môn kiêm tra thử'
    
    
    

class KiemTraThu(App):
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex
    from kivy.core.text import LabelBase
    Window.clearcolor = get_color_from_hex('#4b5162')
    LabelBase.register(name='Roboto', fn_regular='fonts/Roboto-Thin.ttf',
                       fn_bold='fonts/Roboto-Medium.ttf')
KiemTraThu().run()


## This program is created by HuyNguyeen
## Facebook: facebook.com/HuyN.2105/
## Do not copy without permission
## Thank you for using this program
