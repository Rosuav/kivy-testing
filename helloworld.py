from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class HelloApp(App):
	def __init__(self):
		self.hitcount = 0
		super().__init__()
		Clock.schedule_interval(self.waiting, 15)

	def build(self):
		return Label(text="Hit me.")

	def on_touch_down(self, touch):
		if not self.collide_point(*touch.pos): return
		if self.hitcount:
			self.hitcount += 1
			msg = "You've hit me %d times." % self.hitcount
		else:
			self.hitcount = 1
			msg = "Hit me again!"
		self.root.text = msg

	def waiting(self, delay):
		self.root.text = "Go on, hit me!"

if __name__ == "__main__":
	HelloApp().run()
