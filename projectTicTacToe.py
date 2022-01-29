pattern = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
counter_x=0
counter_o=0

def when_not_(pointer):#בודק שאין מקף תחתון
    if pointer == '_':
        return False
    else:
        return True

def clean_pattern():  #מנקה את התבנית
    global pattern
    pattern = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    print("it's a draw")
    print("let's try again")

def print_board():
    """
    בניית פונקציה המדפיסה לוח של המשחק
    :return: print pattern
    """
    global pattern
    for i in pattern:
        print(i)

print_board()
while True:
    line=int(input('enter the line (0-2)'))
    raw=int(input('enter the raw (0-2)'))
    if 3 > line >= 0 and 3 > raw >= 0 and pattern[line][raw] == '_':
      if counter_x>=counter_o:
          pattern[line][raw] = 'x'
          print_board()
          counter_o += 1
      else:
          pattern[line][raw] = 'o'
          print_board()
          counter_x += 1
         # בדיקה של כל התנאים לניצחון
    if pattern[0][0] == pattern[0][1]== pattern[0][2] and when_not_(pattern[0][2]) :
        print(pattern[0][0] + ' is the winner!!')
        break
    if pattern[1][0] == pattern[1][1] == pattern[1][2] and when_not_(pattern[1][2]) :
        print(pattern[1][0] + ' is the winner!!')
        break
    if pattern[2][0] == pattern[2][1] == pattern[2][2] and when_not_(pattern[2][2]):
        print(pattern[2][0] + ' is the winner!!')
        break
    if pattern[0][0] == pattern[1][0] == pattern[2][0] and when_not_(pattern[2][0]):
        print(pattern[0][0] + ' is the winner!!')
        break
    if pattern[0][1] ==pattern[1][1] == pattern[2][1] and when_not_(pattern[2][1]):
        print(pattern[0][1] + ' is the winner!!')
        break
    if pattern[0][2] == pattern[1][2] == pattern[2][2] and when_not_(pattern[2][2]):
        print(pattern[0][2] + ' is the winner!!')
        break
    if pattern[0][0] == pattern[1][1] == pattern[2][2] and when_not_(pattern[2][2]):
        print(pattern[0][0] + ' is the winner!!')
        break
    if pattern[0][2] == pattern[1][1] == pattern[2][0] and when_not_(pattern[2][0]):
        print(pattern[0][2] + ' is the winner!!')
        break
    #  בדיקה של כל התאים אם הם כולם שונים ממקף תחתון ואין מנצח ירוקן את התבנית ויריץ את המשחק מהתחלה
    if when_not_(pattern[0][0]) and when_not_(pattern[0][1])\
         and when_not_(pattern[0][2]) and when_not_(pattern[1][0]) \
         and when_not_(pattern[1][1]) and when_not_(pattern[1][2]) and when_not_(pattern[2][0]) \
         and when_not_(pattern[2][1]) and when_not_(pattern[2][2]):
        clean_pattern()
