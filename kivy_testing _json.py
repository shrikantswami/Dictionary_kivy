from kivy.app import App
import json
from difflib import get_close_matches
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from functools import partial
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

kv ='''
<Screen>:
    
    result:resultsLabel
    function:findButton
    input:inputText
    add:addButton
    BoxLayout:
        orientation: 'vertical'
        Button:
            id:addButton
            text:'Add'
            size_hint:0.5,0.2
            on_press:app.add()

        Button:
            id:findButton
            text:'Search'
            size_hint:0.5,0.2
            #pos:200,200
            on_press:app.find()
       
        TextInput:
            id:inputText
            text:''
            font_size:20
            size_hint:0.5,0.2
            #pos:300,300
    Label:
        id:resultsLabel
        text_size: self.size
        text:'Answer will be Here'
        font_size:20
        #size_hint:0.5,0.2
        halign:'left'
        valign:'middle'
        
'''

class Test(App):
    def build(self):
        Builder.load_string(kv)
        return Screen()
    def find(self):
        data = json.load(open('data.json'))
        word=str.lower(self.root.input.text)
        if word in data :
            self.root.result.text = str(data[word])
        elif len(get_close_matches(word,data.keys())) > 0 :
            self.root.result.text = str("did you mean %s" % get_close_matches(word, data.keys())[0])
        else :
            self.root.result.text = "Not Found"
  
    
    def add(self):
        add=str(self.root.input.text)
        #while add !="" :
        with open("a.txt","a")as x:
            #word=input("enter word:")
            #mn=input("Meaning:")
            #x.write(str(word+":"+mn+"\n"))
            x.write(add+"\n")
            self.root.result.text="Word Added Succesfully"
            #add=input("Do you want to add another word(yes/no):")
                            
    
class Screen(BoxLayout):
    result = ObjectProperty(None)
    function = ObjectProperty(None)
    

if __name__=='__main__' :
    Test().run()
