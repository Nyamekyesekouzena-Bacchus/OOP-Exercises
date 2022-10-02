#Write a program to print the area and perimeter of a triangle.


class triangle:
  def __init__(self, length:int, width:int, depth:int ):
    self.length = length
    self.width = width
    self.depth = depth

  def area(self):
    return 0.5* self.width * self.length

  def perimeter (self):
    return self.length + self.width + self.depth

  def display (self):
    print(f"Length: {self.length}, Width: {self.width}, Depth: {self.depth}, Area: {self.area()}, Perimeter: {self.perimeter()}")


item1 = triangle(2,4,4)
print(item1.area())
print(item1.perimeter())
item1.display()
