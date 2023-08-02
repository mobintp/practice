class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []
    
  def add_passenger(self, name):
    if not self.open_seats():
      print("capacity is full. ")
    else:
      self.passengers.append(name)
      print(f"{name} added. ")

    
  def open_seats(self):
    return self.capacity - len(self.passengers)
    
flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
  flight.add_passenger(person)