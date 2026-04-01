# ===============================================
# Loot Drop Simulator
# Author: Bailey Baxter
# Date: April 1, 2026
# Description: A CLI Tool that runs a simulation
#              to determine the likelihood of
#              video game loot being dropped
# ===============================================

# Imports
import random
from colorama import Fore, Back, Style, init
init(autoreset=True)


# Simulation Class
class Simulation:
    def __init__(self, dropRate, sims, luckBoost):
        self.dropRate = dropRate
        self.sims = sims
        self.luckBoost = luckBoost
        self.drops = 0
        self.ratio = 0
        self.avgRolls = 0
        self.totalLuck = 0

        

    def print_data(self):
        print(Fore.YELLOW + f"Drop Rate: {self.dropRate}% | Number of Simulations: {self.sims}")

    def run(self):
        for _ in range(self.sims):
            if random.random() < ((min(self.totalLuck,100)) / 100): # calculates if a random number falls into the total luck threshold to simulate a drop
                self.drops += 1 # item is dropped
        self.ratio = (self.drops/self.sims) * 100 # ratio is calculated
        if self.drops > 0:
            self.avgRolls = self.sims/self.drops # average rolls are calculated
        else:
            self.avgRolls = 0 # if there are no drops, the average rolls were 0

    def print_results(self):
        print(Fore.YELLOW + "You opened " + Fore.RED + str(self.sims) + Fore.YELLOW + " times and got " + Fore.GREEN + str(self.drops) + Fore.YELLOW + " drops! That is a ratio of " + Fore.GREEN + f"{self.ratio:.2f}" + Fore.YELLOW + "%!")
        if self.luckBoost != 0:
            print(Fore.YELLOW + f"You applied a luck boost of {self.luckBoost:.2f}%")
        if self.avgRolls == 0:
            print(Fore.RED + "You had 0 drops, so your average rolls per drop is 0.")
        else:
            print(Fore.YELLOW + "On average, it took about " + Fore.GREEN + f"{self.avgRolls:.2f}" + " rolls to get a drop.")
        if self.drops == 0:
            print(Fore.RED + "You were unlucky and had no drops with a ratio of 0%.")
        elif self.ratio < self.totalLuck:
            print(Fore.RED + "You were unlucky and had a lower rate of success than the original drop rate.")
        elif self.ratio > self.totalLuck:
            print(Fore.GREEN + "You were lucky and had a higher rate of success than the original drop rate!")
        else:
            print(Fore.YELLOW + "You had the same rate of success as the original drop rate!")
    
    def adjust_total_luck(self):
        self.totalLuck = self.dropRate+self.luckBoost # variable used to describe ds+lb
    
    def bar_graph(self):
        maxValue = max(self.ratio, (self.totalLuck))
        if maxValue == 0:
            maxValue = 1
        filledExpected = round(((self.dropRate / maxValue) * 20))
        filledBoost = round((((self.totalLuck)/ maxValue) * 20))
        filledActual = round(((self.ratio / maxValue) * 20))
        print("---Drop Rate Table---")
        print(Fore.YELLOW + f"{"Expected:":<10} {self.dropRate:>6.2f} |" + Fore.GREEN + "█" * filledExpected + Fore.RED + "░" * (20 - filledExpected))
        if self.luckBoost != 0:
            print(Fore.YELLOW + f"{"Boosted:":<10} {(self.totalLuck):>6.2f} |" + Fore.GREEN + "█" * filledBoost + Fore.RED + "░" * (20 - filledBoost))
        print(Fore.YELLOW + f"{"Actual:":<10} {self.ratio:>6.2f} |" + Fore.GREEN + "█" * filledActual + Fore.RED + "░" * (20 - filledActual))



def newRun():
    again = ""
    while again != "yes" and again != "no":
        again = (input(Fore.YELLOW + "Would you like run a new simulation? [yes/no] -> ")).lower().strip()
    if again == "yes":
        return True
    else:
        return False


def getData():
    dR = 0.0 # the drop rate percentage
    sims = 0 # the number of runs the simulation will do
    lB = -1.0 # the optional boost to luck
    while dR <= 0:
        try:
            dR = float(input("Enter drop rate % -> "))
            if dR <= 0:
                print(Fore.RED + "Please enter a number over 0.0")
        except ValueError:
            print(Fore.RED + "Invalid number!")
    while sims <= 0:
        try:
            sims = int(input("Enter number of simulations -> "))
            if sims <= 0:
                print(Fore.RED + "Please enter a number over 0")
        except ValueError:
            print(Fore.RED + "Invalid number!")
    while lB < 0:
        try:
            lB = float(input("Enter luck boost % [enter 0 if no luck boost] -> "))
            if lB < 0:
                print(Fore.RED + "Please enter a number 0 or larger!")
        except ValueError:
            print(Fore.RED + "Invalid number!")
    
    
    return dR, sims, lB
        

def createSim():
    dr, sims, luck = getData()
    newSim = Simulation(dr, sims, luck)
    return newSim


def main():
    print(Fore.MAGENTA + Style.BRIGHT + ("="*10) + Fore.YELLOW + " DROP RATE SIMULATOR " + Fore.MAGENTA + Style.BRIGHT + ("="*10))
    while True:
        simulate = createSim() # create a simulation object
        simulate.adjust_total_luck() # alter the luck total variable
        simulate.print_data() # output data user entered
        simulate.run() # run the simulations
        simulate.print_results() # print the results of the simulation
        simulate.bar_graph() # generate a bar graph
        again = newRun() # check if user wants to create a new simulation
        if not again:
            break
        print(Fore.MAGENTA + Style.BRIGHT + ("="*41))
    print(Fore.MAGENTA + Style.BRIGHT + ("="*10) + Fore.YELLOW + " DROP RATE SIMULATOR " + Fore.MAGENTA + Style.BRIGHT + ("="*10))


if __name__ == "__main__":
    main()