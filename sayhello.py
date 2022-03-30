from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window


class SayHelloApp(App):
    def build(self):
        Window.clearcolor='#006633'
        
        self.window=GridLayout()
        self.window.color=(255,255,255,255)
        # self.window.canvas='#00ffce'
        self.window.cols=1
        self.window.background='#00ffce'
        self.window.size_hint=(0.6,0.7)
        self.window.pos_hint={'center_x':0.5, 'center_y':0.5}
        self.window.add_widget(Image(source='hello.png'))
        self.greet=Label(text="What's your Name",
        font_size=18,color='#00FFCE')
        self.window.add_widget(self.greet)
        self.inp=TextInput(multiline=False,padding_y=(20,20),padding_x=(20,20),size_hint=(1,0.5))
        self.window.add_widget(self.inp)
        self.enter=Button(text='Greet',size_hint=(.7,.5),bold=True,background_color='#00ffce')
        self.enter.bind(on_press=self.callback)
        self.window.add_widget(self.enter)
       
        
        
        
        
        


        return self.window

    def callback(self,event):
        if self.inp.text=='':
            self.greet.text=self.greet.text
        else:
       
            self.greet.text='Hello '+self.inp.text +' !'
            
       
        
        



if __name__=='__main__':
    SayHelloApp().run()
