#main function, runs everything; also controls what user sees
def main():
    with open('testdata.txt','r') as cow:
        lines = cow.readlines()
    cow.close()
    
    cownames = []
    #tokenization
    lines = [sub.split() for sub in lines]
    #sorts cows names
    for line in lines:
        if line[0] not in cownames:
            cownames.append(line[0])
    Listofcows = [[]] * len(cownames)
    #runs each cow name, all of the lines, and all present cownames into cowCheck
    for name in cownames:
        Listofcows[cownames.index(name)] = cowCheck(lines, name, cownames)
    
    fixPrint(Listofcows)
    
#prints out results in a way only an autograder could love
def fixPrint(Listofcows):
    for value in Listofcows:
        print(value[0],value[1],value[2],value[3])

#the function that actually sorts input
def cowCheck(lines, name, cownames):
    returnme = []
    milk = []
    weight = []
    for line in lines:
        #checks so cow names arent doubled
        if not returnme:
            returnme.append(int(name))
        #if name present
        if name in cownames:
            #if 2nd part of line and name equal 
            if line[1] == 'W' and line[0] == name:
                #add to weight list
                weight.append(int(line[2]))
            if line[1] == 'M' and line[0] == name:
                #add to milk list
                milk.append(int(line[2]))
                
    #lowest weight
    returnme.append(min(weight))
    #latest milk
    returnme.append(weight[len(weight)-1])
    #average milk
    returnme.append(int(sum(milk)/len(milk)))
    return returnme

if __name__ == "__main__":
    main()