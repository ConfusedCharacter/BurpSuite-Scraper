# !/usr/bin/python3
# BurpSuite Scraper v1.1
# By ConfusedCharacter

from xml.etree import ElementTree
from typing import NamedTuple
import argparse
import base64
import json

__version__ = 1.1

class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

class ExtractedData(NamedTuple):
    responselength  : int
    burpFile        : str
    response        : str
    request         : str
    method          : str
    status          : int
    time            : str
    url             : str


def extract_burp_data(xml_file:str):
    tree = ElementTree.parse(xml_file)              # Reading Burpsuite xml file.
    root = tree.getroot()
    root = root[0]
    responselength = None
    time_created = None
    response = None
    request = None
    method = None
    status = None
    url = None

    for element in root:
        tag,text = element.tag,element.text         # Getting TAG, TEXT from xml attributes.
        if tag == "responselength":
            responselength = int(text)
        elif tag == "response":
            response = text
        elif tag == "status":
            status = int(text)
        elif tag == "request":
            request = text
        elif tag == "time":
            time_created = text
        elif tag == "method":
            method = text.lower()
        elif tag == "url":
            url = text


    return ExtractedData(   
        responselength=responselength,
        response=response,
        burpFile=xml_file,
        time=time_created,
        request=request,
        method=method,
        status=status,
        url=url
    )

def add_comments(extracted:ExtractedData):
    source = ""
    source += "# !/usr/bin/python3\n"                                       # Source Comments.
    source += "# BurpSuite Scraper v{}\n".format(__version__)
    source += "# By ConfusedCharacter\n\n"
    source += "# BurpSuite Filename: \"{}\"\n".format(extracted.burpFile)
    source += "# Time: \"{}\"\n".format(extracted.time)
    source += "# Request url: \"{}\"\n".format(extracted.url)
    source += "# Request method: \"{}\"\n".format(extracted.method.upper())
    source += "# Request status: \"{}\"\n".format(extracted.status)
    source += "# Base64 Raw Request: {}\n".format(extracted.request)
    source += "# Base64 Raw Response: {}\n\n".format(extracted.response)
    return source

def convert_to_py(extracted:ExtractedData,comment_response_data:bool = False):
    source = add_comments(extracted)                                        # Add init comments to source.
    source += "import requests\n\n"
    source += "def MyRequest():\n\t"

    request = base64.b64decode(extracted.request.encode()).decode()         # Decoding base64 raw request data.
    response = base64.b64decode(extracted.response.encode()).decode()       # Decoding base64 raw response data.
    
    response = response.splitlines()
    request = request.splitlines()
    if request[-1] == "":                                                   # To define whether the request has data or not.
        request_data = False
    else:
        request_data = True
    
    if response[-1] == "":                                                  # To define whether the response has data or not.
        response_data = False
    else:
        response_data = True

    request = request[2:]                                                   # Ignore Method, path and Host. example: "GET /json/ HTTP/1.1\nHost: www.google.com...".
    
    source += "headers = {\n\t\t"
    for header in request:
        if header == "":                                                    # Stop for loop if reach to request data.
            break
        else:
            if ":" not in header:                                           # Continue if string is not header.
                continue
            else:
                key,value = header.split(": ")
                source += "'{}': '{}',\n\t\t".format(key,value)             # Adding header "key" and "value"

    source += "}\n\t"                                                       # Finish adding header.

    source += "response = requests.{}(\n\t\t".format(extracted.method)      # make request
    source += "url='{}',\n\t\t".format(extracted.url)
    source += "headers=headers,\n\t\t"

    if request_data and extracted.method == "post":
        data = "\n".join(request[request.index("") + 1:])
        source += "data='{}'\n\t)\n\n\t".format(data)
    else:
        source += ")\n\n\t"

    source += "return response\n\n\t"
    if comment_response_data:                                               # Add post data if available.
        if response_data:
            response_raw = "\n".join(response[response.index("") + 1:])
            try:
                load_json = json.loads(response_raw)
                pretty_json = json.dumps(load_json,indent=4)
                pretty_json = pretty_json.splitlines()
                comment_json = "\n".join(list(map(lambda line: "\t# "+line,pretty_json)))
                source += "# Response:\n"
                source += comment_json
            except:
                source += "# Response: {}\n".format(response_raw)
        else:
            source += "# Response: None\n"


    return source

def convert_to_php(extracted:ExtractedData,comment_response_data:bool = False):
    pass


if __name__ == "__main__":
    # set Windows console in VT mode
    if __import__("platform").system() == "Windows":
        kernel32 = __import__("ctypes").windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        del kernel32
    
    print(f"""{Colors.LIGHT_RED}
  ____                   _____                                
 |  _ \                 / ____|                               
 | |_) |_   _ _ __ _ __| (___   ___ _ __ __ _ _ __   ___ _ __ 
 |  _ <| | | | '__| '_ \\___ \ / __| '__/ _` | '_ \ / _ \ '__|
 | |_) | |_| | |  | |_) |___) | (__| | | (_| | |_) |  __/ |   
 |____/ \__,_|_|  | .__/_____/ \___|_|  \__,_| .__/ \___|_|   
                  | |                        | |              
                  |_|                        |_|              
                  
                    By {Colors.BLUE}"ConfusedCharacter"
                    
{Colors.END}""")
    parser = argparse.ArgumentParser(description=f'[{Colors.BLUE}BurpSuite Scraper{Colors.END} {Colors.CYAN}v{__version__}{Colors.END}] Convert {Colors.YELLOW}BrupSuite{Colors.END} "XML" to programming language.')
    parser.add_argument('-f', '--file', help='Input BurpSuite XML File to convert')
    parser.add_argument('-c', '--comment', help='Comment Response data',default=False)
    parser.add_argument('-l', '--language', help=f'Input language: {Colors.YELLOW}python{Colors.END},{Colors.YELLOW}php{Colors.END}',default="python")
    parser.add_argument('-o', '--output', help='Output file after convert',default="BurpScraper_result.py")
    args = parser.parse_args()

    if args.file:
        extracted = extract_burp_data(args.file)
        print(f"[{Colors.GREEN}+{Colors.END}] Reading \"{args.file}\"...")
        if args.language.lower() == "python":
            source = convert_to_py(extracted,comment_response_data=args.comment)
            print(f"[{Colors.GREEN}+{Colors.END}] Converting to \"Python\"...")
        elif args.language.lower() == "python":
            source = convert_to_py(extracted,comment_response_data=args.comment)
            print(f"[{Colors.GREEN}+{Colors.END}] Converting to \"PHP\"...")

        with open(args.output,"w") as file:
            file.write(source)
            file.close()

        print(f"[{Colors.GREEN}+{Colors.END}] Sucess. Saved to \"{args.output}\"...")
        
    