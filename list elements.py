# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [comment]
def one():
    try:
        #empty list
        name = []
        #inputting data elements
        for x in range(3):
            user = input(' PLS input ur name: ')
            name.append(user)
        #outputting data elements
        for y in range(3):
            print(name[y])
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def two():
    try:
        #empty list
        name = []
        #inputting data elements
        for x in range(3):
            user = input(' PLS input ur name: ')
            name.insert(0,user)
        #outputting data elements
        for user in name:
            print(name)
        pass   
    except Exception as e:
        print("Error occurred:", e )
# [comment]
def three():
    try:
        #empty list
        name = []
        #inputting data elements
        for x in range(3):
            user = input(' PLS input ur name: ')
            name.extend([user,user])
        #outputting data elements
        for user in name:
            print(name)
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
