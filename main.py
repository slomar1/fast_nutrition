import search_functions as sf


header = "Welcome to the Fast Nutrition Advisor (WIP)"
main_menu = "1. Find Food by Maximum Calories\n" \
            "2. Find Food by Minimum Calories\n" \
            "3. Find Food by Minimum protein\n" \
            "4. Find Food by Maximum fat\n" \
            "5. Find Food by Minimum Fat\n" \
            "6. Find Food by Maximum Carbs\n" \
            "7. Quit Program\n"





# Main Function
def main():

    print(header)
    print(main_menu)
    menu_choice = int(input("Please Choose One Option From Above: "))

    if menu_choice == 1:
        num_value = int(input("What is the maximum amount of calories you would like?: "))
        print(sf.find_food_by_max_calories(num_value))

    elif menu_choice == 2:
        num_value = int(input("What is the minimum amount of calories you would like?: "))
        print(sf.find_food_by_min_calories(num_value))

    elif menu_choice == 3:
        num_value = int(input("What is the minumum amount of protein you would like?: "))
        print(sf.find_food_by_min_protein(num_value))

    elif menu_choice == 4:
        num_value = int(input("What is the maximum amount of fat you would like?: "))
        print(sf.find_food_by_max_fat(num_value))

    elif menu_choice == 5:
        num_value = int(input("What is the minimum amount of fat you would like?: "))
        print(sf.find_food_by_min_fat(num_value))
        
    elif menu_choice == 6:
        num_value = int(input("What is the maximum amount of carbs you would like?: "))
        print(sf.find_food_by_max_carbs(num_value))

    elif menu_choice == 7:
        quit()





# Execute main program function call
if __name__ == "__main__":
    main()
