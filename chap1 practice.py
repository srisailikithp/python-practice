#Q1. write a pogram to print twinkel twinkel little star poem in python .
print(''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Twinkle, twinkle, little star,
How I wonder what you are!
''')

# Q2. write a program to print the contents of a directory using the oos module. 
import os

directory = "."

for item in os.listdir(directory):
    full_path = os.path.join(directory, item)
    print(full_path)
