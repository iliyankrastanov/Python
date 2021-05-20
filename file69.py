import re

if __name__ == "__main__":
    txt = 'Lorem ipsum dolor sit 956-34-56 amet, consectetur 234-56-78 adipiscing elit, sed do eiusmod'
    #txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod'

    pattern = re.compile(r'\d{3}\D\d{2}\D\d{2}')
    m = re.search(pattern, txt)
    print(m.group() if m else 'not found')

    result = re.findall(pattern, txt)
    print(result)
    
    print("--- --- --- ---")