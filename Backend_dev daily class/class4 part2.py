## loop
## for loop

player_name=["messi","ronaldo","neymar","mbappe","zidane"]
for name in player_name:
    print(name)


## for loop with index
player_name=["messi","ronaldo","neymar","mbappe","zidane"]
for i in range(len(player_name)):
    print(player_name[i])

##break statemnet 
for name in player_name:
    if name == "neymar":
        break
    print(name)

## continue statement 
for name in player_name:
    if name == "neymar":
        continue
    print(name)

## range
for player_name in range(5):
    print(player_name)


