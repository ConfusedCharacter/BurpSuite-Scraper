# BurpSuite-Scraper
Convert your BurpSuite XML to Programming Language fast !

![pic](https://raw.githubusercontent.com/ConfusedCharacter/BurpSuite-Scraper/main/shot/1.png)

## Overview
The BurpSuite Request Converter is a powerful tool that allows you to convert BurpSuite requests to various programming languages' code snippets. This tool saves time and effort when transferring requests from BurpSuite to your preferred programming language, making it easy to integrate requests into your automation scripts and projects.

## Features
1. BurpSuite Integration: Easily import requests from BurpSuite into the converter.
2. Supported Programming Languages: Convert requests to code snippets in popular programming languages such as Python, PHP.
3. Easy-to-Use: The converter has a simple and intuitive interface, making it user-friendly for both beginners and experienced developers.
4. You can see the responses as comments in your code with `-c` argument.
5. If the output is `json`, it will automatically be `pretty`.

## Usage
1. Start by launching the BurpSuite application.
2. Export your requests from BurpSuite.
 <img src="https://raw.githubusercontent.com/ConfusedCharacter/BurpSuite-Scraper/main/shot/2.png" alt="pic" width="400">

4. Run script and choose the programming language you want to convert the request to.
5. Copy the generated code snippet and integrate it into your project.
6. Result:
<img src="https://raw.githubusercontent.com/ConfusedCharacter/BurpSuite-Scraper/main/shot/3.png" alt="pic" width="350">

## guide

```bash
usage: burpscrapper [-h] [-f FILE] [-c COMMENT] [-l LANGUAGE] [-o OUTPUT]

[BurpSuite Scraper v1.1] Convert BrupSuite
"XML" to programming language.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input BurpSuite XML File to convert
  -c COMMENT, --comment COMMENT
                        Comment Response data
  -l LANGUAGE, --language LANGUAGE
                        Input language: python,php
  -o OUTPUT, --output OUTPUT
                        Output file after convert
```
Example:
```bash
python3 burpscrapper.py -f test/timeir.xml -o test/php_result.php -l php
```
- [output example](https://raw.githubusercontent.com/ConfusedCharacter/BurpSuite-Scraper/main/test/php_result.php)
## Add to Bash!
You can download the executable file and place it in the bash path to use this tool more easily
download it with wget
```bash
wget ......
```

copy executable file to `/usr/bin/`
```bash
sudo cp burpscraper /usr/bin/
```
or you can make executable with `pyinstaller` and put it in `/usr/bin/`
## Supported Programming Languages
- Python
- PHP


## Contribute to Our Project!

We wholeheartedly welcome you to join our project and contribute your invaluable skills and expertise. Together, we can create an outstanding collaboration and bring exciting innovation and features to this project.

Whether you're an experienced developer or new to the field, your ideas are fundamental to our growth. We truly believe that innovation thrives in a diverse and inclusive community - so come as you are, with all your creative ideas!

### Why Contribute?

By contributing to our project, you'll not only enhance your skills and gain practical knowledge, but you'll also have the chance to work alongside a team of talented individuals who are passionate about building something remarkable. Your contributions, big or small, can make a significant impact on the project's success.

### How to Contribute?

Contributing to our project is a breeze. Here's a step-by-step guide to get you started:

1. Fork this repository and clone it to your local machine.
2. Create a new branch with a descriptive name that reflects the nature of your contribution.
3. Make the necessary changes or enhancements to the codebase.
4. Commit your changes and push them to your forked repository.
5. Submit a Pull Request (PR) with a clear description of the changes you've made. Don't forget to mention any related issues you resolved or features you added.
