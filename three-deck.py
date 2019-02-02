import random
import time


#We rank the cards,  such that J=11,  Q=12,  etc.


# We have already established the
#We rank the cards,  such that J=11,  Q=12,  etc.
red_deck = [14, 14, 14, 14, 9, 9, 9, 9, 7, 7, 7, 7]
blue_deck = [13, 13, 13, 13, 11, 11, 11, 11, 6, 6, 6, 6]
black_deck = [12, 12, 12, 12, 10, 10, 10, 10, 8, 8, 8, 8]


#We already know Monte's best responses for each deck choice
decks = [red_deck, blue_deck, black_deck]
responses = [black_deck, red_deck, blue_deck]


#This function plays the game once
def war(decks, responses):


    decks = decks
    responses = responses

    #Player chooses a random deck
    playerchoice = random.randint(0,2)



    #Player's deck selected from list, as well as appropriate response from Monte
    pd = decks[playerchoice]
    md = responses[playerchoice]
    pdd = pd

    mdd = md
    #initialise points and deck size
    p_pts, m_pts = 0, 0
    decksize = 12

    #Play the game, until one player has 5 points upon which they are declared the winner
    while ( (p_pts < 5) and (m_pts < 5) ):



        p_rand = random.randint(0,(decksize - 1))
        m_rand = random.randint(0,(decksize - 1))


        p_card = pdd[p_rand]
        m_card = mdd[m_rand]

        if ( p_card > m_card):
            p_pts += 1
        else:
            m_pts += 1

        #reduce the decksize, and remove drawn cards
        decksize -= 1

        del pdd[p_rand]
        del mdd[m_rand]

    #Return the winner to main()
    if(p_pts > m_pts):
        winner = "player"
        return winner
    else:
        winner = "monte"
        return winner



def main():

    #Set number of loops to perform
    iterations = 1000000
    count, p_wins, m_wins = 0, 0, 0

    while (count < iterations):

        #This if is a progress indicator, for high iteration counts
        if(count % (iterations/10) == 0):
            print("Progress %s%%" % ((count / iterations)*100))

        #call game function war()
        winner = war(decks, responses)

        #Tally up the scores
        if (winner == "player"):
            p_wins += 1
        else:
            m_wins += 1

        count += 1


    print("You won %s games out of %s games. Win probability = %s%%" % (p_wins, iterations, (p_wins/iterations)*100))




#war(decks, responses)
main()
