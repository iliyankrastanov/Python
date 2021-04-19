def show(title, a = 100, *args, **kwargs):
    print(f"positional arg title = {title}")

    print(f"default arg a = {a}")
    print("args")
    for v in args:
        print(f"arg:{v}", end = ' ')
    print()

    print(f"keyword args")
    if "log" in kwargs:
        print(f'log file:{kwargs["log"]}')
    if "path" in kwargs:
        print (f'app path:{kwargs["path"]}')
    print(" - " * 20)
if __name__ == "__main__":
    show("Text Editor")

    show("Calculator", 1)

    show("Calculator", 1, 10,20,30,40)

    show("Calculator", 1, 10,20,30,40, log = "messages.log", path = "/usr/local")

    config = {
        'app_title': 'Text Editor',
        'Version': '1.2.4',
        'Temp': '/tmp',
        'Max_file': 1000,
        'path': 'usr',
        'log': 'calculator.log'
    }

    print("--- --- --- ---")