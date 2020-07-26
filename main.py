# author - datta
# to do- error message when input is not number or greater than 9
# to-do- popup while loading
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

#from suduko import *

#header design
Builder.load_string("""
<grid_format>:
  rows:25
  id:ram
  title:title
  Label:
    font_size:30
    text: '[b]Garuda.inc[/b]'
    canvas.before:
      Color:
        rgb: 1,0,0
      Rectangle:
        pos:self.pos
        size:self.size 
    markup: True
    size_hint: (1,0.4)
  Button:
    font_size:30
    id: title
    text: '[b]suduko-solver[/b] Press ok to Get the answer for suduko'
    background_color: (0.2,0.8,1,1.7)
    markup: True
    size_hint: (1,0.4)
<error>:
  title:'error'
  size_hint:(.75,.4)
  Label:
    id:tex
    text:'only integers should be written'
  """)

# for suduko entry grid and other buttons
class grid_format(GridLayout):
    prev=[]
    pre_point=-1
    def __init__(self):
        super(grid_format, self).__init__()
        self.all_boxs=[]

        # creates the text input grid to enter suduko
        for row in range(9):
              row_box=BoxLayout(size_hint=(1,0.5))
              if (row%3==0):
                   self.add_widget(Label(size_hint=(1,0.03))) #black line to seperate 3 consecutive lines
              for col in range(0,9):
                    if (((col%2==0) & (row%2==0)) | ((col%2!=0) & (row%2!=0))):  #to have different colors
                        t=TextInput(text=' ',font_size=20,background_color=(0.5,0.5,0.5,1),multiline=False,input_type='number')
                        self.all_boxs.append(t) 
                    else:
                        self.all_boxs.append(TextInput(text=' ',font_size=20,background_color=(0.6,0.2,0.2,1),multiline=False,input_type='number'))
                    if (col%3==0):
                         row_box.add_widget(Label(size_hint=(0.05,1))) # to have black label sepeartor after 3 boxs
                    row_box.add_widget(self.all_boxs[row*9+col])
              row_box.add_widget(Label(size_hint=(0.05,1)))
              self.add_widget(row_box)
        self.add_widget(Label(size_hint=(1,0.03)))


        t.bind(size=self.inp_siz)

        ok=Button(on_press=lambda a:self.ok(self.all_boxs),text='ok',background_color=(0.2,0.8,1,1.5))
        box1=BoxLayout(padding=10,size_hint=(1,1.5)) # to have padding and spacing for the button
        box1.add_widget(ok)
        self.add_widget(box1)

        reset=Button(text='reset',on_press=lambda a:self.clean(self.all_boxs),background_color=(0.2,0.8,1,1.5))
        undo=Button(text='undo',on_press=lambda a:self.undo(self.all_boxs),background_color=(0.2,0.8,1,1.5))
        box2=BoxLayout(spacing=5) # to have padding and spacing for the button
        box2.add_widget(reset)
        box2.add_widget(undo)
        self.add_widget(box2)

    #for the change in input size accordingly
    def inp_siz(self,a,siz):
        print(siz)
        for i in self.all_boxs:
          i.font_size=siz[1]/1.5

    #converts box to int and final to the list
    def boxs2int(self,all_boxs):  
        a=[]  
        for i in all_boxs:
             try:
                   a.append(int(i.text))
             except Exception as e:
                   if (i.text!=' '):
                      error('enter only integers').open()
                      return 0
                   a.append(0)
        self.prev.append(a[:]) 
        self.pre_point+=1
        return a

        
    def ok(self,all_boxs):
        a=self.boxs2int(all_boxs)
        if (a==0):
          return
        try:
             a=suduko(a).due()
             for i in range(0,81):
                   all_boxs[i].text=' '+str(a[i])
                   all_boxs[i].foreground_color=(0,0,0,1)
             m=self.prev[self.pre_point]
             for i in range(0,81):
                   if (m[i]!=0):
                    all_boxs[i].foreground_color=(1,1,1,1)
                    all_boxs[i].text=' '+str(m[i])
             self.title.text='[b]suduko-solver[/b] the answer of suduko is'
        except Exception as e:
             print(str(e))
             error(str(e)).open()
             
             
    def clean(self,all_boxs):
        a=self.boxs2int(all_boxs)
        for i in all_boxs:
              i.text=' ' 
              i.foreground_color=(0,0,0,1)
        self.title.text= '[b]suduko-solver[/b] Press ok to Get the answer for suduko'
        
        
    def undo(self,k):
        if (self.pre_point==-1):
              self.clean(k)
              m=self.prev[self.pre_point]
              self.prev.remove(m)
              self.pre_point-=1
              return
        m=self.prev[self.pre_point]
        self.prev.remove(m)
        self.pre_point-=1
        for i in range(0,81):
              k[i].foreground_color=(0,0,0,1)
              if (m[i]==0):
                   k[i].text=' '
              else:
                   k[i].text=' '+str(m[i])
        self.title.text= '[b]suduko-solver[/b] Press ok to Get the answer for suduko'


# to solve suduko
class suduko():
      def __init__(self,p):
          self.a=p
      def construct(self,i):
          if (self.a[i]==0):
              for t in range(1,10):
                  if (self.check(t,i) & self.check1(t,i)):
                      self.a[i]=t
                      if (i==80):
                          return True
                      p=i+1
                      if (self.construct(p)):
                          return True
              self.a[i]=0
              return False
          elif (i==80):
              return True
          else:
              p=i+1
              return self.construct(p)
      def check(self,t,i):
          for j in range(0,9):
              if (self.a[(i//9)*9+j]==t):
                  return False
              if (self.a[(9*j)+(i%9)]==t):
                  return False
          return True
      def check1(self,t,i):
          col=((i//9)//3)*3
          row=(((i)%9)//3)
          for l in range(0,3):
              for m in range(0,3):
                  if (self.a[9*(col+l)+((3*row)+m)]==t):
                      return False
          return True
      def due(self):
          self.construct(0)
          return self.a


class error(Popup):
      def __init__(self,text):
        super(error,self).__init__()
        self.ids.tex.text=text
      
class datta(App):
      def build(self):
             return grid_format()
      def on_pause(self):
             return True

datta().run()
