open_file = open("CupcakeInvoices.csv")




for order in open_file:
    order = order.rstrip('\n').split(',')
    # print(order)
    print(order[2])
      
open_file.seek(0)

for line in open_file:
    value = line.rstrip('\n').split(',')
    total = int(value[3]) * float(value[4])
    print(total)

open_file.seek(0)

total = 0

for line in open_file:
    value = line.rstrip('\n').split(',')
    total += int(value[3]) * float(value[4])

print(total)


chocolate = 0
vanilla = 0
strawberry = 0

open_file.seek(0)

for line in open_file:
    value = line.rstrip('\n').split(',')
    for flavor in value:
        if flavor == 'Chocolate':
            chocolate += 1
        elif flavor == 'Vanilla':
            vanilla += 1
        elif flavor == "Strawberry":
            strawberry += 1
print(chocolate)
print(vanilla)
print(strawberry)


    







