#
# Example file for working with classes
#

class myClass():
  def method1(self):
    print("myClass method1")
  
  def method2(self, someString):
    print(someString, "myClass method2")

def main():
  c = myClass()

  c.method1()
  c.method2("This is a string")

  
if __name__ == "__main__":
  main()
