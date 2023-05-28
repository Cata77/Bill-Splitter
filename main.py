import random

number_of_friends = int(input("Enter the number of friends joining (including you):\n"))

if number_of_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends_dict = {}
    for i in range(number_of_friends):
        name = input()
        friends_dict[name] = 0
    total_bill = int(input("\nEnter the total bill value:\n"))
    option = input('\nDo you want to use the "Who is lucky" feature? Write Yes/No:\n')
    if option == "No":
        bill_split = round(total_bill / number_of_friends, 2)
        friends_dict = dict.fromkeys(friends_dict, bill_split)
        print("\nNo one is going to be lucky")
    else:
        lucky_friend = random.choice(list(friends_dict.keys()))
        print("\n{} is the lucky one!".format(lucky_friend))
        bill_split = round(total_bill / (number_of_friends - 1), 2)
        for i in friends_dict:
            if i != lucky_friend:
                friends_dict[i] = bill_split
    print(friends_dict)
