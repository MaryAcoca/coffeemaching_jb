Since we are learning Python, sometimes it might be useful to convert texts from lowerCamelCase to snake_case. The main trick is to find the correct place where to insert an underscore. Let's make a rule that it's right before a capital letter of the next word.

The input format:

Read a word or a phrase written in lowerCamelCase.

The output format:

Print out words in lowercase and separate them by underscores.

Hint

The string methods str.isupper() and str.islower() might come in handy. You can use them to check the case and obtain either True or False value in response.
Sample Input 1:

python
Sample Output 1:

python
Sample Input 2:

parselTongue
Sample Output 2:

parsel_tongue