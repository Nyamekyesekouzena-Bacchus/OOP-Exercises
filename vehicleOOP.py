"""Create a vehicle that comprises different parts that can be selected to be added to the vehicle. 
Each vehicle has its own serial number and name. Each vehicle can only have up to three wheels. 
For all parts, keep a note of the type of part, its serial number and an age of the part. For wheels, store their diameter and material. 
For normal parts, they can be determined to be old if they are over two years old. For wheels, if the wheel is above 1m in diameter, it is old after a year, otherwise it is old after three years."""
class part:
  def __init__ (self, type: str, serialNum: int, age: int):
    assert type != "", "type cannot be null"
    self.type =type;
    self.serialNum = serialNum;
    self.age = age;

  def isOld(self):
    return self.age>2

  def display(self):
    print(f"type: {self.type}, Serial Number: {self.serialNum}, Age:{self.age} ")

#Sub class of the part class 
class wheel(part):
  def __init__(self, diameter: float, material: str):
    self.diameter = diameter
    self.material= material

  def isOld(self):
    if self.diameter > 1:
      return 1
      #print("Wheel is old after one year")
    else:
      return 3
      #print("Wheel is old after three year")

  #Overrides parrent function 
  def display(self):
    print(f" Diameter: {self.diameter}, Years: {self.isOld()}, Material: {self.material},  ")
  
 

class vehicle:
  def __init__(self, serialNum:int, name: str, wheels: wheel, parts: part): 
    assert len(wheels)<=3, "the vechicle must have 3 or less wheels"
  
    self.name= name
    self.serialNum = serialNum
    self.wheels=wheels
    self.parts=parts

  def display(self):
    print(f"Serial Number: {self.serialNum}, name: {self.name} ")
    print("Wheels:")
    for wheel in self.wheels:
      wheel.display()
    print("Parts:")
    for part in self.parts:
      part.display()
      

#Fucntion to run everything; this does not need to be in function form  
def run():
  wheels=[]
  wheels.append(wheel(3, "rubber"))
  wheels.append(wheel(1, "rubber"))
  parts= []
  parts.append(part("engine", 1, 2))
  parts.append (part("handlebar", 2, 1))
  parts.append(part("seat", 2, 2))
  parts.append(part("breaks", 4, 11))
  parts.append(part("Gastank", 6, 2))
  parts.append(part("Breaks", 9, 2))
  parts.append(part("Headligths", 1, 1))
  parts.append(part("Speedmeter", 5, 2))

  #Create Vehicle object
  test =vehicle(123, "Motor Cycle", wheels, parts)
  test.display()

run()
  
  
  
