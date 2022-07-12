
class Bird:
 def __init__(self):
	 self.hungry=True
 def eat(self):
    if self.hungry:
       print('Aaaah ...')
       self.hungry = False
    else:
       print('No, thanks!')

print("-------------------------------")

class SongBird(Bird):
	def __init__(self):
		super().__init__()
		self.sound="hiiiiii"
        
print("-----------------")

b=Bird()
b.eat()
b.eat()

print("-----------------")
sb = SongBird()
print(sb.sound)
sb.eat()
sb.eat()




