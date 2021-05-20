import re

if __name__ == "__main__":
    txt = 'Lorem, ipsum dolor sit amet, consectetur, adipiscing elit, sed, do eiusmod'

    pattern = re.compile(r'[,]')
    result = re.split(pattern, txt)

    print(result)

    print("--- --- --- ---")