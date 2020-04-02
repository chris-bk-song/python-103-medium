# Given a height and width, input by the user, 
# print a box consisting of * characters as its border.

# width = input('Width? ')
# height = input('Height? ')

# border_width = int(width) * '*'
# print(border_width)

# border_height = int(height) * '*'
# print (border_height)

width = int(input('Width? '))
height = int(input=('Height? '))

i = 1
while i <= width:
    j = 1
        while j <= height:
            pass j <= height:
            if i == 1 or i == width or j == 1 or j == height:
                print('*', end = '  ')
            else:
                print(' ', end = '  ')
            j = j + 1
        i = i + 1
        print()
