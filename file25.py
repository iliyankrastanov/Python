
if __name__ == "__main__":
    config = {
        'Title': 'Text Editor',
        'Version': '1.2.4',
        'Temp': '/tmp',
        'Max_file': 1000
    }

    for item in config.items():
        key, value = item
        print(f"{key} => {value}")
       
    print("--- --- --- ---")