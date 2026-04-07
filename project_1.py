
import random
import string

def color_generator(color_type,count):
  colors=[]
  letters = string.digits+"abcdef"
  if color_type == "hexa":
      for i in range(count):
          final1 =""

          for j in range(6):
              final1+=random.choice(letters)

          colors.append("#"+final1)
      return colors
  
  elif color_type =="rgb":
   
   for p in range(count):
       r = random.randint(0,255)
       g = random.randint(0,255)
       b = random.randint(0,255)
       
       colors.append(f"rgb({r},{g},{b})")
       return colors
   
  else:
       return "Invalid color type"
      
print(color_generator("hexa",4))
print(color_generator("rgb",3))
      
print(color_generator("hexa",7))
print(color_generator("rgb",9))
