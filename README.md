# orbit
An advanced web fuzzing tool

## DISCLAIMER 
```
DO NOT MISUSE THIS
I WILL NOT BE RESPONSIBLE FOR ANY HARM CAUSED BY THIS
THIS IS JUST FOR EDUCATIONAL PURPOSE
IF YOU ARE TRYING THIS, MAKE SURE YOU HAVE THE PERMISSION OF THE VICTIM MACHINE's OWNER
```

### **USAGE**
1. Compulsory Arguments
```
MODE          What mode do you want to use. (dir/vhost)  <for now only dir is supported, vhost comming soon>
-u  URL       Target URL with the 'ORBIT' keyword. (Plcae 'ORBIT' where the actual fuzzing needs to be done)
                        Eg: http://example.com/ORBIT/
-w WORDLIST   Path of the wordlist to be used.
```
2. Optional Arguments
```
-t THREADS    No of threads to be used. (default = 5)
-exc-code [RESPONSE CODES TO EXCLUDE]     (default = 404)
              Response codes to exclude. (Seperated by spaces)
              Eg: -exc-code 404 403 500
-inc-code [RESPONSE CODE TO INCLUDE]      (default = all codes except 404)
              Response codes to include. (Seperated by spaces)
              Eg: -inc-code 200
-exc-wc [WORD COUNT TO EXCLUDE]
              Exclude responses with some specific word count. (Seperated by spaces)
              Eg: -exc-wc 118
-inc-wc [WORD COUNT TO INCLUDE]
              Include responses with some specific word count. (Seperated by spaces)
              Eg: -inc-wc 15
-exc-cc [CHARACTER COUNT TO EXCLUDE]
              Exclude responses with some specific character count. (Seperated by spaces)
              Eg: -exc-cc 118
-inc-cc [CHARACTER COUNT TO INCLUDE]
              Include responses with some specific character count. (Seperated by spaces)
              Eg: -inc-cc 118
```

### **EXAMPLES**
```
[1] python orbit.py dir -u http://example.com/ORBIT -w /path/to/wordlist 

[2] python orbit.py dir -u http://example.com/ORBIT -w /path/to/wordlist -inc-code 200 -exc-wc 100
```
