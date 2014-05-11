#import double
import math
import time

items = []
price = float(0)
numItems = 1
order = {price: items}
orderTotal = float(0)
finalOrder = {}
hostessCredits = float(0)
halfPriceItems = 0

# Load a dictionary of (price:array of items at that price)

while True:
    while True:
        item = input("Please enter item #" + str(numItems) + ":")
        if item != "":
            break
        else:
            print('Please enter a value - enter "done" when finished')
    if (item == "done" or item == "Done"):
        break
    itemStr = "#" + str(numItems) + "-> " + item
    while True:
        price = input("Please enter the price of " + item + ":")
        try:
            val = float(price)
            break
        except ValueError:
            print("Please enter a number.")
            
    if str(price) in order:
        order[price].append(itemStr)
    else:
        tempList = [itemStr]
        order[price] = tempList
    numItems += 1


#print(order)
print("\n\n\n*****Calculating order*****\n\n\n")
time.sleep(5)


# zero price for 5/6 and summate order
priceArray = []
lastMaxPrice = 100000000000000000000000
while True:
    if lastMaxPrice == 0:
        break
    maxPrice = 0
    for num in order.keys():
        if int(num) > int(maxPrice) and int(num) < int(lastMaxPrice):
            maxPrice = num
    #print(str(maxPrice) + " : " + str(len(order[str(maxPrice)])))
    priceArray.append(maxPrice)
    lastMaxPrice = maxPrice
    
#print(priceArray)

itemsGrouped = 0
itemsRemaining = []
for priceVal in priceArray:
    while True:
        if len(order[priceVal]) == 0:
            break
        if itemsGrouped < 5:
            itemsGrouped += 1
            itemToMove = order[priceVal].pop()
            print("Cost is " + priceVal + " for " + itemToMove)
            orderTotal += float(priceVal)
            itemsRemaining.append([priceVal, itemToMove])
            if str(priceVal) in finalOrder:
                finalOrder[priceVal].append(itemToMove)
            else:
                tempList = [itemToMove]
                finalOrder[priceVal] = tempList
        else:
            itemsGrouped = 0
            itemToMove = order[priceVal].pop()
            newPrice = 0
            itemsRemaining.clear()
            print("FREEBEE " + str(newPrice) + " for " + itemToMove)
            if str(newPrice) in finalOrder:
                finalOrder[newPrice].append(itemToMove)
            else:
                tempList = [itemToMove]
                finalOrder[newPrice] = tempList

#print(finalOrder)
#print(itemsRemaining)
for item in itemsRemaining:
    orderTotal -= float(item[0])
    finalOrder[item[0]].remove(item[1])
print("\nOrder total used to calculate hosteess rewards is: " + str(orderTotal))
#print(finalOrder)
# check for party level

#TODO add functionality to split MEGA PARTIES (over $1200)

if orderTotal >= 1000:
    print("$1000 party! $120 in hostess credits and 6 half-price items!")
    hostessCredits = 120
    halfPriceItems = 6
elif orderTotal >= 800:
    print("$800 party! $90 in hostess credits and 5 half-price items!")
    hostessCredits = 90
    halfPriceItems = 5
elif orderTotal >= 500:
    print("$500 party! $60 in hostess credits and 4 half-price items!")
    hostessCredits = 60
    halfPriceItems = 4
elif orderTotal >= 400:
    print("$400 party! $45 in hostess credits and 3 half-price items!")
    hostessCredits = 45
    halfPriceItems = 3
elif orderTotal >= 300:
    print("$300 party! $35 in hostess credits and 2 half-price items!")
    hostessCredits = 35
    halfPriceItems = 2
elif orderTotal >= 200:
    print("$200 party! $25 in hostess credits and 1 half-price item!")
    hostessCredits = 25
    halfPriceItems = 1
elif orderTotal >= 100:
    print("$100 party! 1 half-price item!")
    hostessCredits = 0
    halfPriceItems = 1
else:
    print("Sorry, this party does not qualify for hostess rewards... sad panda")

#print(finalOrder)



# Calculate hostess rewards with the last 5 or less items
# if using the credit will reduce the item's cost by over 50%, use it
# else, use the half off item (if available)

while True:
##    if hostessCredits == 0 and halfPriceItems == 0:
##        break
    if len(itemsRemaining) == 0:
        break
    itemToModify = itemsRemaining.pop()
    if (int(itemToModify[0]) <= hostessCredits * 2) or (halfPriceItems == 0 and hostessCredits > 0):
        creditsToUse = float(0)
        if hostessCredits >= float(itemToModify[0]):
            creditsToUse = itemToModify[0]
        else:
            creditsToUse = hostessCredits
        hostessCredits = float(hostessCredits) - float(creditsToUse)
        newPrice = float(itemToModify[0]) - float(creditsToUse)
        print("\nUsing " + str(creditsToUse) + " in hostess credit")
        print("Reducing " + itemToModify[1] + " from " + itemToModify[0] + " to "
              + str(newPrice))
        itemToModify[0] = str(newPrice)
    elif(halfPriceItems > 0):
        newPrice = float(itemToModify[0]) / 2
        halfPriceItems -= 1
        print("\nUsing a half-price item!")
        print("Reducing " + itemToModify[1] + " from " + itemToModify[0] + " to "
              + str(newPrice))
        itemToModify[0] = str(newPrice)


        
    if str(itemToModify[0]) in finalOrder:
        finalOrder[itemToModify[0]].append(itemToModify[1])
    else:
        tempList = [itemToModify[1]]
        finalOrder[itemToModify[0]] = tempList



#print(finalOrder)
finalCost = float(0)
for key in finalOrder.keys():
    finalCost += (float(len(finalOrder[key])) * float(key))
print("\n\n\The final cost of this order is... " + str(finalCost))
