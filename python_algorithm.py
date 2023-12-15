# First loop
let T = 0

for each ticket on rail:
    T = T + 1
    
Return T


# Second loop
let T = 0

for each pair of ticket on rail:
    T = T + 2

Return T


let T = 0

for each pair of ticket on rail
        Set T = T + 2
    
if 1 ticket remains then
        Set T = T + 1
    
Return T