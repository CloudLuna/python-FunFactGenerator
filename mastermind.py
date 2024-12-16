#Code-breaking game 
import random as r

def select_difficulty():
    return int(input("Please select a difficulty (1,2,3,4,5): "))


def generate_code(difficulty):
    return int(r.random()*(10**difficulty))


def get_score(code,guess):
    correct    = 0
    missplaced = 0
    wrong      = 0
    guess_list = [int(x) for x in str(guess)]
    code_list  = [int(x) for x in str(code) ]
    for j in range(len(guess_list)-1,-1,-1):
        if (code_list[j]) == (guess_list[j]):
            correct += 1
            guess_list.pop(j)
            code_list.pop(j)
    for k in guess_list:
        if k in code_list:
            missplaced += 1
            code_list.remove(k)
    wrong = len(code_list)
    return [correct, missplaced, wrong]


def print_score(score):
    print('{0:20} : {1:5}'.format('Correct','/'*score[0]))
    print('{0:20} : {1:5}'.format('Missplace','/'*score[1]))
    print('{0:20} : {1:5}'.format('Wrong','/'*score[2]))


print("--------------------------------")
print("---Python guess a number game---")
print("--------------------------------")
print()
win = 0
difficulty = select_difficulty()
code = generate_code(difficulty)

#print(code)
for i in range((difficulty+1)*3):
    print()
    guess = input(f'Guess a {difficulty} digit number: ')
    score = get_score(code,guess)
    print_score(score)
    if score[0] == difficulty:
        print("You win!!")
        win = 1
        break
if win == 0: print("You lost!!")    