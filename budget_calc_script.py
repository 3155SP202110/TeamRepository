#calculator logic

#inputs
numRooms = 0
foodRate = 0
nightlyRate = 0

print("Please enter the number of rooms your hotel has: ")
numRooms = input()
numRooms = int(numRooms)
print("Please enter how much a meal costs for one: ")
foodRate = input()
foodRate = int(foodRate)
print("Please enter how much one night of stay is: ")
nightlyRate = input()
nightlyRate = int(nightlyRate)
#calculate average monthly revenue
roomRevenue = nightlyRate * numRooms * 30 * .65 #average of 65% capacity - 30 days
foodRevenue = foodRate * numRooms * 30 * .75 * .65 #assuming food is ordered by 75% occupants at 65% of capacity - 30 days
totalRevenue = foodRevenue + roomRevenue

#---spending---
#labor
#maintenance - general maintenance $20,000 - energy $30,000 - equipment $10,000
#supplies - $10,000

housekeepers = 0
housekeeperWage = 13
clerks = 0
clerkWage = 12
managers = 0
managerWage = 28
supervisors = 0
supervisorWage = 21
security = 0
securityWage = 16
kitchen = 0
kitchenWage = 11
misc = 0
miscWage = 15

bills = 0
supplies = 0
maintenance = 0

if numRooms < 10:
    housekeepers = 2
    clerks = 2
    managers = 1
    supervisors = 1
    security = 0
    kitchen = 2
    misc = 0
    bills = 2000
    supplies = 1000
    maintenance = 2000

elif numRooms < 25 and numRooms >= 10:
    housekeepers = 5
    clerks = 2
    managers = 1
    supervisors = 1
    security = 0
    kitchen = 4
    misc = 1
    bills = 4000
    supplies = 2000
    maintenance = 4000
elif numRooms < 50 and numRooms >= 25:
    housekeepers = 10
    clerks = 4
    managers = 1
    supervisors = 1
    security = 1
    kitchen = 4
    misc = 3
    bills = 8000
    supplies = 4000
    maintenance = 8000
elif numRooms < 75 and numRooms >= 50:
    housekeepers = 15
    clerks = 5
    managers = 1
    supervisors = 2
    security = 2
    kitchen = 8
    misc = 5
    bills = 16000
    supplies = 8000
    maintenance = 16000
elif numRooms >= 75:
    housekeepers = 20
    clerks = 5
    managers = 2
    supervisors = 3
    security = 4
    kitchen = 10
    misc = 10
    bills = 32000
    supplies = 16000
    maintenance = 32000

#output
hkCost = housekeepers * housekeeperWage * 160
clerkCost = clerks * clerkWage * 160
mngrCost = managers * managerWage * 160
spCost = supervisors * supervisorWage *160
secCost = security * securityWage *160
kitchenCost = kitchen * kitchenWage *160
miscCost = misc * miscWage *160
totalLabor = hkCost + clerkCost + mngrCost + spCost + secCost + kitchenCost + miscCost
totalSpending = totalLabor + bills + supplies + maintenance

print("Here is how much you should spend per month:"
      + "\nHousekeepers: $" + str(hkCost)
      + "\nClerks: $" + str(clerkCost)
      + "\nManagers: $" + str(mngrCost)
      + "\nSupervisors: $" + str(spCost)
      + "\nSecurity guards: $" + str(secCost)
      + "\nKitchen staff: $" + str(kitchenCost)
      + "\nMiscellaneous Staff: $" + str(miscCost)
      + "\nTotal Labor: $" + str(totalLabor)
      + "\nBills: $" + str(bills)
      + "\nSupplies: $" + str(supplies)
      + "\nMaintenance: $" + str(maintenance)
      + "\nTotal Spending: $" + str(totalSpending))
