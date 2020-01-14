import csv

def dicts(a_file, symbol_dict, group_dict, period_dict):
    data_reader = csv.reader(a_file)
    for line in data_reader:
        if line[0].isdigit():
            symbol_str = line[1]
            symbol_dict[symbol_str] = line[:8]
            if line[2] in group_dict:
                group_dict[line[2]].append(line[:8])
            else:
                group_dict[line[2]] = [line[:8]]

            if line[4] in period_dict:
                period_dict[line[4]].append(line[:8])
            else:
                period_dict[line[4]] = [line[:8]]
    
def is_metal(symbol_dict, input):
    nonmetals = {'H': symbol_dict['H']}
    #metalloids = [B, Si, Ge, As, Sb, Te, At]
    if input in symbol_dict:
        if input in nonmetals:
            print("Element is nonmetal.")
        elif symbol_dict[k] in metalloids:
            print("Element is metalloid.")
        else:
            print("Element is metal.")
    







def group_d(periodic_file, group_dict):
    data_reader = csv.reader(periodic_file)
    for line in data_reader:
        if line[0].isdigit():
            if line[2] in group_dict:
                group_dict[line[2]].append(line[1])
            else:
                group_dict[line[2]] = [line[1]]
    print(group_dict)
            #for keys in group_dict:
                #if keys.isdigit():
                    #group_dict = {int(k):v for k,v in group_dict.items()}
            
                #group_str = line[2]
                #group_dict[group_str] = line[:8]

def period_d(a_file, period_dict):
    data_reader = csv.reader(a_file)
    for line in data_reader:
        if line[0].isdigit():
            if line[4] in period_dict:
                period_dict[line[4]].append(line[1])
            else:
                period_dict[line[4]] = [line[1]]
    print(period_dict)
    
periodic_file = open("Periodic-Table.csv", "r", encoding="windows-1252")
symbol_dict={}
group_dict={}
period_dict={}

dicts(periodic_file, symbol_dict, group_dict, period_dict)
#group_d(periodic_file, group_dict)
#period_d(periodic_file, period_dict)

print(symbol_dict)
print(group_dict)
print(period_dict)

input("Enter an elemental symbol: \n")

is_metal(symbol_dict, input)
