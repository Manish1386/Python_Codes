
class makeStartup():
    startlst=[1, 2, 3]

class UserInput():
    def user_guess(self):
        guess=int(input("Enter your guess here: "))
        return guess

class Game():
    def Check(self, Startup):
        y=UserInput()
        z = True
        while z==True:
            result = "miss1"
            guess_value = y.user_guess()
            for value in Startup:
                if value==guess_value:
                    result="hit"
                    Startup.remove(value)
                    if Startup == []:
                        result = "kill"
                        z=False
                    break
            print(result)

class GameLauncher():
    x=makeStartup()
    y=UserInput()

    z=Game()
    wg=x.startlst

    result=z.Check(x.startlst)


a=GameLauncher()
a.result