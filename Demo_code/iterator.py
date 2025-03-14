class MyNumbers:
  def __iter__(self): #usee to iterate
    self.i = 1
    return self

  def __next__(self):# to execute next iterator
    x = self.i
    self.i += 1
    return x

myclass = MyNumbers() #calling class
myiter = iter(myclass)#calling iterator

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("this is Second class output")
class Mynum:
  def __iter__(self):
    self.a=1
    return self
  
  def __next__(self):
    if self.a < 20:
      c=self.a
      self.a+=1
      return c
    else:
      raise StopIteration
m=Mynum()
my_iter=iter(m)

for c in my_iter:
  print(c)

  