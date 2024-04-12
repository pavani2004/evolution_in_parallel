import sys

def is_evoluted(sample, current_species):
    i = j = 0
    while i < len(sample):
        if j == len(current_species):
            return False
        if sample[i] == current_species[j]:
            i += 1
        j += 1
    return True

def diff(fossils_found):
    lst1 = []
    lst2 = []
    for i in range(1, MAX):
        if fossils_found[i][0] == 0:
            continue
        else:
            if fossils_found[i][1] == 0:
                if len(lst1) == 0:
                    lst1.append(fossils_found[i][0])
                elif len(lst2) == 0:
                    if is_evoluted(lst[-1], fossils_found[i][0]):
                        lst1.append(fossils_found[i][0])
                    else:
                        lst2.append(fossils_found[i][0])
                else:
                    if not is_evoluted(lst1[-1], fossils_found[i][0]):
                        lst2.append(fossils_found[i][0])
                    elif not is_evoluted(lst2[-1], fossils_found[i][0]):
                        lst1.append(fossils_found[i][0])
                    else:
                        return -1
            else:
                if len(lst1) == 0:
                    lst1.append(fossils_found[i][0])
                    lst2.append(fossils_found[i][1])
                elif len(lst2) == 0:
                    if is_evoluted(lst1[-1], fossils_found[i][0]):
                        lst1.append(fossils_found[i][0])
                        lst2.append(fossils_found[i][1])
                    elif is_evoluted(lst1[-1], fossils_found[i][1]):
                        lst1.append(fossils_found[i][1])
                        lst2.append(fossils_found[i][0])
                    else:
                        return -1
    return len(lst1),len(lst2),lst1,lst2

def store():
    result = True
    for i in range(3, no_of_fossils_found+3):
        fossil_sample = sys.argv[i]
        fs = len(fossil_sample)
        if not is_evoluted(fossil_sample, current_species) or (fossils_found[fs][0] and fossils_found[fs][1]):
            result = False
            return -1
        elif fossils_found[fs][0] == 0:
            fossils_found[fs][0] = fossil_sample
        elif fossils_found[fs][1] == 0:
            fossils_found[fs][1] = fossil_sample
    if result:
        return diff(fossils_found)

MAX = 4000
no_of_fossils_found = int(sys.argv[1])
current_species = sys.argv[2]
fossils_found = [[0,0] for i in range(0, MAX)]
print(store())

