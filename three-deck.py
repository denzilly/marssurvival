import random
import time


#We rank the cards,  such that J=11,  Q=12,  etc.


# We have already established the
#We rank the cards,  such that J=11,  Q=12,  etc.
red_deck = [14, 14, 14, 14, 9, 9, 9, 9, 7, 7, 7, 7]
blue_deck = [13, 13, 13, 13, 11, 11, 11, 11, 6, 6, 6, 6]
black_deck = [12, 12, 12, 12, 10, 10, 10, 10, 8, 8, 8, 8]

decks = [red_deck, blue_deck, black_deck]

responses = [black_deck, red_deck, blue_deck]



def play(decks, responses):

    decks = decks
    responses = responses

    playerchoice = random.randint(0,2)

    playerdeck = decks[playerchoice]
    montedeck = responses[playerchoice]

    war(playerdeck, montedeck)


def war(playerdeck, montedeck)

    pd = playerdeck
    md = montedeck

    p_pts, m_pts = 0, 0

    while ( (p_pts < 5) | (m_pts < 5) ):

        p_card = pd[random.randint(0,11)]
        m_card = md[random.randint(0,11)]

        if ( p_card > m_card):
            p_pts += 1
            print("Your %s beats Monte's %s. Score is P%s-M%s.") % (p_card, m_card, p_pts, m_pts)
        else:
            m_pts += 1
            print("Your %s loses to Monte's %s. Score is P%s-M%s.") % (p_card, m_card, p_pts, m_pts)

        input("enter to continue")
