import search_functions as sf


def header():
     print("\nWelcome to the Fast Nutrition Advisor (WIP)") 

def main_menu():
     print( "1. Find Food by Maximum Calories\n"
            "2. Find Food by Minimum Calories\n"
            "3. Find Food by Minimum protein\n"
            "4. Find Food by Maximum fat\n"
            "5. Find Food by Minimum Fat\n"
            "6. Find Food by Maximum Carbs\n"
            "7. Quit Program\n")

def menu_choices():
    header()
    main_menu()
    while True:
        menu_choice = input("Please Choose One Option From Above: ")

        if menu_choice == "1":
            while True:
                try:
                    num_value = int(input("What is the maximum amount of calories you would like?: "))
                    break
                except:
                    print("Invalid command!")
            print(sf.find_food_by_max_calories(num_value))
            header()
            main_menu()
            continue  

        elif menu_choice == "2":
            while True:
                try:
                    num_value = int(input("What is the minimum amount of calories you would like?: "))
                    break
                except:
                    print("Invalid command!")
            print(sf.find_food_by_min_calories(num_value))
            header()
            main_menu()
            continue

        elif menu_choice == "3":
            while True:
                try:
                    num_value = int(input("What is the minumum amount of protein you would like?: "))
                    break
                except:
                    print("Invalid command!")
            print(sf.find_food_by_min_protein(num_value))
            header()
            main_menu()
            continue

        elif menu_choice == "4":
            while True:
                try:
                    num_value = int(input("What is the maximum amount of fat you would like?: "))
                    break
                except:
                    print("Invalid command!")
            print(sf.find_food_by_max_fat(num_value))
            header()
            main_menu()
            continue

        elif menu_choice == "5":
            while True:
                try:
                    num_value = int(input("What is the minimum amount of fat you would like?: "))
                    break
                except:
                    print("Invalid command!")
            print(sf.find_food_by_min_fat(num_value))
            header()
            main_menu()
            continue
            
        elif menu_choice == "6":
            while True:
                try:
                    num_value = int(input("What is the maximum amount of carbs you would like?: "))
                    break
                except:
                    print("Invalid command!")
            print(sf.find_food_by_max_carbs(num_value))
            header()
            main_menu()
            continue

        elif menu_choice == "7":
            quit()

        else:
            print("Invalid command!")
            
