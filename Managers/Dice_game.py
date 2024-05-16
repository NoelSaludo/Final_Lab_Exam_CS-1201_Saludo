import datetime
import random
from Models.Score import Score
import os
class DiceGame():
    listofScores = []
    datapath = os.path.join("data", "scores.txt")

    def __init__(self):
        if not os.path.exists(self.datapath):
            with open(self.datapath, "w") as file:
                pass
        self.load_scores()
    
    def load_scores(self):
        with open(self.datapath, "r") as file:
             for line in file:
                name, value, date, won = line.strip("\n").split(",")
                score = Score(name, int(value), date, won)
                self.listofScores.append(score)
        pass
    
    def save_scores(self):
        with open(self.datapath, "w") as file:
            for score in self.listofScores:
                file.write(f"{score.name},{score.value},{score.date},{score.stagewon}\n")
        pass
    
    def play_game(self, player: str):
            stage = 0
            finalscore = 0
            while True:
                pscore, cpuscore = 0, 0
                turn = 1
                while turn < 4:
                        cpudice, playerdice = random.randint(1, 6), random.randint(1, 6)
                        print(f"{player} rolled {playerdice}")
                        print(f"CPU rolled {cpudice}")
                        if playerdice > cpudice:
                            pscore += 1
                        elif playerdice == cpudice:
                             pass
                        else:
                            cpuscore += 1
                        turn += 1
                if pscore > cpuscore:
                    print(f"{player} wins stage {stage}")
                    stage += 1
                    finalscore += pscore + 3
                    nextstage = input("Do you want to continue to next stage? (y/n)")
                    if nextstage.lower == 'n':
                        break
                    continue
                else:
                    print(f"CPU wins stage {stage}")
                    print(f"Game Over! CPU wins")
                date = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                score = Score(player, finalscore, date, stage)
                DiceGame.listofScores.append(score)
                break
                
    def show_top_scores(self):
        if len(self.listofScores) == 0:
            print("No scores available")
            return
        sortedlist = sorted(self.listofScores, key = lambda x: x.value, reverse = True)
        for score in sortedlist:
            print(f"{score.name}: Points - {score.value}, Wins - {score.stagewon}")
        pass

    
    if __name__ == "__main__":
        pass
    