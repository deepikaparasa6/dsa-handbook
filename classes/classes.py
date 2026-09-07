class Cookie:
    def __init__(self,color): 
        self.color = color 
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color
Cookie_one = Cookie('green')
Cookie_two = Cookie('blue')
print("Cookie one color: ",Cookie_one.get_color()) #output: Cookie one color:  green
print("Cookie two color: ",Cookie_two.get_color()) #output: Cookie two color:  blue
Cookie_one.set_color('red')
print("Cookie one color: ",Cookie_one.get_color()) #output: Cookie one color:  red
