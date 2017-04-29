import requests
import argparse
from pyquery import PyQuery as pq

url = 'https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data#ed-firms-firemap'
	
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputCSV', type=str, help='the file to store CSV data')
args = parser.parse_args()

def getFireCSV():
	
	response = requests.get(url)
	if response.status_code != 200:
		print 'get web error : ' + response.status_code
	doc = pq(response.content)
	csvUrl = doc('.eui-accordion__body').eq(2).children('table').eq(0).children('tbody').eq(0).children('tr').eq(0).children('td').eq(2).children('a').eq(2).attr('href')
	print 'start getting csv file from web...'
	r = requests.get(csvUrl)
	
	with open(args.outputCSV, "w") as file:
		file.write(r.content)


def main():
	getFireCSV()	


if __name__ == '__main__':
	main()