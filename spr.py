import random
def play():
  user=input("What's your choice? 'r' for rock, 'p' for paper, 's' for sissors\n")
  computer=random.choice(['r','p','s'])
  if user==computer:
    return 'tie'
  if is_win(user,computer):
    return'you win!'
  return 'you lost!'
def is_win(user,computer):
  if (user=='r'and computer=='s')or(user=='s'and computer=='p')or(user=='p'and computer=='r'):
    return True
s=play()
print(s)
