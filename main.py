# This program calculates prices for custom signs.#

# Validate the Characters and compute the text cost ##
def checkInputChar(testChar):
  if testChar.isnumeric():
    return int(testChar)
  else:
    print(f"{testChar} is not a number. Please start over and try again.")
    exit()

def computeCharCost(preValChar): #this is the value from previous checkInputChar function
  if preValChar <= 5:
    return 0
  if preValChar > 5:
    return 4 * (preValChar - 5)

## Validate the Wood Type ##
def checkInputWood(testWood):
  if testWood == "oak" or testWood == "Oak":
    return 20
  if testWood == "pine" or testWood == "Pine":
    return 0
  else:
    print(f"{testWood} is not a valid wood type. Please enter Pine or Oak")
    exit()
    
## Validate the text input ##
def checkInputText(testText):
  if testText == "gold" or testText == "Gold":
    return 15
  if testText == "White" or testText == "white" or testText == "black" or testText == "Black":
    return 0
  else:
    print(f"{testText} is not a valid Input. Please list if text is Black, White, or Gold")
    exit()


##### Declare and initialize variables here. #####
charge = 0.00
minCharge = 35.00
numChar = input("Number of characters: ")
numCharValid  = checkInputChar(numChar)
woodType = input("Oak or Pine?: ")
colorText = input("White, Black, or Gold text?: ")


##### Computing Charges ##### 
charCharge = computeCharCost(numCharValid)
woodCharge = checkInputWood(woodType)
textCharge = checkInputText(colorText)


##### Output of total cost #####
totalCost = charge +minCharge +charCharge +woodCharge +textCharge
print("The charge for this sign is: ${:.2f}".format(totalCost))