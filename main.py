#Battle game
import random
from random import randrange

class playerCharacter:
    def __init__(self, name, health, maxHealth, weapon): #name is the character type. Example: Warrior
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.weapon = weapon
        self.powerupProgress = 0
        self.powerupMax = 0

playerCharacter(0,0,0,0)

class Sword:
    def __init__(self):
        self.name = "Sword"
        self.powerValue = 0
        self.maxPowerValue = 2
        self.minDamage = 5
        self.maxDamage = 15
        self.powerDamage = 40

class Axe:
    def __init__(self):
        self.name = 'Axe'
        self.powerValue = 0
        self.maxPowerValue = 3
        self.minDamage = 8
        self.maxDamage = 12
        self.powerDamage = 60

class MagicBall:
    def __init__(self):
        self.name = "Magic Orbs"
        self.powerValue = 0
        self.maxPowerValue = 3
        self.minDamage = 7
        self.maxDamage = 14
        self.powerDamage = 60

class Spell:
    def __init__(self):
        self.name = "Cursed Spells"
        self.powerValue = 0
        self.maxPowerValue = 2
        self.minDamage = 4
        self.maxDamage = 17
        self.powerDamage = 40

class enemy:
    def __init__(self, name, health, maxHealth, attack):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.attack = attack

enemy(0,0,0,0)

###SETUP###

def setupMatch():
    print("Welcome to Shrimp!")
    pickCharacter()

def say(message): #Only use for simple messages, otherwise problems occur.
    print('--', message, '--')

def pickCharacter():
    say("Choose two characters, the warrior, or the wizard -- \n 1) Warrior \n 2) Wizard \n --Type the number of the character you want")
    x = input()
    if x == "1":
        playerCharacter.name = "Warrior"
        print("--You are a", playerCharacter.name, "--")
        pickHealth()
    elif x == "2":
        playerCharacter.name = "Wizard"
        print("--You are a", playerCharacter.name, "--")
        pickHealth()
    else:
        invalidResponse()
        pickCharacter()

def pickHealth():
    minHealth = 100
    maxHealth = 200
    healthRandomInterval = 10
    randomHealth = randrange(healthRandomInterval + 1) * healthRandomInterval + minHealth
    if randomHealth >= maxHealth:
        playerCharacter.health = maxHealth
        playerCharacter.maxHealth = playerCharacter.health
    else:
        playerCharacter.health = randomHealth
        playerCharacter.maxHealth = playerCharacter.health
    print("Health:", playerCharacter.health)
    pickWeapon()

def pickWeapon():
    warriorWeapons = [Sword(), Axe()]
    wizardWeapons = [MagicBall(), Spell()]
    if playerCharacter.name == "Warrior":
        playerCharacter.weapon = warriorWeapons[randrange(len(warriorWeapons))]
        print("Weapon:", playerCharacter.weapon.name)
    elif playerCharacter.name == 'Wizard':
        playerCharacter.weapon = wizardWeapons[randrange(len(wizardWeapons))]
        print("Weapon:", playerCharacter.weapon.name)
    else:
        print('Unknown Error.')
    findEnemy()

def findEnemy():
    enemyTypes = ['Monster', 'Dragon']
    enemy.name = enemyTypes[randrange(len(enemyTypes))]
    enemyHealthConstant = 1.75 #Multiplier
    enemy.health = playerCharacter.health * enemyHealthConstant
    enemy.maxHealth = enemy.health
    say('Enemy found!')
    say('Enemy Info')
    print('Enemy:', enemy.name)
    print('Health:', enemy.health)
    chooseMove()

def chooseMove():
    say('Choose a Move')
    print('1) Attack')
    print('2) Defend')
    print('3) Special')
    move = input()
    if move == "1":
        print('Attack')
    elif move == "2":
        print('Defend')
    elif move == "3":
        print('Special')
    else:
        invalidResponse()
        chooseMove()

def invalidResponse():
    print("***Invalid Response***")
    return        

###SETUP###

setupMatch() #Do not remove or the program will not run.2
