from random_words import RandomWords
rw = RandomWords()
while True:
    cur = rw.random_word()
    solve = ''
    for i in range (len(cur)):
        solve += '*'
    tries = 6
    print('tries:' + str(tries))
    print(solve)
    while tries > 0:
        print('choose a letter')
        curlet = input()
        if len(curlet) == 1 and curlet.isalpha() and curlet.islower():
            if curlet in cur:
                for i in range (len(cur)):
                    if cur[i] == curlet:
                        solve = solve[:i] + curlet + solve[i + 1:]
                print(curlet + ' in word')
                print('tries:' + str(tries))
                print(solve)
                if solve.find('*') == -1:
                    print('you win!')
                    break
            else:
                print('not in word')
                tries -= 1
                print('tries:' + str(tries))
                print(solve)
        else:
            print('only one lowercase letter acceptable')
            continue
    print('the word was ' + cur)
    print('play again? (Y/N)')
    answer = input()
    if answer == 'y' or answer == 'Y':
        continue
    else:
        exit()
