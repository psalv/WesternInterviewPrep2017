
"""



Questions for the coach:

    How much interaction can I expect between an interviewer and myself during the interview?
    
    What types of questions do you find candidates do the worst on?
    
    Is there anything that candidates tend to consistently underprepare for?

    What types of questions will almost definitely be asked?



They are looking for:
    
    Well written code

    Algorithms + Data Structure knowledge

    Analytical Skills

    Sound Design

    Communication



At the beginning of the interview are generally questions, these are opportunities to be likable,
but the interview is a fixed length so get to the technically questions quickly.

Brain teaser questions have been banned at Google.

Questions aim to test fundamentals, since it's hard to get to know someone in only 45 minutes.

Know your big oh! Give it without even being asked, this is explicitly looked for.

They aren't looking for the answer, they are looking for how you solve the problem: your thought process is the key.

Will often ask for successive iterations of opotimization,
so don't try to start with an ooptimal/clever solution, this can come afterwards.



---


Clarify problem
Define approach
Priopose solutiojn
Consider info or constraints
Propose alternative solution // probably wont be able to do this fully but note the other and pros/cons
Implment solution

    pay attention to corner cases --> identify them and tell the interviewer when you're handling them

    your code will reflect your abilities greatly
        hriign panel will see your code
        
    
learn hwo to do mod for negative numbers

whats deliverable: do i need a class?


** verbally propose solution before coding (faster to find mistakes)
ask if the interviewer has questions before refining
feel free to say that you will refine


want to shw that we've thought about testing the code
    think about potential problems
    
    
    
    
    
    
    
tiem/space tradeoff
    choose sol'n you can omplement in interview time frame
    state choices to interviewer
    
optimizing
    refine later!!
    tak through naive soln and impprove
    consider various scenarios: input is big or small?
    
API
    this is not a memory test, if you cant remember and API ask!!!      // make up the API call if you don't know and say that you are

testing:
    say what cases you would test
    eserve time to work on a small case and edge cases
"""

# imagine large bucket of coloured marbles, algorithm to pull out random

# pass in as data structure

# with or without replacement


# array each index is a colour with counter of number
# then predict chance
# pay attention to off by 1's
import random
def selectMarbles(marbles):
    n = 0
    marblesColours = {0:"red", 1:"green", 2:"blue", 3:"yellow"}
    for i in marbles:
        n += i

    n = random.randint(0, n - 1)

    cur = 0
    for i in range(len(marbles)):
        cur += marbles[i]
        if cur > n:
            marbles[i] -= 1
            return marblesColours[i]

