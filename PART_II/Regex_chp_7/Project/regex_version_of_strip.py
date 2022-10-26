#chap 7



def stripfunc(string,string2=''):
    if string2 != '':
        for x in string2:
            for y in string:
                if x == y:
                    string = string.replace(y," ")
        result = ''          
        for z in string:
            if z != " ":
                result += z   
        print(result)                 
    else:
        print(string.strip())

maleName = "    Stephan "
stripfunc(maleName,'tan')