class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return 0
    
    def get_perimeter(self):
        return 0
    
    def get_diagonal(self):
        return 0
    
    def get_picture(self):
        return 0
    
    def get_amount_inside(self):
        return 0
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
