class Cookie: #this is class
    def __init__(self,color): #this is constructor method
        self.color = color 
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color
Cookie_one = Cookie('green') #cookie_one is an object of class Cookie and calliing constructor method
Cookie_two = Cookie('blue')
print("Cookie one color: ",Cookie_one.get_color()) #output: Cookie one color:  green
print("Cookie two color: ",Cookie_two.get_color()) #output: Cookie two color:  blue
Cookie_one.set_color('red')
print("Cookie one color: ",Cookie_one.get_color()) #output: Cookie one color:  red
