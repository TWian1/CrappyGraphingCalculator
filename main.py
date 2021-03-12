boardtxt = open('board.txt', 'r')
board = []
counter = -1
for a in boardtxt.readlines():
  counter += 1
  board.append([])
  counter2 = -1
  for b in a:
    counter2 += 1
    if b == "\n":
      continue
    board[counter].append([])
    board[counter][counter2].append(b)
#print(board)
boardtxt.close()
print('By TheWolfIan \n \nIf you want a negative Y Intercept then do ex: +-5.  If you want to clear the board typr "clear".  This is a prototype, it\'s not ment to be great.  Don\'t use spaces when typing the equation.\n \n Example Equations: y=x+4, y=x+-2, 2y=-3x\n')
while True:
  equation = input("\nequation:")
  print("\n")
  if equation == "clear":
    boardtxt = open('board.txt', 'r')
    board = []
    counter = -1
    for a in boardtxt.readlines():
      counter += 1
      board.append([])
      counter2 = -1
      for b in a:
        counter2 += 1
        if b == "\n":
          continue
        board[counter].append([])
        board[counter][counter2].append(b)
    boardtxt.close()
    continue
  for a1 in range(len(equation)):
    if equation[a1] == "=":
      equalindx = a1
      break
  for a2 in range(len(equation)):
    if equation[a2] == "x":
      Xindx = a2
      break
  b5 = False
  for a3 in range(len(equation)):
    if equation[a3] == "+":
      Plusindx = a3
      b5 = True
      break
  for a8 in range(len(equation)):
    if equation[a8] == "y":
     Yindx = a8
  multnums = []
  for a4 in range(len(equation)):
    if a4 > equalindx and a4 < Xindx:
      multnums.append(a4)
  multnumsstr = ""
  for a5 in multnums:
   multnumsstr += equation[a5]
  if multnumsstr == "":
   multnumsstr = "1"
  slope = float(multnumsstr)
  ofnums = []
  if b5 == True:
    for a6 in range(len(equation)):
      if a6 > Plusindx:
       ofnums.append(a6)
  ofsetstr = ""
  for a7 in ofnums:
    ofsetstr += equation[a7]
  if b5 == True:
   offset = float(ofsetstr)
  else:
    offset = float(0)
  ymultstr = ""
  if Yindx > 0:
    for a9 in range(Yindx):
      ymultstr += equation[a9]
      print(ymultstr)
    ymult = float(ymultstr)
    slope = slope / ymult
    offset = offset / ymult
  temp2 = ""
  for b2 in range(240):
    b4 = b2/10 - 8
    temp = int((b4 * slope) + offset)
    if -1 * temp + 6 >= 13 or -1 * temp + 6 < 0:
      continue
    if int(b4) + 8 >= 17 or int(b4) + 8 < 0:
      continue
    #print(str(int(b4) + 8) + " " + str(-1 * temp + 6))
    #print(board)
    board[-1 * temp + 6][int(b4)+8][0] = "o"
  for b1 in range(13):
    for b3 in board[b1]:
      temp2 += b3[0]
    print(temp2)
    temp2 = ""
  print("\n")