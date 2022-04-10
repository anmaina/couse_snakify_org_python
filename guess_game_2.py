n = int(input())
possible = set(range(n))
while True:
  line = input()
  if line == 'HELP':
    break
  guess = set([int(i) for i in line.split()])
  if input() == 'YES':
    possible &= guess
  else:
    possible -= guess
print(*sorted(possible))

# n = int(input())
# all_nums = set(range(1, n + 1))
# possible_nums = all_nums
# while True:
#     guess = input()
#     if guess == 'HELP':
#         break
#     guess = {int(x) for x in guess.split()}
#     answer = input()
#     if answer == 'YES':
#         possible_nums &= guess
#     else:
#         possible_nums &= all_nums - guess

# print(' '.join([str(x) for x in sorted(possible_nums)]))
        