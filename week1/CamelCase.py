"""Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

Your task is to write a program that creates or splits Camel Case variable, method, and class names.

Input Format

Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
The operation will either be S (split) or C (combine)
M indicates method, C indicates class, and V indicates variable
In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String. Methods should end with an empty set of parentheses to differentiate them from variable names.
Output Format

For each input line, your program should print either the space-delimited list of words (in the case of a split operation) or the appropriate camel case string (in the case of a combine operation).
Sample Input

S;M;plasticCup()

C;V;mobile phone

C;C;coffee machine

S;C;LargeSoftwareBook

C;M;white sheet of paper

S;V;pictureFrame

Sample Output

plastic cup

mobilePhone

CoffeeMachine

large software book

whiteSheetOfPaper()

picture frame

Explanation

Use Scanner to read in all information as if it were coming from the keyboard.

Print all information to the console using standard output (System.out.print() or System.out.println()).

Outputs must be exact (exact spaces and casing)."""
#import
import sys
#funciones
def readWord(intro):
    resul=intro.split(";")
    return resul
def split_word (words):
    sol=""
    for c in words:
        if c.isupper() and sol:
            sol+=" "
        sol+=c
    return sol.lower()
def lose_brakets(words):
    return words[:-2]
def firstCapitalLetter(word):
    sol=""
    for c in word:
        if not sol:
            sol+=c
            sol=sol.upper()
        else:
            sol+=c
    return sol
def camelCase(word):
    inputStr=readWord(word)
    if inputStr[0]=="S":
        sol1=split_word(inputStr[2])
        if inputStr[1]=='M':
            sol2=lose_brakets(sol1)
        else:
            sol2=sol1
    elif inputStr[0]=="C":
        sol1=inputStr[2].split()
        if inputStr[1]=="M":
            sol2=""
            for word in sol1:
                if not sol2:
                    sol2+=word
                else:
                    sol2+=firstCapitalLetter(word)
            sol2+="()"
        elif inputStr[1]=="C":
            sol2=""
            for word in sol1:
                sol2+=firstCapitalLetter(word)
        if inputStr[1]=="V":
            sol2=""
            for word in sol1:
                if not sol2:
                    sol2+=word
                else:
                    sol2+=firstCapitalLetter(word)
    print(sol2)
#programa
if __name__ == "__main__":
    for line in sys.stdin:
        camelCase(line.strip("\r\n"))