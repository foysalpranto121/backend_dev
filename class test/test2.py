#Use case for anwar vai
total_tips=18
earned_per_tips=420

bonus=750
total_earned_1=total_tips*earned_per_tips+bonus

print("Total earned:", total_earned_1)

deducted_commission=(total_earned_1*.22)
print("Deducted commission:", deducted_commission)
fuel_spent=2850
tools_cost=350
parking_cost=450
total_expenses_1=fuel_spent+tools_cost+parking_cost+deducted_commission
print("Total expenses:", total_expenses_1)

net_profit_1=total_earned_1-total_expenses_1
print("Net profit:", net_profit_1)

##use case for Abdullah vai'
total_tips=21
earned_per_tips=390
bonus=500
total_earned_2=total_tips*earned_per_tips+bonus
print("Total earned:", total_earned_2)

deducted_commission=(total_earned_2*.22)
print("Deducted commission:", deducted_commission)
fuel_spent=3150
tools_cost=500
parking_cost=300
total_expenses_2=fuel_spent+tools_cost+parking_cost+deducted_commission
print("Total expenses:", total_expenses_2)

net_profit_2=total_earned_2-total_expenses_2
print("Net profit:", net_profit_2)

## use case for Anik jubayer

total_tips=16
earned_per_tips=510
bonus=900
total_earned_3=total_tips*earned_per_tips+bonus
print("Total earned:", total_earned_3)
deducted_commission=(total_earned_3*.22)
print("Deducted commission:", deducted_commission)
fuel_spent=2650
tools_cost=250
parking_cost=550

total_expenses_3=fuel_spent+tools_cost+parking_cost+deducted_commission
print("Total expenses:", total_expenses_3)
net_profit_3=total_earned_3-total_expenses_3
print("Net profit:", net_profit_3)

## now solving ques


## ques 1

total_tips_earning=(18*420)+(21*390)+(16*510)
print("Total tips earned:", total_tips_earning)


## ques 2
total_uber_commision=total_tips_earning*.22
print("Total Uber commission:", total_uber_commision)

## ques 3
total_earned_after_bonus=total_earned_1+total_earned_2+total_earned_3
print("Total earned after bonus:", total_earned_after_bonus)

total_earn_final=total_earned_after_bonus-total_uber_commision
print("Total earned after commission:", total_earn_final)


## ques 4
final_expenses=total_expenses_1+total_expenses_2+total_expenses_3
print("Final expenses:", final_expenses)

## ques 5
net_profit=total_earn_final-final_expenses
print("Net profit:", net_profit)

## ques 6
highest_net_profit=max(net_profit_1, net_profit_2, net_profit_3)
print("Highest net profit:", highest_net_profit)

##ques 7( rank ubber)


if net_profit_1>net_profit_2 and net_profit_1>net_profit_3:
    print("Anwar vai highest net profit.")
elif net_profit_2>net_profit_1 and net_profit_2>net_profit_3:
    print("Abdullah vai highest net profit.")
else:
    print("Anik jubayer vai highest net profit.")


##question 8 

##anower vai use case 

time_spent_1=(9*60)+15

##abdullah vai use case
time_spent_2=(10*60)

## jubayer vai use case
time_spent_3=(8*60)+30

longest_time_duration=max(time_spent_1, time_spent_2, time_spent_3)
print("Longest time duration:", longest_time_duration, "minutes")


## ques 9

# for anowar vai

if net_profit_1>=6000:
    print("excellent ")
elif net_profit_1 >=4000 and net_profit_1<=5999:

    print("Good performance ")

else:
    print("Needs Improvement")






