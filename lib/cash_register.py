#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last = {}


  def get_discount(self):
    return self._discount

  def set_discount(self, discount):
    self._discount = discount
  
  value = property(get_discount, set_discount)

  def add_item(self, title, price, quantity=1):

    count = 0
    while count < quantity:
      self.items.append(title)
      self.last = {"title":title, "price":price, "quantity": quantity}
      count += 1
    self.total += (price*quantity)
  
  def void_last_transaction(self):
    self.total -=(self.last["price"] * self.last["quantity"])
    self.items.pop()
    if len(self.items) == 0:
      self.total = 0.0
  
  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total*((100-self.discount)*.01)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    