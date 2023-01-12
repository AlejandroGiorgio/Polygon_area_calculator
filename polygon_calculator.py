class Rectangle:

  def __init__(self, width, height):
    self.width = int(width)
    self.height = int(height)

  def set_width(self, width):
    self.width = int(width)

  def set_height(self, height):
    self.height = int(height)

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_area(self):
    return self.width * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    linecount = 0
    picture = ""
    while linecount < self.height:
      for x in range(self.width):
        picture += "*"
      picture += "\n"
      linecount += 1
    return picture

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def get_amount_inside(self, obj):
    return (int(self.get_area() / obj.get_area()))


class Square(Rectangle):

  def __init__(self, side):
    self.width = int(side)
    self.height = int(side)

  def set_width(self, width):
    self.width = int(width)
    self.height = int(width)

  def set_height(self, height):
    self.height = int(height)
    self.width = int(height)

  def set_side(self, side):
    self.width = int(side)
    self.height = int(side)

  def __repr__(self):
    return f"Square(side={self.width})"