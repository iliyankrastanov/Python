import re

if __name__ == "__main__":
    names = None

    #pattern = re.compile('^\w+\\s+\w+$')
    pattern = re.compile('^\\s*(?P<first>[A-Z][a-z]+)\\s+(?P<last>[A-Z][a-z]+)\\s*$')
    

    while not names:
        names = input('your names (firstname lastname:')
        m = pattern.match(names)
        if not m:
            names = None
            continue
        print(f'names start:{m.start()} end:{m.end()} span:{m.span()}')
        print(f'gropu:{m.group()} firstname:{m.group("first")} lastname:{m.group("last")}')
        
    
    print("--- --- --- ---")