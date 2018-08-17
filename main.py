from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from suduko import *

class ramu(GridLayout):
    def __init__(self, **kwargs):
        super(ramu, self).__init__(**kwargs)
        global p,k,t
        p=[]
        k=[]
        for i in range(0,9):
              if (i%3==0):
                   self.add_widget(Label(size_hint=(1,0.03)))
              p.append(BoxLayout(size_hint=(1,0.5)))
              for j in range(0,9):
                    if ((j%2==0) & (i%2==0)):
                        k.append(TextInput(text=' ',font_size=80,background_color=(0.5,0.5,0.5,1),
			multiline=False))
                    elif ((j%2!=0) & (i%2!=0)):
                         k.append(TextInput(text=' ',font_size=80,background_color=(0.5,0.5,0.5,1),multiline=False))
                    else:
                        k.append(TextInput(text=' ',font_size=80,background_color=(0.6,0.2,0.2,1),multiline=False))
                    if (j%3==0):
                         p[i].add_widget(Label(size_hint=(0.05,1)))
                    p[i].add_widget(k[i*9+j])
              p[i].add_widget(Label(size_hint=(0.05,1)))
              self.add_widget(p[i])
        self.add_widget(Label(size_hint=(1,0.03)))
        ok=Button(on_press=lambda a:self.dare(),text='ok',background_color=(0.2,0.8,1,1.5))
        t=BoxLayout(spacing=5)
        t1=BoxLayout(padding=10,size_hint=(1,1.5))
        t1.add_widget(ok)
        set=Button(text='reset',on_press=lambda a:self.clean(),background_color=(0.2,0.8,1,1.5))
        set1=Button(text='undo',on_press=lambda a:self.undo(),background_color=(0.2,0.8,1,1.5))
        t.add_widget(set)
        t.add_widget(set1)
        self.add_widget(t1)
        self.add_widget(t)
        
        
    def dare(self):
        global k
        global y
        a=[]
        n=[]
        try:
             for i in range(0,81):
                   if ((k[i].text==' ' ) | (k[i].text=='')):
                        a.append(0)
                   else:
                        a.append(int(k[i].text))
             y.append(a)
             a=due(a)
             for i in range(0,81):
                   k[i].text=' '+str(a[i])
             self.su.text='[b]suduko-solver[/b] the answer of suduko is'
        except Exception:
             error().open()
             
             
    def clean(self):
        for i in range(0,81):
              k[i].text=' '  
        self.su.text= '[b]suduko-solver[/b] Press ok to Get the answer for suduko'
        
        
    def undo(self):
        global y
        m=y[0]
        for i in range(0,81):
              k[i].text=str(m[i])
              self.su.text= '[b]suduko-solver[/b] Press ok to Get the answer for suduko'
              
class error(Popup):
      pass
      
class datta(App):
      global y
      y=[]
      def build(self):
             return ramu()
      def on_pause(self):
             return True

datta().run()