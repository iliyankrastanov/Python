import re

if __name__ == "__main__":
    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod'

    pattern = re.compile(r'(\w+)')

    for wrd in pattern.finditer(txt):
        print(f'start:{wrd.start()} end:{wrd.end()} span:{wrd.span()} group:{wrd.group()}')

    print("--- --- --- ---")