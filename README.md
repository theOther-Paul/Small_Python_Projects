# Small_Python_projects

This repo contains some basic terminal programs that helped me understand various concepts such as:

- enums;
- dictionaries
- display rules
- classes
- superclasses
- writing functional and clean code
- refactoring each non-scalable function

##Project structure and brief explanation
### Box-drawing Menu:

- creates an adaptive menu using the box drawing unicode characters
- have a list of dictionaries as input and splits the dictionaries into columns

###Temperature Convertor:

- converts a given temperature between 0K and 1K from any scale into any scale
- was constructed using a data class and a class, using a dictionary to remember each scale and limit equivalents
- receives as input 3 parameters: the temperature value, the scale in which the temperature is written and the scale the
  user want the value to be converted to

### Product Management System:

- a work in progress project
- after the development is done, this project will have a console menu for the user to input a base file and to run some menu option to add or remove various characteristics of a product
- is constructed using only classes to read from a base file, add prices to raw product identifiers and modify other characteristics such as name and description
- will have a method to set up a backup file, should the situation need it
