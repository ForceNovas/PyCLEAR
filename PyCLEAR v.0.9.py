print(f"PyCLEAR V0.9 win; Write 'help' for programs list.") # Приветствие
import os
import getpass
username = getpass.getuser()
config_path = f"C:/Users/{username}/Documents/PyCLEAR/config/config.txt"

# Try loading saved path
if os.path.exists(config_path):
    with open(config_path, 'r', encoding='utf-8') as cfg:
        saved_path = cfg.read().strip()
        if os.path.isdir(saved_path):
            folder_path = saved_path
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
                notation_1 = input()                     
                if notation_1 == '!q':                                     
                    paragraphing = False
                elif notation_1 == '!reset': 
                    reset_option = input('You are going to reset folder path. Are you sure? (+/-): ')
                    if reset_option == '+':
                        folder_path = f"C:/Users/{username}/Documents/PyCLEAR"
                        config_path = folder_path
                        print('Path changed.')
                    elif reset_option == '-':
                        print('Going back to work.')
                    else:
                        print("You've made a mistake.  Please, write '+' or '-'. Going back to work.")
                else:                                                           
                    notation = notation + '\n' + notation_1                    
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
    # Команда edit

    elif prompt == 'edit':
        lines = notation.strip().split('\n')
        while True:
            print("\nCurrent text:\n")
            for i, line in enumerate(lines):
                print(f"{i+1}: {line}")
            print("\nChoose an action:")
            print("1. Delete a line")
            print("2. Replace a line")
            print("3. Insert a line after another")
            print("4. Return to normal mode")
            
            choice = input("Enter the number of your choice (1–4): ")
            
            if choice == '1':
                try:
                    line_num = int(input("Enter the line number to delete: ")) - 1
                    if 0 <= line_num < len(lines):
                        removed_line = lines.pop(line_num)
                        print(f"Line '{removed_line}' deleted.")
                    else:
                        print("Invalid line number.")
                except ValueError:
                    print("Please enter a valid number.")
            
            elif choice == '2':
                try:
                    line_num = int(input("Enter the line number to replace: ")) - 1
                    if 0 <= line_num < len(lines):
                        new_line = input("Enter the new text: ")
                        lines[line_num] = new_line
                        print("Line updated.")
                    else:
                        print("Invalid line number.")
                except ValueError:
                    print("Please enter a valid number.")
            
            elif choice == '3':
                try:
                    line_num = int(input("Enter the line number to insert after: ")) - 1
                    if 0 <= line_num < len(lines):
                        insert_line = input("Enter the text to insert: ")
                        lines.insert(line_num + 1, insert_line)
                        print("Line inserted.")
                    else:
                        print("Invalid line number.")
                except ValueError:
                    print("Please enter a valid number.")
            
            elif choice == '4':
                notation = '\n'.join(lines)
                print("Exiting editor.")
                break
            else:
                print("Invalid input. Please choose between 1 and 4.")
        # Чтение файлов (read)

    elif prompt == 'read':
        read = input('Do you need read file from other directory? (+/-)')
        if read == '+':
            folder_path = input("Please, write your path. It should be like 'C:/Users/username/Documents/NewPyCLEAR' \n")
            print('If something will happen, just use "!reset".')
        elif read == '-':
            print("")
        else:
            print("Incorrect answer. Command haven't been activated.")
        filename = input("Enter the filename to read: ")
        full_path = os.path.join(folder_path, f"{filename}")
        try:
            with open(full_path, "r", encoding="utf-8") as file:
                file_content = file.read()
                print(f"\nContent of '{filename}.txt':\n")
                print(file_content)
                notation = file_content  # загружаем в рабочее поле
        except FileNotFoundError:
            print("File not found. Please check the name or use.")
        except Exception as error:
            print("Something went wrong while reading the file.")
            print(f"Error: {error}")
            
        # Сохранение файлов (save)
    
    elif prompt == 'save':
        if notation == '':
            print('The program have no files. Saved file will be empty.')
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
    #Сброс пути сохранения
    elif prompt == '!reset': #Сброс пути
        reset_option = input('You are going to reset folder path. Are you sure? (+/-): ')
        if reset_option == '+':
            folder_path = f"C:/Users/{username}/Documents/PyCLEAR"
            print(f'Path changed to "C:/Users/{username}/Documents/PyCLEAR".')
        elif reset_option == '-':
            print('Going back to work.')
        else:
            print("You've made a mistake.  Please, write '+' or '-'. Going back to work.")
    
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
        path_change = input(f'Your current path: {folder_path}. Do you want to change it? (+/-): ')
        if path_change == '+':
            folder_path = input("Please, write your path. It should be like 'C:/Users/username/Documents/NewPyCLEAR' \n")
            try:
                os.makedirs(os.path.dirname(config_path), exist_ok=True) 
                with open(config_path, 'w', encoding='utf-8') as cfg:     
                    cfg.write(folder_path.strip())
                print('Path has been successfully updated and saved.')
                print('If something will happen, just use "!reset".')
            except Exception as error:
                print("Something went wrong while saving the path:")
                print(f"Error: {error}")
        elif path_change == '-':
            print("Command haven't been activated.")
        else:
            print("Incorrect answer. Command haven't been activated.")

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
        print('read // Read file')
        print('edit // Edit file')
        print('!reset // Resets file directory ')
        print('clear // Clears the screen from clutter.')
        print('changefolder // Changes saves folder_path')
        print("quit; !q // Close session.")
        print('check // check, if program have any save files')
        print("\n This is my first program, so I won't mind criticism and notes on ways to optimize it. Written 85% by a human. \n")
    else: # Неправильно введеная программа
        print('Unknown command. Try again')



#  Также хочу заняться оптимизацией кода, чтобы эта смехуятина на 200 строк читалась приемлимо, а не через Ctrl + f
## Мб сделать из 2 файлов пайклир? или хуета затея
