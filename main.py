from game_data import data
import art
import random



def compare():
    point = 0
    acct_1 = random.choice(data)
    acct_2 = random.choice(data)
    while True:
        while acct_2 == acct_1:
            acct_2 = random.choice(data)

        print(art.logo)
        print(f'''Compare A: {acct_1["name"], acct_1["description"], acct_1["country"]} 
        \n {art.vs} 
        \nCompare B: {acct_2["name"], acct_2["description"], acct_2["country"]}''')

        u_guess = input(f"Who has more followers 'A' or 'B'")
        acct_1_follower = acct_1["follower_count"]
        acct_2_follower = acct_2["follower_count"]

        if u_guess == "A" and acct_1_follower > acct_2_follower:
            print("Correct +1 point")
            point +=1
        elif u_guess == "B" and acct_2_follower > acct_1_follower:
            print("Correct +1 point")
            point += 1
        else:
            print(f"{art.logo}\nWrong Game Over!")
            break

        acct_1 = acct_2
        acct_2 = random.choice(data)

        print(point)


compare()