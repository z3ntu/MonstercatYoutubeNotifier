#!/usr/bin/python3

import os


def main():
    template_file = open("config.DEFAULT.py", "r")
    config = open("config.py", "w")

    template = template_file.read()
    template = template.replace("api_key=\"\"", "api_key=\""+os.environ['API_KEY']+"\"")

    config.write(template)

if __name__ == '__main__':
    main()
