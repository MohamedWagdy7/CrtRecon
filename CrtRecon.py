from sys import argv
from requests import get
from re import findall,match,sub
from termcolor import colored

def extractAlters(content,word):
    ids = set(findall('\?id=(\d+)',content))
    alters = []
    for id in ids:
        content=str(get(f"https://crt.sh/?id={id}").content)
        alters= list(set(findall(rf"DNS:((([A-Za-z0-9\-]+\.)+)?{word}\.\w+)",content)))
    return alters

def extractSubs(content):
    filteredResponse = findall('(?:<TD>)(.*?)</TD>', content)
    filteredResponse.extend(findall('(?:BR>)(.*?)<', content))
    return filteredResponse

if len(argv) < 3:
    print(colored("USAGE: crt <domain> <output_dir>","red"))
    exit()
    
if __name__ == '__main__':
    domain = argv[1]
    word = domain.split(".")[-2]
    content1 = str(get(f'https://crt.sh/?q=%25.{domain}').content)
    content2 = str(get(f'https://crt.sh/?q={word}.%25'))
    subs = extractSubs(content1)
    subs.extend(extractSubs(content2))
    with open(f"{argv[2]}/{domain}.txt","a") as f:
        for i in list(set(subs)):
            if match("<A.*",i) or match("It is not.*",i) or "@" in i or " " in i or i==None:
                continue
            f.write(sub(r"\\.*","",i).replace("<BR>","\n")+"\n")
        for id in extractAlters(content1,word):
            f.write(id[0]+"\n")
        for id in extractAlters(content2,word):
            f.write(id[0]+"\n")