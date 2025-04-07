# Takeaway Early Careers Assignment

## How to run this solution
1. Prerequisites: you need to install Python first. 
2. Pull the project in the desired folder.
3. Since my solution is developed in Python, before running you need to install some packages. Run the command ```pip install requests rich ``` and the packages needed for running main will be downloaded. 
4. Navigate to the folder where the solution is downloaded.
5. Run the command ```python main.py```.

## Implementation documentation
I first started with inspecting the API call's content and observe what the JSON contained. For clarity, I downloaded the JSON file locally and used a code editor to format it. 
Then, I focused on choosing a suitable programming language for this. I debated between using Java and Python, both languages being familiar to me. The reason why I chose to use Python 
is the fact that this assignment is lightweight and for this scope, it was easier to set up. In addition, Python offers quite some flexible packages for displaying the data. 
The other option that I considered was Java and JavaFX for displaying the data, but setting it up would have taken too much time.
Of course, for a more complex project with additional functionalities, Java or Kotlin combined with frameworks like Spring Boot or Hibernate would be more suitable, 
as they simplify the integration between objects and databases.

As seen in my solution, I created a Restaurant class and instantiated it after retrieving the data from the API. 
This approach made it easier to work with the restaurant information in a structured way.
Using objects allowed me to define clear fields,
resulting in more maintainable code compared to using simpler data structures like dictionaries or lists.

## Assumptions 
My first assumption was to consider that all restaurants would have a name, a rating, a complete address and a list of
cuisines. Regarding the address, I observed that the field contains the key "firstLine", which raised a question for me, 
since I would have expected that there would be a field called "secondLine" in the JSON, which was not the case, after 
inspecting the JSON response. Further, I assumed that the minimum rating is 1 star. If the rating is 0, this means that 
the restaurant doesn't have any reviews yet. 

## Improvements
There are multiple things that there could be improved in my solution. First of all, my implementation does not cover 
the case in which one of the fields is empty, as I assumed that name and the address could never be null. Second of all, 
at this moment the result is not sorted in any way, in the sense that the results could be displayed in alphabetical
order, based on the name, based on the rating, from low to high. Moreover, filtering could be done, based on cuisine. 
Lastly, there is no postcode format check. The way I addressed it is by checking if the response returns an empty JSON. 
If the JSON is empty, then it means that there is no restaurant or the postcode is incorrect. Input checking would prevent 
malicious code to be input in the url, increasing the security of the application.

