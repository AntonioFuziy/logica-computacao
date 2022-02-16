import sys

# string test "10   +  5 - 4   + 4 -   10"
input_string = sys.argv[1]
parse_string = input_string.replace(' ', '')
print(parse_string)
print("")

soma = False
sub = False

number = 0
sub_list = []

if input_string[0] == '-' or input_string[0] == '+':
  raise ValueError

split_sum = parse_string.split('+')

print(split_sum)

for i in split_sum:
  if "-" not in i:
    number += int(i)
  else:
    sub_list.append(i)

if len(sub_list) > 0:
  for sub_operation in sub_list:
    sub_string = sub_operation.split('-')
    for sub_index in range(len(sub_string)):
      if sub_index == 0:
        number += int(sub_string[sub_index])
      else:
        number -= int(sub_string[sub_index])
    print(sub_string)
print(number)