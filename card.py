# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [comment]
def one():
    try:
        import random

        card = ['Jack','Queen','King','Ace']
        #shuffling card
        random.shuffle(card)
        print(card)
        #choosing card
        play= random.choice(card)
        print(play)
        #sort card
        card.sort()
        print(card)
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def two():
    try:
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def main():
    try:
        one()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
