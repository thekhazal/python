#
# Example file for working with conditional statements
#

def main():
  x, y = 1000, 1000
  
  # conditional flow uses if, elif, else  
  if (x < y):
    st = "x less than y"
  elif(x == y):
    st = "x is equal as y"
  else:
    st = "y less than x"
  print(st)

  # conditional statements let you use "a if C else b"
  st = "x is less than y" if (x<y) else "x is greater than y"
  print(st)



if __name__ == "__main__":
  main()
