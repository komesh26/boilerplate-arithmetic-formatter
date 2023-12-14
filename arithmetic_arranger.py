def arithmetic_arranger(problems, display_total=False):
  prob_length = len(problems)

  if prob_length > 5:
    return 'Error: Too many problems.'

  #print(prob_length)
  n1 = list()
  n2 = list()
  op = list()
  total = list()

  for i in problems:
    if i.split()[1] == '/' or i.split()[1] == '*':
      return "Error: Operator must be '+' or '-'."

    if len(i.split()[0]) > 4 or len(i.split()[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    if not i.split()[0].isnumeric() or not i.split()[2].isnumeric():
      return 'Error: Numbers must only contain digits.'

    #print(i.split()[0])
    n1.append(i.split()[0])
    op.append(i.split()[1])
    n2.append(i.split()[2])
    total.append(eval(i.split()[0] + i.split()[1] + i.split()[2]))

  def addspace(n):
    sp = ''
    for i in range(n):
      sp = sp + ' '
    return sp

  def addsaperator(n):
    sp = ''
    for i in range(n):
      sp = sp + '-'
    return sp

  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  text_return = ''

  #print('aa', total)

  for i in range(prob_length):
    print(i, prob_length)
    width = len(n1[i]) + 2 if len(n1[i]) > len(n2[i]) else len(n2[i]) + 2

    #print('width', width)

    line1 = line1 + addspace(width - len(n1[i]))
    if i == prob_length - 1:
      line1 = line1 + n1[i]
    else:
      line1 = line1 + n1[i] + '    '

    line2 = line2 + op[i] + ' '
    line2 = line2 + addspace(width - len(n2[i]) - 2)
    if i == prob_length - 1:
      line2 = line2 + n2[i]
    else:
      line2 = line2 + n2[i] + '    '

    if i == prob_length - 1:
      line3 = line3 + addsaperator(width)
    else:
      line3 = line3 + addsaperator(width) + '    '

    line4 = line4 + addspace(width - len(str(total[i])))
    if i == prob_length - 1:
      line4 = line4 + str(total[i])
    else:
      line4 = line4 + str(total[i]) + '    '


# print(line1 + '\n' + line2 +'\n'+ line3 +'\n'+ line4)

  if display_total:
    text_return = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
  else:
    text_return = line1 + '\n' + line2 + '\n' + line3

  print(text_return)
  return text_return
