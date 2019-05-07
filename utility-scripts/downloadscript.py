import argparse
import urllib.request as req
import sys
import os

if __name__ == '__main__':
    url = sys.argv[1]
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('-d', '--destination', default='./{}'.format(os.path.basename(url)), help='The name of the file to store the url in')
    
    args = parser.parse_args()

    req.urlretrieve(args.url, args.destination)