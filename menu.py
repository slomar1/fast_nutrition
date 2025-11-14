import search_functions as sf


def main_menu():
     
     print( "1. Find Food by Maximum Calories\n"
            "2. Find Food by Minimum Calories\n"
            "3. Find Food by Minimum protein\n"
            "4. Find Food by Maximum fat\n"
            "5. Find Food by Minimum Fat\n"
            "6. Find Food by Maximum Carbs\n"
            "7. Quit Program\n")


def try_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print("Invalid command!")


def menu_choices():
    
    main_menu()
    
    while True:
        menu_choice = input("Please Choose One Option From Above: ")

        if menu_choice == "1":
            num_value = try_int("What is the maximum amount of calories you would like?: ")
            print(sf.find_food_by_max_calories(num_value))
            main_menu()
            continue  

        elif menu_choice == "2":
            num_value = try_int("What is the minimum amount of calories you would like?: ")
            print(sf.find_food_by_min_calories(num_value))
            main_menu()
            continue

        elif menu_choice == "3":
            num_value = try_int("What is the minumum amount of protein you would like?: ")
            print(sf.find_food_by_min_protein(num_value))
            main_menu()
            continue

        elif menu_choice == "4":
            num_value = try_int("What is the maximum amount of fat you would like?: ")
            print(sf.find_food_by_max_fat(num_value))
            main_menu()
            continue

        elif menu_choice == "5":
            num_value = try_int("What is the minimum amount of fat you would like?: ")
            print(sf.find_food_by_min_fat(num_value))
            main_menu()
            continue
            
        elif menu_choice == "6":
            num_value = try_int("What is the maximum amount of carbs you would like?: ")
            print(sf.find_food_by_max_carbs(num_value))
            main_menu()
            continue

        elif menu_choice == "7":
            quit()

        else:
            print("Invalid command!")