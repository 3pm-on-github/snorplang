import argparse
import random
from argparse import ArgumentParser
VERSION = "0.0.01A"

def run(filecontent):
    for line in filecontent.splitlines():
        if line.startswith("snorp(") and line.endswith(")"):
            content = line.removeprefix("snorp(").removesuffix(")")
            if content.startswith("\"") and content.endswith("\""):
                print(content.removeprefix("\"").removesuffix("\""))
            elif content.startswith("'") and content.endswith("'"):
                print(content.removeprefix("'").removesuffix("'"))
            elif content.startswith("\"") and content.endswith("'"):
                print("you are a monster")
            elif content.startswith("'") and content.endswith("\""):
                print("you are a monster")
        else:
            print(f"what the fuck does \"{line}\" mean")

def main():
    print("snorplang v0.0.01A by 3pm")
    if random.randint(1, 100) == 56:
        print("you won the useless prize of having a 1% chance of seeing this message")
    argparser = ArgumentParser()
    argparser.add_argument("filename")
    args = argparser.parse_args()
    filename = args.filename
    if filename.endswith(".py"):
        print("thats a python file dumbass")
    else:
        try:
            with open(filename, "r") as file:
                run(file.read())
        except FileNotFoundError:
            print("did u imagine the file name because the file doesnt exist")

if __name__ == "__main__":
    main()