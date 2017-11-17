# battle
This programm produce a 120 sec battle.
From the list of 1000 players (pull.txt) are randomly chosen 200 players, each player get a 'power'-characteristic randomly
from the range (1,1000) and gets 1000 medals in the beginning of the battle. Players are sorted by power and devided in 4 groups 
of 50 players (first 50, second 50,...).Then the battle (24 five-second rounds) in every group starts.
The description of the round is written below.

At the beginning all players in group are mixed. Then every player gets an 'agressor'-characteristic (1 0r 0 randomly, i.e.agressor or not).
Starting from the top of the agressor-list every agressor (if he was not chosen as a victim) gets a victim (rules are the following:
victim can be chosed only once in the round and only once for each agressor, player cannot fight himself, every player should be an
agressorat least once in the battle). Agressor attacks his victim: an integer from -10 to +10 is chosen randomly and is added
to medals-number of the agressor and substractedfrom medals-number of the victim.

After the 24th round all the players in each group are sorted by medals and the winners get 'money':
1st place -- +300,
2nd place -- +200,
3rd place --+100.

The winners in every group are showed out.
