
if __name__ == "__main__":

    users = ["Anna", "Maria", "Markus", "Jane", "John"]
    mails = ["Anna@no.com", "Maria@no.com", "Markus@no.com", "Jane@no.com"]
    users_dict = {}

    for data in zip(users, mails):
        user, mail = data
        print(f"{user} => {mail}")
        users_dict[user] = mail

    print(users_dict)   
    print("--- ---")