import argparse
import multiprocessing
import requests
import sys
import threading
import json

def geturl(url):
    r = requests.get("http://web.archive.org/cdx/search/cdx?url="+args.url+"/*&output=json&collapse=urlkey")


    for urls in r.json():
        if urls[2] == 'original':
            continue
        print(urls[2])




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url", metavar='',type=str, help='domain')
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    try:
        geturl(args.url)
        # x = threading.Thread(target=geturl, args=(args.url,))
        # x.start()
    # threading or multiprocessing?    
    except Exception as e:
        pass
