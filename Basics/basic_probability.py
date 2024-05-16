'''
Mike wants to go fishing this weekend to nearby lake. His neighbour Alice (is the one Mike was hoping to ask out since long time)
is also planing to go to the same spot for fishing this weekend. The probability that it will rain this weekend is
. There are two possible ways to reach the fishing spot (bus or train). The probability that Mike will take the bus is
 and that Alice will take the bus is
. Travel plans of both are independent of each other and rain.

What is the probability
 that Mike and Alice meet each other only (should not meet in bus or train) in a romantic setup (on a lake in rain)?
'''

print("Enter Mike's Bus Probability:")
mikeBusProb = float(input())
print("Enter Alice's Bus Probability:")
alisBusProb = float(input())
print("Enter rain's Probability:")
rainProb = float(input())

res = rainProb * alisBusProb * (1-mikeBusProb) + rainProb * mikeBusProb * (1-alisBusProb)
print("Probability of Mike and Alice meeting on the lake")
print('%.6f' % res)