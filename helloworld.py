from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class HelloApp(App):
	def __init__(self):
		self.hitcount = 0
		super().__init__()
		Clock.schedule_once(self.waiting, 15)

	def build(self):
		self.btn = Button(text="Hit me.")
		self.btn.bind(on_press=self.on_click)
		return self.btn

	def on_click(self, btn):
		if self.hitcount:
			self.hitcount += 1
			msg = "You've hit me %d times." % self.hitcount
		else:
			self.hitcount = 1
			msg = "Hit me again!"
		self.btn.text = msg

	def waiting(self, delay):
		self.btn.text = "Go on, hit me!"

if __name__ == "__main__":
	HelloApp().run()
