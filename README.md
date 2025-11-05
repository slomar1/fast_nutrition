Project: "Meal-Finder-CLI"

A simple command-line tool to help college students find fast-food options that meet their nutritional goals. This is the "pre-pre-alpha" version, focusing on core logic.


MVP Goal (Version 0.1)
Create a command-line program that lets a user define a nutritional target (e.g., "max 600 calories" or "min 30g protein") and searches a small, built-in list of food items to find matches.



V0.1 Roadmap: The "To-Do" List

[✅] Step 1: Project Setup
[✅] Decide on a programming language (Python or Node.js are great choices).
[✅] Create your main project folder.
[✅] Create this `README.md` file.
[✅] Create your main script file (e.g., `main.py` or `index.js`).


[ ] Step 2: Define Your Data Structure (How will you represent a single food item?)
Goal: Decide on a simple structure. A dictionary in Python is perfect.
Example:
    {
      "name": "Chicken Burrito Bowl",
      "restaurant": "Chipotle",
      "calories": 650,
      "protein_g": 40,
      "fat_g": 20,
      "carbs_g": 75
    }


[ ] Step 3: Create a "Mock" Database (Do NOT use an API yet)
Goal: Create a simple list or array containing 5-10 of your food item objects (from Step 2).
[ ] Hard-code this list directly into your script file for now. This is your "database" for the MVP.


[ ] Step 4: Build the Core Search Logic (Start simple: Write a function called `find_food_by_max_calories(max_cals)`.)
Goal: Write a function that takes the user's criteria and your list of food as input.
[To-Do] This function should:
    * Loop through your hard-coded list.
    * Check if an item's `calories` are less than or equal to `max_cals`.
    * If it is, add it to a `results` list.
    * Return the `results` list.
Goal: Write a function called `find_food_by_min_protein(min_protein)`.
* [To-Do] This function should:
    * Loop through your hard-coded list.
    * Check if an item's `protein_g` is greater than or equal to `min_protein`.
    * If it is, add it to a `results` list.
    * Return the `results` list.


[ ] Step 5: Build the User Interface (CLI)
Goal: Use simple `print` and `input` statements to interact with the user.
[ ] Print a welcome message.
[ ] Ask the user *what* they want to search for (e.g., "1 for calories", "2 for protein").
[ ] Ask the user for their target value (e.g., "Enter max calories:").
[ ] Call the correct search function (from Step 4) based on their input.
[ ] Print the results in a clean, readable format.
[ ] Add a loop so the program runs again until the user types "exit".



Future Goals (V0.2 and Beyond)

Once you've finished the V0.1 to-do list, *then* you can start on these harder features.

[ ] Integrate the USDA API:
  * [ ] Learn how to get an API key for the USDA FoodData Central.
  * [ ] Learn how to make an HTTP request (e.g., using `requests` in Python or `fetch` in Node.js).
  * [ ] Replace your "Mock Database" with live calls to the API.
[ ] Improve Search: Allow the user to combine searches (e.g., "max 600 calories" *AND* "min 30g protein").
[ ] Web Version: Convert the project from a CLI tool to a simple website using Flask, Django, or Express.