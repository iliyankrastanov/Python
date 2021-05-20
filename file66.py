import re

if __name__ == "__main__":
    names = None

    #pattern = re.compile('^\w+\\s+\w+$')
    pattern = re.compile('^([A-Z][a-z]+)\\s+([A-Z][a-z]+)$')
    

    while not names:
        names = input('your names (firstname lastname:')
        m = pattern.match(names)
        if not m:
            names = None
            continue
        print(f'names start:{m.start()} end:{m.end()} span:{m.span()}')
        print(f'gropu:{m.group()} firstname:{m.group(1)} lastname:{m.group(2)}')
        
    
    print("--- --- --- ---")