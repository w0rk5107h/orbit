import requests
import os
import argparse
import _thread
from bs4 import BeautifulSoup
import re

# to clear the console
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# to get the text from raw HTML
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

# to bruteforce the dirs
def start_dir(URL, WORDS, THREADS, EXC_CODE, INC_CODE, EXC_WC, INC_WC, EXC_CC, INC_CC, THREAD):
    for i in range(THREAD, len(WORDS), THREADS):
        URL = URL.replace('ORBIT', WORDS[i])
        URL = URL.replace(WORDS[i-THREADS], WORDS[i])
        # print(f'Thread {THREAD} sending request to {WORDS[i]}') # log
        r = requests.get(URL)
        STATUS_CODE = r.status_code
        WORD_COUNT = int
        CHAR_COUNT = int
        raw_html = r.text
        raw_html = BeautifulSoup(raw_html, features='lxml')
        for body in raw_html.find_all('body'):
            text = cleanhtml(str(body))
            WORD_COUNT = len(text.split())
            CHAR_COUNT = len(text)

        # on the basis of status code
        if STATUS_CODE in INC_CODE and STATUS_CODE not in EXC_CODE:

            # on the basis of word count
            if len(INC_WC) > 0 and len(EXC_WC) > 0:
                if WORD_COUNT in INC_WC and WORD_COUNT not in EXC_WC:

                    # on the basis of char count
                    if len(INC_CC) > 0 and len(EXC_CC) > 0:
                        if CHAR_COUNT in INC_CC and CHAR_COUNT not in EXC_CC:
                            print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                        else:
                            pass
                    elif len(INC_CC) > 0 or len(EXC_CC) > 0:
                        if len(INC_CC) > 0:
                            if CHAR_COUNT in INC_CC:
                                print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                            else:
                                pass
                        elif len(EXC_CC) > 0:
                            if CHAR_COUNT in EXC_CC:
                                pass
                            else:
                                print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                    else:
                        print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")                    
                else:
                    pass
            elif len(INC_WC) > 0 or len(EXC_WC) > 0:
                if len(INC_WC) > 0:
                    if WORD_COUNT in INC_WC:
                        
                        # on the basis of char count
                        if len(INC_CC) > 0 and len(EXC_CC) > 0:
                            if CHAR_COUNT in INC_CC and CHAR_COUNT not in EXC_CC:
                                print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                            else:
                                pass
                        elif len(INC_CC) > 0 or len(EXC_CC) > 0:
                            if len(INC_CC) > 0:
                                if CHAR_COUNT in INC_CC:
                                    print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                                else:
                                    pass
                            elif len(EXC_CC) > 0:
                                if CHAR_COUNT in EXC_CC:
                                    pass
                                else:
                                    print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                        else:
                            print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")                        
                    else:
                        pass
                elif len(EXC_WC) > 0:
                    if WORD_COUNT in EXC_WC:
                        pass
                    else:

                        # on the basis of char count
                        if len(INC_CC) > 0 and len(EXC_CC) > 0:
                            if CHAR_COUNT in INC_CC and CHAR_COUNT not in EXC_CC:
                                print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                            else:
                                pass
                        elif len(INC_CC) > 0 or len(EXC_CC) > 0:
                            if len(INC_CC) > 0:
                                if CHAR_COUNT in INC_CC:
                                    print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                                else:
                                    pass
                            elif len(EXC_CC) > 0:
                                if CHAR_COUNT in EXC_CC:
                                    pass
                                else:
                                    print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                        else:
                            print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
            else:

                # on the basis of char count
                if len(INC_CC) > 0 and len(EXC_CC) > 0:
                    if CHAR_COUNT in INC_CC and CHAR_COUNT not in EXC_CC:
                        print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                    else:
                        pass
                elif len(INC_CC) > 0 or len(EXC_CC) > 0:
                    if len(INC_CC) > 0:
                        if CHAR_COUNT in INC_CC:
                            print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                        else:
                            pass
                    elif len(EXC_CC) > 0:
                        if CHAR_COUNT in EXC_CC:
                            pass
                        else:
                            print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
                else:
                    print(f"Found: /{WORDS[i]}, Status: {STATUS_CODE}, WC: {WORD_COUNT}, CC: {CHAR_COUNT}")
        else:
            pass

if __name__ == '__main__':
    try:
        clear()

        # cmd line args
        parser = argparse.ArgumentParser(description='AN ADVANCED WEB FUZZING TOOL')
        parser.add_argument('MODE', type=str, choices=['dir', 'vhost'], help='What do you want to fuzz. (dir/vhost)')
        parser.add_argument('-u', type=str, required=True, help='URL that you want to fuzz, with the "ORBIT" keyword included. (read README.md for more)', metavar='URL')
        parser.add_argument('-w', type=str, required=True, help='Path of the wordlist to be used.', metavar='WORDLIST')
        # parser.add_argument('-o', type=str, help='Path to the outfile', metavar='OUTFILE')
        parser.add_argument('-t', type=int, help='Number of threads to use', metavar='THREADS')
        parser.add_argument('-exc-code', type=int, help='Response codes to exclude. (seperated by spaces)', metavar='RESPONSE CODES TO EXCLUDE', nargs='*')
        parser.add_argument('-inc-code', type=int, help='Response codes to include. (seperated by spaces)', metavar='RESPONSE CODES TO INCLUDE', nargs='*')
        parser.add_argument('-exc-wc', type=int, help='Exclude the responses with some specific word count. (seperated by spaces)', metavar='WORD COUNT TO EXCLUDE', nargs='*')
        parser.add_argument('-inc-wc', type=int, help='Include the responses with some specific word count. (seperated by spaces)', metavar='WORD COUNT TO INCLUDE', nargs='*')
        parser.add_argument('-exc-cc', type=int, help='Exclude the responses with some specific character count. (seperated by spaces)', metavar='CHARACTER COUNT TO EXCLUDE', nargs='*')
        parser.add_argument('-inc-cc', type=int, help='Include the responses with some specific character count. (seperated by spaces)', metavar='CHARACTER COUNT TO INCLUDE', nargs='*')
        args = parser.parse_args()

        # if dir mode
        if args.MODE == 'dir':

            # URL
            URL = args.u
            if URL.find('ORBIT') != -1:
                pass
            else:
                print('\'ORBIT\' keyword not found !!! \nRefer to --help. ')
                exit()

            # wordlist
            WORDLIST = args.w
            f = open(WORDLIST)
            WORDS = []
            while True:
                WORD = f.readline()
                if WORD == '':
                    break
                WORD = WORD.rstrip()
                WORDS.append(WORD)
            
            # output to a file
            # will see later

            # no of threads
            THREADS = int
            if args.t:
                THREADS = args.t
            else:
                THREADS = 10
            
            # exclude code
            EXC_CODE = []
            if args.exc_code:
                EXC_CODE = args.exc_code
            else:
                EXC_CODE = [404]

            # include code
            INC_CODE = []
            if args.inc_code:
                INC_CODE = args.inc_code
            else:
                INC_CODE = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 306, 307, 308, 400, 401, 402, 403, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 427, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
                # INC_CODE = True

            # exclude word count
            EXC_WC = []
            if args.exc_wc:
                EXC_WC = args.exc_wc
            else:
                pass

            # include word count
            INC_WC = []
            if args.inc_wc:
                INC_WC = args.inc_wc
            else:
                pass

            # exclude char count
            EXC_CC = []
            if args.exc_cc:
                EXC_CC = args.exc_cc
            else:
                pass

            # include char count
            INC_CC = []
            if args.inc_cc:
                INC_CC = args.inc_cc
            else:
                pass

            # start brute force
            # for THREAD in range(0, THREADS):
            #     _thread.start_new_thread(start_dir,(URL, WORDS, THREADS, EXC_CODE, INC_CODE, EXC_WC, INC_WC, EXC_CC, INC_CC, THREAD))

            # test
            start_dir(URL,WORDS,1,EXC_CODE, INC_CODE, EXC_WC, INC_WC, EXC_CC, INC_CC, 0)
    except KeyboardInterrupt:
        print('Stopping....')