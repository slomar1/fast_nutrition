Project: "Meal-Finder-CLI"
A simple command-line tool to help college students find fast-food options that meet their nutritional goals. This is the "pre-pre-alpha" version, focusing on core logic.


MVP (v0.1)
Goal: Create a command-line program that lets a user define a nutritional target (e.g., "max 600 calories" or "min 30g protein") and searches a small, built-in list of food items to find matches.

V0.1 Roadmap: The "To-Do" List

[✅] Step 1: Project Setup

[✅] Step 2: Define Principle Data Structure

[✅] Step 3: Create a "Mock" Database and Hard-Code it in (Do NOT use an API yet)


[✅] Step 4: Build the Core Search Logic (Start simple: Use Basic Functions

[✅] Step 5: Build the User Interface (CLI. Use simple 'print' and 'input' statements, welcome message, menu options, error handling, etc.)



Database Implementation (v0.2)
Goal: Replace the hard-coded "mock" database with live data from the USDA API. Implement a more powerful search function that lets the user filter by multiple criteria at once.


[ ] Step 1: Integrate the USDA API
  * [ ] Go to https://fdc.nal.usda.gov/api-key-signup.html and sign up for free API key.
  * [ ] Do not paste your API key directly into code. Save it in a separate, simple .env file.
  * [ ] Learn to make an HTTP requests with the Pyhton 'requests' library (import requests)
  * [ ] Create an API handler file.
  * [ ] Create API functions that can take a keyword (like "Chicken Sandwich") as input, build the correct URL to query the USDA API, include  API key in the request, fetch the data, and return the raw JSON response.
  * [ ] Test and Parse the JSON with helper functions that pull out only the data we care about (name, calories, protein, fat, carbs) for each food item. This new function should return a clean list of food objects


[ ] Step 2: Build Advanced Search Logic
  * [ ] Design the filter function. The filters parameter should be a dictionary that holds all the user's criteria, like max calories, min protein, etc.
  * [ ] Write the filter logic: loop through the food_list form API, check it against all the criteria in the filters dictionary, return the final_results list.
  * [ ] Delete  old v0.1 functions like find_food_by_max_calories and find_food_by_min_protein. New filter_food_list function replaces all of them.


[ ] Step 3: Update the CLI User Interface
  * [ ] Change the user flow to be more efficient. Ask for nutritional goals one by one ('Enter max calories (press Enter to skip): ', 'Enter min protein (press Enter to skip): ', etc.)
  * [ ] Use user search term to call your usda search function and show clear, readable results
  * [ ] Neatly print the final, filtered list of foods that match all their criteria.
