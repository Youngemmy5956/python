Ace
Atlas
Bailey
Bear
Blaze
Boomer
Buddy
Coco
Cooper
Duke
Dozer
Echo
Gizmo
Harley
Mac
Max
Milo
Oscar
Rex
Rocky
Rocket

import random
f = open("petnames.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))

import random
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))