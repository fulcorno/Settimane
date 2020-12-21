string = '(703)321-6753'

valid = len(string) == 13 # set valid to True or False
position = 0
while valid and position < len(string) :
   valid = ((position == 0 and string[position] == "(")
       or (position == 4 and string[position] == ")")
       or (position == 8 and string[position] == "-")
       or (position != 0 and position != 4 and position != 8
          and string[position].isdigit()))
   position = position + 1

print(valid)
