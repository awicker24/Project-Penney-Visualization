## Heatmap code to work on
### starting with group 1 (since it takes in an array)

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
import os
import json
import matplotlib.ticker as mtick

#initialize
card_wins_matrix = np.zeros((8,8))
trick_wins_matrix = np.zeros((8,8))
#print(card_wins_matrix)
#print(trick_wins_matrix)

#fill
i = 0
for x in range(8):
    for z in range(8):
        card_wins_matrix[x,z] = i
        trick_wins_matrix[x,z] = 64-i
        i+=1

#print(card_wins_matrix)
#print()
#print(trick_wins_matrix)

#save
np.save("card_wins.npy",card_wins_matrix)
np.save("trick_wins.npy",trick_wins_matrix)

sequences = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']
def create_heatmaps(num_cards = num_cards_result, num_tricks = num_tricks_result):

    if not os.path.exists('figures'):
        os.makedirs('figures')
       
    #Heatmap for number of cards
    plt.figure(figsize=(10,8))
    sns.heatmap(num_cards,
                annot=True,
                fmt = '.2%',
                annot_kws={'color': 'black'},
                cmap=LinearSegmentedColormap.from_list('rg',["r", "w", "g"], N=256),
                linewidths=.5,
                cbar_kws={'label': 'Win Probability', 'format': mtick.PercentFormatter(xmax=1, decimals=0)})
    plt.title('Win Probabilities for Card Scoring')
    plt.xlabel('Player 2 Choice')
    plt.ylabel('Player 1 Choice')
    plt.savefig('figures/num_card_probs.png', bbox_inches = 'tight')

    #Heatmap for number of tricks
    plt.figure(figsize=(10,8))
    sns.heatmap(num_tricks,
                annot=True,
                fmt = '.2%',
                annot_kws={'color': 'black'},
                cmap=LinearSegmentedColormap.from_list('rg',["r", "w", "g"], N=256),
                linewidths=.5,
                cbar_kws={'label': 'Win Probability', 'format': mtick.PercentFormatter(xmax=1, decimals=0)})
    plt.title('Win Probabilities for Trick Scoring')
    plt.xlabel('Player 2 Choice')
    plt.ylabel('Player 1 Choice')
    plt.savefig('figures/num_trick_probs.png', bbox_inches = 'tight')

if __name__ == "__main__":
    create_heatmaps()
