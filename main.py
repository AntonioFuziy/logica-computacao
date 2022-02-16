import sys

input_string = sys.argv[1]
parse_string = input_string.replace(' ', '')

number = 0
sub_list = []

if input_string[0] == '-' or input_string[0] == '+':
  raise ValueError

if "-" and "+" not in parse_string:
  raise ValueError

split_sum = parse_string.split('+')

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
print(number)