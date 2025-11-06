# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [Removing items from lists]
def one():
    try:
        names = ['mon','tues','wed','thur','frid','sat','sun']

        #removing an item
        names.remove('mon')
        print(names)
        #deleting an item from a position
        del names[0]
        print(names)
        #deleting an item from a position
        names.pop(0)
        print(names)
        #deleting an item from a position
        names.clear()
        print(names)
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
