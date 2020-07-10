import kivy
from kivymd.button import MDRaisedButton
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang import Builder
import os

Window.clearcolor = (1, 1, 199 / 255, 1)
Builder.load_string("""
#:import utils kivy.utils
#:import Factory kivy.factory.Factory

<HomeScreen>:
    padding:10
    spacing:10

    FloatLayout:


        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Start Prayer"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1            

        Button:
            text: "Rosary"
            pos_hint: {'x': .35, 'y': .6}
            size_hint: .3, .1
            on_press: root.manager.current = "iblv"
            background_color: 0/255, 0/255, 255/255,1

        Button:
            text: "Divine Mercy"
            pos_hint: {'x': .35, 'y': .45}
            size_hint: .3, .1
            on_press: root.manager.current = "dvour"
            background_color: 0/255, 0/255, 255/255,1



        Button:
            text: "Mystery days"
            pos_hint: {'x': .02, 'y': .03}
            size_hint: .3, .1
            background_color: 0/255, 0/255, 255/255,1
            on_release: Factory.MiPopup().open()

        Button:
            background_color: 0/255, 0/255, 255/255,1
            text: "About"
            pos_hint: {'x': .68, 'y': .03}
            size_hint: .3, .1
            on_release: Factory.MyPopup().open()


<IblvScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '30sp'
            text: "Apostles’ Creed"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 20, 10, 
            font_size: '13sp'
            halign: 'center'
            valign: 'center'       
            text: "In the name of the Father of the Son and of the Holy Spirit. Amen \\n \\n I believe in God the Father Almighty, Creator of heaven and earth; and in Jesus Christ, His only Son, our Lord; Who was conceived by the Holy Ghost, born of the Virgin Mary, suffered under Pontius Pilate, was crucified, died and was buried. He descended into hell. On the third day He arose again; He ascended into heaven,and sitteth at the right hand of God, the Father Almighty; from thence He shall come to judge the living and the dead. I believe in the Holy Ghost, the Holy Catholic Church, the communion of saints, the forgivness of sins, the resurrection of the body, and life everlasting. Amen "
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .1}
                size_hint: .3, .1
                on_press: root.manager.current = "rour"
<OurdadRScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Our Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Our Father, who art in heaven, hallowed be Thy name: Thy kingdom come: Thy will be done on earth as it is in heaven. Give us this day our daily bread: and forgive us our trespasses as we forgive those who trespass against us. And lead us not into temptation: but deliver us from evil. Amen."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "rone"                
<HailRoneScreen>:

    FloatLayout:

        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "rtwo"
<HailRtwoScreen>:
    FloatLayout:
        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "rthree"                
<HailRthreeScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "rgloryb"   
<GlorybRScreen>:
    FloatLayout:
        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Glory Be"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Glory be to the Father, and to the Son and to the Holy Spirit.As it was in the beginning, is now and ever shall be, world without end. Amen.\\n\\n O my Jesus, forgive us our sins, save us from the fires of hell, and lead all souls to Heaven, especially those in most need of Your Mercy"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "am"                

<MysteriesAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Mysteries"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "First joyful-The Annunciation\\nFirst Sorrowful-The Agony in the Garden\\nFirst Glorious-The Resurrection\\nFirst Luminous-The Baptism of Jesus in the Jordan"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.25
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "aour"    
<OurdadAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Our Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Our Father, who art in heaven, hallowed be Thy name: Thy kingdom come: Thy will be done on earth as it is in heaven. Give us this day our daily bread: and forgive us our trespasses as we forgive those who trespass against us. And lead us not into temptation: but deliver us from evil. Amen."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "aone"                                  

<HailoneAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "atwo"                

<HailtwoAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "athree"
<HailthreeAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "afour"                
<HailfourAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "afive"  
<HailfiveAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "asix" 
<HailsixAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "aseven"
<HailsevenAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "aeight"
<HaileightAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "anine"
<HailnineAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "aten"
<HailtenAScreen>:
    FloatLayout:
        cols:1   
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "agloryb"
<GlorybAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Glory Be"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Glory be to the Father, and to the Son and to the Holy Spirit.As it was in the beginning, is now and ever shall be, world without end. Amen.\\n\\n O my Jesus, forgive us our sins, save us from the fires of hell, and lead all souls to Heaven, especially those in most need of Your Mercy"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bm"

<MysteriesBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Mysteries"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Second joyful-The Visitation\\nSecond Sorrowful-The Scourging at the Pillar\\nSecond Glorious-The Ascension\\nSecond Luminous-The Wedding at Cana"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bour"  
<OurdadBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Our Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Our Father, who art in heaven, hallowed be Thy name: Thy kingdom come: Thy will be done on earth as it is in heaven. Give us this day our daily bread: and forgive us our trespasses as we forgive those who trespass against us. And lead us not into temptation: but deliver us from evil. Amen."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bone"                               

<HailoneBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "btwo"                

<HailtwoBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bthree"
<HailthreeBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bfour"                
<HailfourBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bfive"  
<HailfiveBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bsix" 
<HailsixBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bseven"
<HailsevenBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "beight"
<HaileightBScreen>:
    FloatLayout:
        cols:1   
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bnine"
<HailnineBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bten"
<HailtenBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bgloryb"
<GlorybBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Glory Be"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Glory be to the Father, and to the Son and to the Holy Spirit.As it was in the beginning, is now and ever shall be, world without end. Amen.\\n\\n O my Jesus, forgive us our sins, save us from the fires of hell, and lead all souls to Heaven, especially those in most need of Your Mercy"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cm"                





<MysteriesCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Mysteries"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Third joyful-The Nativity\\nThird Sorrowful-The Crowning with Thorns\\nThird Glorious-The Descent of the Holy Spirit\\nThird Luminous-Jesus' Proclamation of the Kingdom of God"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cour"                
<OurdadCScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Our Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Our Father, who art in heaven, hallowed be Thy name: Thy kingdom come: Thy will be done on earth as it is in heaven. Give us this day our daily bread: and forgive us our trespasses as we forgive those who trespass against us. And lead us not into temptation: but deliver us from evil. Amen."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cone"                                                                                       
<HailoneCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "ctwo"                

<HailtwoCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cthree"
<HailthreeCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cfour"                
<HailfourCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cfive"  
<HailfiveCScreen>:
    FloatLayout:
        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "csix" 
<HailsixCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cseven"
<HailsevenCScreen>:
    FloatLayout:
        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "ceight"
<HaileightCScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cnine"
<HailnineCScreen>:
    FloatLayout:
        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cten"
<HailtenCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cgloryb"
<GlorybCScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Glory Be"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Glory be to the Father, and to the Son and to the Holy Spirit.As it was in the beginning, is now and ever shall be, world without end. Amen.\\n\\n O my Jesus, forgive us our sins, save us from the fires of hell, and lead all souls to Heaven, especially those in most need of Your Mercy"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dm"





<MysteriesDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Mysteries"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Fourth joyful-The Presentation of Jesus at the Temple\\nFourth Sorrowful-The Carrying of the Cross\\nFourth Glorious-The Assumption of Mary\\nFourth Luminous-The Transfiguration"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dour"  
<OurdadDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Our Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Our Father, who art in heaven, hallowed be Thy name: Thy kingdom come: Thy will be done on earth as it is in heaven. Give us this day our daily bread: and forgive us our trespasses as we forgive those who trespass against us. And lead us not into temptation: but deliver us from evil. Amen."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "done"                               

<HailoneDScreen>:
    FloatLayout:
        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dtwo"                

<HailtwoDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dthree"
<HailthreeDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dfour"                
<HailfourDScreen>:
    FloatLayout:
        cols:1   
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dfive"  
<HailfiveDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dsix" 
<HailsixDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dseven"
<HailsevenDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "deight"
<HaileightDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dnine"
<HailnineDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dten"
<HailtenDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dgloryb"
<GlorybDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Glory Be"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Glory be to the Father, and to the Son and to the Holy Spirit.As it was in the beginning, is now and ever shall be, world without end. Amen.\\n\\n O my Jesus, forgive us our sins, save us from the fires of hell, and lead all souls to Heaven, especially those in most need of Your Mercy"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "em"




<MysteriesEScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Mysteries"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Fifth joyful-The Finding of Jesus in the Temple\\nFifth Sorrowful-The Crucifixion and Death of our Lord\\nFifth Glorious-The Coronation of the Virgin\\nFifth Luminous-The Institution of the Eucharist"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "eour"  
<OurdadEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Our Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Our Father, who art in heaven, hallowed be Thy name: Thy kingdom come: Thy will be done on earth as it is in heaven. Give us this day our daily bread: and forgive us our trespasses as we forgive those who trespass against us. And lead us not into temptation: but deliver us from evil. Amen."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "eone"                               

<HailoneEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "etwo"                

<HailtwoEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "ethree"
<HailthreeEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "efour"                
<HailfourEScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "efive"  
<HailfiveEScreen>:
    FloatLayout:
        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "esix" 
<HailsixEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "eseven"
<HailsevenEScreen>:
    FloatLayout:
        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen" 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "eeight"
<HaileightEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "enine"
<HailnineEScreen>:
    FloatLayout:
        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "eten"
<HailtenEScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "egloryb"
<GlorybEScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Glory Be"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Glory be to the Father, and to the Son and to the Holy Spirit.As it was in the beginning, is now and ever shall be, world without end. Amen.\\n\\n O my Jesus, forgive us our sins, save us from the fires of hell, and lead all souls to Heaven, especially those in most need of Your Mercy"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "holy" 




<HolyScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '30sp'
            text: "Hail Holy Queen"
            pos_hint: {'x': .35, 'y': .85}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail, holy Queen, Mother of Mercy! our life, our sweetness, and our hope! To thee do we cry, poor banished children of Eve; to thee do we send up our sighs, mourning and weeping in this valley, of tears. Turn, then, most gracious Advocate, thine eyes of mercy toward us; and after this our exile show unto us the blessed fruit of thy womb, Jesus; O clement, O loving, O sweet Virgin Mary."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.1
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "fly"
<FlyScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Let Us Pray"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "O God whose only begotten Son by His Life has purchased for us the rewards of eternal life, Grant that we beseech Thee while meditating upon these mysteries of the Most Holy Rosary of the Blessed Virgin Mary, we may both imitate what they contain and obtain what they promise, through the same Christ our Lord Amen."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "end"                                                                                                                               

<EndScreen>:
    FloatLayout:
        cols:1       
        Label:     
            padding: 50, 10
            font_size: '40sp'
            halign: 'center'
            valign: 'center'       
            text: "In the name of the Father of the Son and of the Holy Spirit. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "END"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "home"  






<OurdadDivScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Our Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Our Father, who art in heaven, hallowed be Thy name: Thy kingdom come: Thy will be done on earth as it is in heaven. Give us this day our daily bread: and forgive us our trespasses as we forgive those who trespass against us. And lead us not into temptation: but deliver us from evil. Amen."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dvhail"                
<HailDivScreen>:
    FloatLayout:

        cols:1
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Hail Mary"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Hail Mary, full of grace, the Lord is with thee: blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dviblv"
<IblvDivScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '30sp'
            text: "Apostles’ Creed"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1         
        Label:     
            padding: 20, 10, 
            font_size: '13sp'
            halign: 'center'
            valign: 'center'       
            text: "I believe in God the Father Almighty, Creator of heaven and earth; and in Jesus Christ, His only Son, our Lord; Who was conceived by the Holy Ghost, born of the Virgin Mary, suffered under Pontius Pilate, was crucified, died and was buried. He descended into hell. On the third day He arose again; He ascended into heaven,and sitteth at the right hand of God, the Father Almighty; from thence He shall come to judge the living and the dead. I believe in the Holy Ghost, the Holy Catholic Church, the communion of saints, the forgivness of sins, the resurrection of the body, and life everlasting. Amen "
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .1}
                size_hint: .3, .1
                on_press: root.manager.current = "aef"                


<EternalFAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Eternal Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Eternal Father, I offer you the Body and Blood, Soul and Divinity of Your Dearly Beloved Son, Our Lord, Jesus Christ, in atonement for our sins and those of the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.25
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "afone"                                     

<FtsoneAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "aftwo"                

<FtstwoAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "afthree"
<FtsthreeAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "affour"                
<FtsfourAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "affive"  
<FtsfiveAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "afsix" 
<FtssixAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "afseven"
<FtssevenAScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "afeight"
<FtseightAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "afnine"
<FtsnineAScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "aften"
<FtstenAScreen>:
    FloatLayout:
        cols:1   
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bef"



<EternalFBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Eternal Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Eternal Father, I offer you the Body and Blood, Soul and Divinity of Your Dearly Beloved Son, Our Lord, Jesus Christ, in atonement for our sins and those of the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.25
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bfone"                                     

<FtsoneBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bftwo"                

<FtstwoBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bfthree"
<FtsthreeBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bffour"                
<FtsfourBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bffive"  
<FtsfiveBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bfsix" 
<FtssixBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bfseven"
<FtssevenBScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bfeight"
<FtseightBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bfnine"
<FtsnineBScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "bften"
<FtstenBScreen>:
    FloatLayout:
        cols:1   
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cef"



<EternalFCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Eternal Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Eternal Father, I offer you the Body and Blood, Soul and Divinity of Your Dearly Beloved Son, Our Lord, Jesus Christ, in atonement for our sins and those of the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.25
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cfone"                                     

<FtsoneCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cftwo"                

<FtstwoCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cfthree"
<FtsthreeCScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cffour"                
<FtsfourCScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cffive"  
<FtsfiveCScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cfsix" 
<FtssixCScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cfseven"
<FtssevenCScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cfeight"
<FtseightCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cfnine"
<FtsnineCScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "cften"
<FtstenCScreen>:
    FloatLayout:
        cols:1   
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "def"


<EternalFDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Eternal Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Eternal Father, I offer you the Body and Blood, Soul and Divinity of Your Dearly Beloved Son, Our Lord, Jesus Christ, in atonement for our sins and those of the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.25
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dfone"                                     

<FtsoneDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dftwo"                

<FtstwoDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dfthree"
<FtsthreeDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dffour"                
<FtsfourDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dffive"  
<FtsfiveDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dfsix" 
<FtssixDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dfseven"
<FtssevenDScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dfeight"
<FtseightDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dfnine"
<FtsnineDScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "dften"
<FtstenDScreen>:
    FloatLayout:
        cols:1   
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "eef"


<EternalFEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "Eternal Father"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Eternal Father, I offer you the Body and Blood, Soul and Divinity of Your Dearly Beloved Son, Our Lord, Jesus Christ, in atonement for our sins and those of the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.25
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "efone"                                     

<FtsoneEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "1"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "eftwo"                

<FtstwoEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "2"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "efthree"
<FtsthreeEScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "3"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "effour"                
<FtsfourEScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "4"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "effive"  
<FtsfiveEScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "5"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "efsix" 
<FtssixEScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "6"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "efseven"
<FtssevenEScreen>:
    FloatLayout:
        cols:1  
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "7"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1       
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'      
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world." 
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "efeight"
<FtseightEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "8"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'     
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."  
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "efnine"
<FtsnineEScreen>:
    FloatLayout:
        cols:1 
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "9"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1        
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "eften"
<FtstenEScreen>:
    FloatLayout:
        cols:1   
        Label:
            color: 209, .46, .7,1
            font_size: '50sp'
            text: "10"
            pos_hint: {'x': .35, 'y': .80}
            size_hint: .3, .1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "For the sake of His sorrowful Passion, have mercy on us and on the whole world."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "hg"

<HolyGScreen>:
    FloatLayout:
        cols:1      
        Label:     
            padding: 50, 10
            halign: 'center'
            valign: 'center'       
            text: "Holy God, Holy Mighty One, Holy Immortal One, have mercy on us and on the whole world.(x3)"
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.2
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "Next"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "eg"                                                                                                                               

<EternalGScreen>:
    FloatLayout:
        cols:1       
        Label:     
            padding: 50, 10
            font_size: '25sp'
            halign: 'center'
            valign: 'center'       
            text: "Eternal God, in whom mercy is endless and the treasury of compassion — inexhaustible, look kindly upon us and increase Your mercy in us, that in difficult moments we might not despair nor become despondent, but with great confidence submit ourselves to Your holy will, which is Love and Mercy itself."
            text_size: self.size
            size: self.texture_size
            size_hint: 1, 1.4
            color: 209, .46, .7,1
        FloatLayout:    
            Button:
                background_color: 0/255, 0/255, 255/255,1
                text: "END"
                pos_hint: {'x': .35, 'y': .2}
                size_hint: .3, .1
                on_press: root.manager.current = "home"  




<MyPopup@Popup>:
    size_hint: .8, .8
    title: 'About'
    auto_dismiss: False
    Button:
        halign: 'center'
        valign: 'center'
        font_size: '30sp'
        text: 'This App was developed by\\n Chijindu Ikenna Nnamani'
        text_size: self.size
        on_release: root.dismiss()


<MiPopup@Popup>:
    size_hint: .8, .8
    title: 'Days for the Mysteries'
    auto_dismiss: False
    Button:
        text: 'Mon-The Joyful Mysteries\\nTue-The Sorrowful Mysteries\\nWed-The Glorious Mysteries\\nThur-The Luminous Mysteries\\nFri-The Sorrowful Mysteries \\nSat-The Joyful Mysteries\\nSun in Advent-The Joyful Mysteries\\nin Lent-The Sorrowful Mysteries\\ninOrdinary time-The Glorious Mysteries'
        on_release: root.dismiss()



""")


class HomeScreen(Screen):
    pass


class IblvScreen(Screen):
    pass


class OurdadRScreen(Screen):
    pass


class HailRoneScreen(Screen):
    pass


class HailRtwoScreen(Screen):
    pass


class HailRthreeScreen(Screen):
    pass


class GlorybRScreen(Screen):
    pass


class MysteriesAScreen(Screen):
    pass


class OurdadAScreen(Screen):
    pass


class HailoneAScreen(Screen):
    pass


class HailtwoAScreen(Screen):
    pass


class HailthreeAScreen(Screen):
    pass


class HailfourAScreen(Screen):
    pass


class HailfiveAScreen(Screen):
    pass


class HailsixAScreen(Screen):
    pass


class HailsevenAScreen(Screen):
    pass


class HaileightAScreen(Screen):
    pass


class HailnineAScreen(Screen):
    pass


class HailtenAScreen(Screen):
    pass


class GlorybAScreen(Screen):
    pass


class MysteriesBScreen(Screen):
    pass


class OurdadBScreen(Screen):
    pass


class HailoneBScreen(Screen):
    pass


class HailtwoBScreen(Screen):
    pass


class HailthreeBScreen(Screen):
    pass


class HailfourBScreen(Screen):
    pass


class HailfiveBScreen(Screen):
    pass


class HailsixBScreen(Screen):
    pass


class HailsevenBScreen(Screen):
    pass


class HaileightBScreen(Screen):
    pass


class HailnineBScreen(Screen):
    pass


class HailtenBScreen(Screen):
    pass


class GlorybBScreen(Screen):
    pass


class MysteriesCScreen(Screen):
    pass


class OurdadCScreen(Screen):
    pass


class HailoneCScreen(Screen):
    pass


class HailtwoCScreen(Screen):
    pass


class HailthreeCScreen(Screen):
    pass


class HailfourCScreen(Screen):
    pass


class HailfiveCScreen(Screen):
    pass


class HailsixCScreen(Screen):
    pass


class HailsevenCScreen(Screen):
    pass


class HaileightCScreen(Screen):
    pass


class HailnineCScreen(Screen):
    pass


class HailtenCScreen(Screen):
    pass


class GlorybCScreen(Screen):
    pass


class MysteriesDScreen(Screen):
    pass


class OurdadDScreen(Screen):
    pass


class HailoneDScreen(Screen):
    pass


class HailtwoDScreen(Screen):
    pass


class HailthreeDScreen(Screen):
    pass


class HailfourDScreen(Screen):
    pass


class HailfiveDScreen(Screen):
    pass


class HailsixDScreen(Screen):
    pass


class HailsevenDScreen(Screen):
    pass


class HaileightDScreen(Screen):
    pass


class HailnineDScreen(Screen):
    pass


class HailtenDScreen(Screen):
    pass


class GlorybDScreen(Screen):
    pass


class MysteriesEScreen(Screen):
    pass


class OurdadEScreen(Screen):
    pass


class HailoneEScreen(Screen):
    pass


class HailtwoEScreen(Screen):
    pass


class HailthreeEScreen(Screen):
    pass


class HailfourEScreen(Screen):
    pass


class HailfiveEScreen(Screen):
    pass


class HailsixEScreen(Screen):
    pass


class HailsevenEScreen(Screen):
    pass


class HaileightEScreen(Screen):
    pass


class HailnineEScreen(Screen):
    pass


class HailtenEScreen(Screen):
    pass


class GlorybEScreen(Screen):
    pass


class HolyScreen(Screen):
    pass


class FlyScreen(Screen):
    pass


class EndScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class OurdadDivScreen(Screen):
    pass


class HailDivScreen(Screen):
    pass


class IblvDivScreen(Screen):
    pass


class EternalFAScreen(Screen):
    pass


class FtsoneAScreen(Screen):
    pass


class FtstwoAScreen(Screen):
    pass


class FtsthreeAScreen(Screen):
    pass


class FtsfourAScreen(Screen):
    pass


class FtsfiveAScreen(Screen):
    pass


class FtssixAScreen(Screen):
    pass


class FtssevenAScreen(Screen):
    pass


class FtseightAScreen(Screen):
    pass


class FtsnineAScreen(Screen):
    pass


class FtstenAScreen(Screen):
    pass


class EternalFBScreen(Screen):
    pass


class FtsoneBScreen(Screen):
    pass


class FtstwoBScreen(Screen):
    pass


class FtsthreeBScreen(Screen):
    pass


class FtsfourBScreen(Screen):
    pass


class FtsfiveBScreen(Screen):
    pass


class FtssixBScreen(Screen):
    pass


class FtssevenBScreen(Screen):
    pass


class FtseightBScreen(Screen):
    pass


class FtsnineBScreen(Screen):
    pass


class FtstenBScreen(Screen):
    pass


class EternalFCScreen(Screen):
    pass


class FtsoneCScreen(Screen):
    pass


class FtstwoCScreen(Screen):
    pass


class FtsthreeCScreen(Screen):
    pass


class FtsfourCScreen(Screen):
    pass


class FtsfiveCScreen(Screen):
    pass


class FtssixCScreen(Screen):
    pass


class FtssevenCScreen(Screen):
    pass


class FtseightCScreen(Screen):
    pass


class FtsnineCScreen(Screen):
    pass


class FtstenCScreen(Screen):
    pass


class EternalFDScreen(Screen):
    pass


class FtsoneDScreen(Screen):
    pass


class FtstwoDScreen(Screen):
    pass


class FtsthreeDScreen(Screen):
    pass


class FtsfourDScreen(Screen):
    pass


class FtsfiveDScreen(Screen):
    pass


class FtssixDScreen(Screen):
    pass


class FtssevenDScreen(Screen):
    pass


class FtseightDScreen(Screen):
    pass


class FtsnineDScreen(Screen):
    pass


class FtstenDScreen(Screen):
    pass


class EternalFEScreen(Screen):
    pass


class FtsoneEScreen(Screen):
    pass


class FtstwoEScreen(Screen):
    pass


class FtsthreeEScreen(Screen):
    pass


class FtsfourEScreen(Screen):
    pass


class FtsfiveEScreen(Screen):
    pass


class FtssixEScreen(Screen):
    pass


class FtssevenEScreen(Screen):
    pass


class FtseightEScreen(Screen):
    pass


class FtsnineEScreen(Screen):
    pass


class FtstenEScreen(Screen):
    pass


class HolyGScreen(Screen):
    pass


class EternalGScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(HomeScreen(name="home"))
sm.add_widget(OurdadDivScreen(name="dvour"))
sm.add_widget(HailDivScreen(name="dvhail"))
sm.add_widget(IblvDivScreen(name="dviblv"))

sm.add_widget(EternalFAScreen(name="aef"))
sm.add_widget(FtsoneAScreen(name="afone"))
sm.add_widget(FtstwoAScreen(name="aftwo"))
sm.add_widget(FtsthreeAScreen(name="afthree"))
sm.add_widget(FtsfourAScreen(name="affour"))
sm.add_widget(FtsfiveAScreen(name="affive"))
sm.add_widget(FtssixAScreen(name="afsix"))
sm.add_widget(FtssevenAScreen(name="afseven"))
sm.add_widget(FtseightAScreen(name="afeight"))
sm.add_widget(FtsnineAScreen(name="afnine"))
sm.add_widget(FtstenAScreen(name="aften"))

sm.add_widget(EternalFBScreen(name="bef"))
sm.add_widget(FtsoneBScreen(name="bfone"))
sm.add_widget(FtstwoBScreen(name="bftwo"))
sm.add_widget(FtsthreeBScreen(name="bfthree"))
sm.add_widget(FtsfourBScreen(name="bffour"))
sm.add_widget(FtsfiveBScreen(name="bffive"))
sm.add_widget(FtssixBScreen(name="bfsix"))
sm.add_widget(FtssevenBScreen(name="bfseven"))
sm.add_widget(FtseightBScreen(name="bfeight"))
sm.add_widget(FtsnineBScreen(name="bfnine"))
sm.add_widget(FtstenBScreen(name="bften"))

sm.add_widget(EternalFCScreen(name="cef"))
sm.add_widget(FtsoneCScreen(name="cfone"))
sm.add_widget(FtstwoCScreen(name="cftwo"))
sm.add_widget(FtsthreeCScreen(name="cfthree"))
sm.add_widget(FtsfourCScreen(name="cffour"))
sm.add_widget(FtsfiveCScreen(name="cffive"))
sm.add_widget(FtssixCScreen(name="cfsix"))
sm.add_widget(FtssevenCScreen(name="cfseven"))
sm.add_widget(FtseightCScreen(name="cfeight"))
sm.add_widget(FtsnineCScreen(name="cfnine"))
sm.add_widget(FtstenCScreen(name="cften"))

sm.add_widget(EternalFDScreen(name="def"))
sm.add_widget(FtsoneDScreen(name="dfone"))
sm.add_widget(FtstwoDScreen(name="dftwo"))
sm.add_widget(FtsthreeDScreen(name="dfthree"))
sm.add_widget(FtsfourDScreen(name="dffour"))
sm.add_widget(FtsfiveDScreen(name="dffive"))
sm.add_widget(FtssixDScreen(name="dfsix"))
sm.add_widget(FtssevenDScreen(name="dfseven"))
sm.add_widget(FtseightDScreen(name="dfeight"))
sm.add_widget(FtsnineDScreen(name="dfnine"))
sm.add_widget(FtstenDScreen(name="dften"))

sm.add_widget(EternalFEScreen(name="eef"))
sm.add_widget(FtsoneEScreen(name="efone"))
sm.add_widget(FtstwoEScreen(name="eftwo"))
sm.add_widget(FtsthreeEScreen(name="efthree"))
sm.add_widget(FtsfourEScreen(name="effour"))
sm.add_widget(FtsfiveEScreen(name="effive"))
sm.add_widget(FtssixEScreen(name="efsix"))
sm.add_widget(FtssevenEScreen(name="efseven"))
sm.add_widget(FtseightEScreen(name="efeight"))
sm.add_widget(FtsnineEScreen(name="efnine"))
sm.add_widget(FtstenEScreen(name="eften"))

sm.add_widget(HolyGScreen(name="hg"))
sm.add_widget(EternalGScreen(name="eg"))

sm.add_widget(HomeScreen(name="home"))
sm.add_widget(IblvScreen(name="iblv"))
sm.add_widget(OurdadRScreen(name="rour"))
sm.add_widget(HailRoneScreen(name="rone"))
sm.add_widget(HailRtwoScreen(name="rtwo"))
sm.add_widget(HailRthreeScreen(name="rthree"))
sm.add_widget(GlorybRScreen(name="rgloryb"))

sm.add_widget(MysteriesAScreen(name="am"))
sm.add_widget(OurdadAScreen(name="aour"))
sm.add_widget(HailoneAScreen(name="aone"))
sm.add_widget(HailtwoAScreen(name="atwo"))
sm.add_widget(HailthreeAScreen(name="athree"))
sm.add_widget(HailfourAScreen(name="afour"))
sm.add_widget(HailfiveAScreen(name="afive"))
sm.add_widget(HailsixAScreen(name="asix"))
sm.add_widget(HailsevenAScreen(name="aseven"))
sm.add_widget(HaileightAScreen(name="aeight"))
sm.add_widget(HailnineAScreen(name="anine"))
sm.add_widget(HailtenAScreen(name="aten"))
sm.add_widget(GlorybAScreen(name="agloryb"))

sm.add_widget(MysteriesBScreen(name="bm"))
sm.add_widget(OurdadBScreen(name="bour"))
sm.add_widget(HailoneBScreen(name="bone"))
sm.add_widget(HailtwoBScreen(name="btwo"))
sm.add_widget(HailthreeBScreen(name="bthree"))
sm.add_widget(HailfourBScreen(name="bfour"))
sm.add_widget(HailfiveBScreen(name="bfive"))
sm.add_widget(HailsixBScreen(name="bsix"))
sm.add_widget(HailsevenBScreen(name="bseven"))
sm.add_widget(HaileightBScreen(name="beight"))
sm.add_widget(HailnineBScreen(name="bnine"))
sm.add_widget(HailtenBScreen(name="bten"))
sm.add_widget(GlorybBScreen(name="bgloryb"))

sm.add_widget(MysteriesCScreen(name="cm"))
sm.add_widget(OurdadCScreen(name="cour"))
sm.add_widget(HailoneCScreen(name="cone"))
sm.add_widget(HailtwoCScreen(name="ctwo"))
sm.add_widget(HailthreeCScreen(name="cthree"))
sm.add_widget(HailfourCScreen(name="cfour"))
sm.add_widget(HailfiveCScreen(name="cfive"))
sm.add_widget(HailsixCScreen(name="csix"))
sm.add_widget(HailsevenCScreen(name="cseven"))
sm.add_widget(HaileightCScreen(name="ceight"))
sm.add_widget(HailnineCScreen(name="cnine"))
sm.add_widget(HailtenCScreen(name="cten"))
sm.add_widget(GlorybCScreen(name="cgloryb"))

sm.add_widget(MysteriesDScreen(name="dm"))
sm.add_widget(OurdadDScreen(name="dour"))
sm.add_widget(HailoneDScreen(name="done"))
sm.add_widget(HailtwoDScreen(name="dtwo"))
sm.add_widget(HailthreeDScreen(name="dthree"))
sm.add_widget(HailfourDScreen(name="dfour"))
sm.add_widget(HailfiveDScreen(name="dfive"))
sm.add_widget(HailsixDScreen(name="dsix"))
sm.add_widget(HailsevenDScreen(name="dseven"))
sm.add_widget(HaileightDScreen(name="deight"))
sm.add_widget(HailnineDScreen(name="dnine"))
sm.add_widget(HailtenDScreen(name="dten"))
sm.add_widget(GlorybDScreen(name="dgloryb"))

sm.add_widget(MysteriesEScreen(name="em"))
sm.add_widget(OurdadEScreen(name="eour"))
sm.add_widget(HailoneEScreen(name="eone"))
sm.add_widget(HailtwoEScreen(name="etwo"))
sm.add_widget(HailthreeEScreen(name="ethree"))
sm.add_widget(HailfourEScreen(name="efour"))
sm.add_widget(HailfiveEScreen(name="efive"))
sm.add_widget(HailsixEScreen(name="esix"))
sm.add_widget(HailsevenEScreen(name="eseven"))
sm.add_widget(HaileightEScreen(name="eeight"))
sm.add_widget(HailnineEScreen(name="enine"))
sm.add_widget(HailtenEScreen(name="eten"))
sm.add_widget(GlorybEScreen(name="egloryb"))

sm.add_widget(HolyScreen(name="holy"))
sm.add_widget(FlyScreen(name="fly"))
sm.add_widget(EndScreen(name="end"))


class ChapletApp(App):
    def build(self):
        return sm


ChapletApp().run()