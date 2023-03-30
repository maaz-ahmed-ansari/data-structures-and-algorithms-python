# Defining Class
class Cookie:
    # this is constructor
    # self indicates that it is method
    def __init__(self, color):  
        self.color = color

    def get_color(self):
        return self.color
    
    # when calling this method, it needs one argument 
    # which will be passed to "color"
    def set_color(self, color):
        self.color = color

# creating objects
cookie_one = Cookie('green')
cookie_two = Cookie('blue')
# calling get_colo methods
print('cookie one is:', cookie_one.get_color())
print('cookie two is:', cookie_two.get_color())
# calling set_color method
cookie_two.set_color('yellow')

print('\ncookie one is still:', cookie_one.get_color())
print('But cookie two is now:', cookie_two.get_color())

