def save(pwd, save_name):
    with open('passwords.txt', 'a') as file:
        file.write(save_name + 'Account - ' + pwd + ',' + '\n')
