import requests
from bs4 import BeautifulSoup
import pickle
from os import listdir, remove

def scape_and_pickle_hands():
	resp = requests.get('https://www.tightpoker.com/poker_hands.html')
	soup = BeautifulSoup(resp.content, 'html.parser')

	hands = []

	for tr in soup.findAll('tr'):
		hands.append(str(tr).split('\n'))

	hands.pop(0)

	if 'Hands.pickle' in listdir():
		remove('Hands.pickle')

	with open('Hands.pickle', 'wb') as pickle_out:
		pickle.dump(hands,pickle_out)
		print('File successfully Pickled')

def modify_data(data = 'Hands.pickle'):

	with open(data, 'rb') as pickle_in:
		hands = pickle.load(pickle_in)

	for i in range(len(hands)):
		del hands[i][0]
		del hands[i][2:]

		#Just getting rid of all the html. I know it's not the best way!
		#TODO: make this in regular expressions, kinda a hack right now.
		hands[i][0] = hands[i][0].split(">")[1].split("<")[0]
		hands[i][1] = hands[i][1].split(">")[1].split("<")[0]
		
		#If they are the same suit (s at the end of the cards) The 's' will be removed. All list 
		#items not have a boolean at index 3 to indicate whether they are the same suit
		hands[i].append(not hands[i][0] == hands[i][0].split(" ")[0])
		hands[i][0] = hands[i][0].split(" ")[0]

	del hands[hands.index(['Cards', 'EV', False])]
	del hands[hands.index(['Cards', 'EV', False])]

	if 'Hands.pickle' in listdir():
		remove('Hands.pickle')

	#Making sure all the EVs are > 0, and rounded to 2 decimal places
	for i in range(len(hands)):
		hands[i][1] = round(float(hands[i][1])+.16, 2)

	with open('Hands.pickle', 'wb') as pickle_out:
		pickle.dump(hands,pickle_out)
		print('File successfully Pickled')

	return hands

def main():
	#Uncomment this line if you want to scrape the web for the data
	# scape_and_pickle_hands()

	#make sure that the data going into this function is directly from the web otherwise it will throw an error
	print(modify_data())

if __name__ == '__main__':
	main()
