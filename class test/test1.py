## For my first Drone 

alp_start = 96
alp_camera = 6
alp_distance = 20
alp_fl = 2
alp_unload = 4
alp_return= 1
alp_time = 34

## Now calculate the reserve and remaining 


alp_aftercamera_start = alp_start - alp_camera
alp_after_fly = alp_aftercamera_start - (alp_distance * alp_fl)
alp_afterunload = alp_after_fly - alp_unload
alp_remaining = alp_afterunload - (alp_distance * alp_return)

alp_reserve = alp_remaining * 15 / 100
alp_usable = alp_remaining - alp_reserve


print("Alpha remaining:", alp_remaining, "usable:", alp_usable)


## for drone 2

brav_start = 98
brav_camera = 8
brav_distance = 18
brav_fly = 2
brav_unload = 6
brav_return= 1
brav_time = 30

## now calculate the reserve and remaining
brav_aftercamera_start = brav_start - brav_camera
brav_after_fly = brav_aftercamera_start - (brav_distance * brav_fly)
brav_afterunload = brav_after_fly - brav_unload
brav_remaining = brav_afterunload - (brav_distance * brav_return)

brav_reserve = brav_remaining * 15 / 100
brav_usable = brav_remaining - brav_reserve

print("Bravo remaining:", brav_remaining, "usable:", brav_usable)


## for drone 3
charl_start = 94
charl_camera = 7
charl_distance = 22
charl_fly = 2
charl_unload = 6
charl_return= 1
charl_time = 38
## now calculate the reserve and remaining

charl_aftercamera_start = charl_start - charl_camera
charl_after_fly = charl_aftercamera_start - (charl_distance * charl_fly)
charl_afterunload = charl_after_fly - charl_unload
charl_remaining = charl_afterunload - (charl_distance * charl_return)

charl_reserve = charl_remaining * 15 / 100
charl_usable = charl_remaining - charl_reserve

print("Charlie remaining:", charl_remaining, "usable:", charl_usable)

## Determine the most completion time 




most_completiontime = max(alp_time, brav_time, charl_time)

print("Most completion time:", most_completiontime)


## Highest usable battery find out 
highest_usable_battery = max(alp_usable, brav_usable, charl_usable)

# find out 1st ,2nd ,3rd drone  ber kra

if highest_usable_battery == alp_usable:
    print("1st drone :", alp_usable)
elif highest_usable_battery == brav_usable:
    print("2nd drone:", brav_usable)
else:
    print("3rd drone :", charl_usable)


## mission sucessful naki nah 

if highest_usable_battery >= 20:
    print("mission successful")
else:
    print(" research required for the drones ")
