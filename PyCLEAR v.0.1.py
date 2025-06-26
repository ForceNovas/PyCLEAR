print("PyCLEAR V0.1; Write 'help' for programs list.")
import os
import getpass
username = getpass.getuser()
cmd = True
folder_path = f"C:/Users/{username}/Documents/PyCLEAR"
reset_option = ''
notation = ''
while cmd == True:
    prompt = input("Please, write your command:  ")
    prompt = prompt.lower()  # Затычка для команд КАПСОМ

    #команда print

    if prompt == 'print':
        notation_quit = False
        paragraphing = True
        print("PyCLEAR session // For stoping paragraphing write '!q'")
        if notation == '':
            notation = input()
        if notation == '!q':
            paragraphing == False
            notation_quit = True
            special_commands = ''
            notation = ''
        else:
            while paragraphing == True:
                notation_1 = input()                                            #1 Ввод текста без проблем с абзацами, а также команды vim-like.
                if notation_1 == '!q':       #Выход из сессии                                 
                    paragraphing = False
                elif notation_1 == '!reset': #Сброс пути
                    reset_option = input('You are going to reset folder path. Are you sure? (+/-): ')
                    if reset_option == '+':
                        folder_path = f"C:/Users/{username}/Documents/PyCLEAR"
                        print('Path changed.')
                    elif reset_option == '-':
                        print('Going back to work.')
                    else:
                        print("You've made a mistake.  Please, write '+' or '-'. Going back to work.")
                else:                                                           
                    notation = notation + '\n ' + notation_1                    
        if notation_quit == False:
            special_commands = input('Anything special? Write +/- \n')
        if special_commands == '-':
            print(notation)
        elif special_commands == '':
            print('')
        elif special_commands == "+":
            try:
                special = input("Enter a command (e.g., .title(), .upper(), .lower()) \n ")
                notation = eval(f"notation{special}")
                print(notation)
            except Exception as error:
                print("Something went wrong while processing your command:")
                print(f"Error: {error}")
                print("Please try again. Write 'printerror' to continue from last action")
        else:
            print("You've made a mistake.  Please, write '+' or '-'. Telling you your input")
            print(notation)   
        paragraphing = True
        notation_quit = False
        print("Command complete. To save file use 'save'")

        # Сохранение файлов (save)

    elif prompt == 'save':
        save_option = input("Do you want to safe file? (+/-): ")
        if save_option == "+":
            os.makedirs(folder_path, exist_ok=True)
            filename = input("Enter filename: ")
            full_path = os.path.join(folder_path, filename)
            try:
                full_path = os.path.join(folder_path, f"{filename}.txt")  # добавляем .txt здесь
                with open(full_path, "w", encoding="utf-8") as save:
                    save.write(notation)
                print(f"'{filename}.txt' saved successfully!")
            except Exception as error_save:
                print("Something went wrong while saving this file.")
                print(error_save)
    
    #Команда для новой сессии
    elif prompt == 'reprint':
        print('Starting new print session.')
        notation = ''
    # Команда для справки о доступных переменных
    
    elif prompt == 'check':
        print('Current processes:')
        if notation != '':
            print('Your last file still here!')
        else:
            print("There is no files in this session.")
    # Команда для изменения пути сохранения
    
    elif prompt == 'changefolder':
        path_change = ''

        path_change = input(f'Your current path: C:/Users/{username}/Documents/PyCLEAR. Do you want to change it? (+/-): ')
        if path_change == '+':
            folder_path = input("Please, write your path. It should be like 'C:/Users/username/Documents/NewPyCLEAR' \n")
            print('If something will happen, just use "!reset".')
        elif path_change == '-':
            print("Command haven't been activated.")
        else:
            print("Incorrect answer. Command haven't been activated.")
    # Команда для восстановления print (printerror)

    elif prompt == 'printerror':
        try:
            special = input("Enter a command (e.g., .title(), .upper(), .lower()) \n ")
            notation = eval(f"notation{special}")
            print(notation)
            print('Backup complete')
        except Exception as error:
            print("Something went wrong while processing your command:")
            print(f"Error: {error}")
            print("Please try again. Write 'printerror' again to continue from last action")

     # Команда clear

    elif prompt == 'clear':
        countclear = 0
        while countclear <= 100:
            print("")
            countclear += 1
        print("Clearing complete.")

     # Команда exit

    elif prompt == 'quit':
        break
    elif prompt == '!q':
        break
    elif prompt == 'help':
        print('\n This program was created by ForceNova. The main function is editing text into caps, queen-like text, and no-caps text.')
        print('\n List of commands: \n')
        print('help // List of available programs')
        print('print // Simple text editor. Allows you to modify text into Python-style formats (title, lower, and others)')
        print('reprint // Starts new write session')
        print('save // Save file')
        print('clear // Clears the screen from clutter.')
        print('changefolder // Changes saves folder_path')
        print("quit; !q // Close session.")
        print('check // check, if program have any save files')
        print("\n This is my first program, so I won't mind criticism and notes on ways to optimize it. Written 85% by a human. \n")
    else: # Неправильно введеная программа
        print('Unknown command. Try again')




## Мб сделать из 2 файлов пайклир? или хуета затея