# by Kami Bigdely
# Extract superclass.

class Shape:
    def __init__(self, x, y, visibility = True):
        self.x = x
        self.y = y
        self.visibility = visibility

    def display(self):
        if self.visibility:
            print("drawing shape at: ", self.x, self.y)

    def set_visibility(self, visibility):
        self.visibility = visibility


class Circle(Shape):
    
    def __init__(self, x, y, r, visible = True):
        super().__init__(x, y, visible)
        self.r = r
              
    def set_visible(self,is_visible):
        self.visible = is_visible
        
    def get_center(self):
        return self.x, self.y
    
    
class Rectangle(Shape):
    
    def __init__(self, x, y, width, height, visible = True):
        # left-bottom corner.
        super().__init__(x, y, visible)
        self.width = width
        self.height = height
                    
    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 



if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visibility()(True)
    circle.display()
    print('center point', circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.set_visibility(False)
    rect.display() # does not display because it's hidden.
    rect.set_visibility(True)
    rect.display()
    print('center point',rect.get_center())