
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



Strategy:

    Clarify problem

    Define approach

    Propose solution
        Think about whats deliverable: do I need a class?
        Verbally propose the solution before coding, so you can find mistakes faster

    Consider info or constraints

    Propose alternative solution // probably wont be able to do this fully but note the other and pros/cons

    Implement solution
        Pay attention to corner cases (Identify them and say when you're dealing with them)
        Your code will reflect your abilities greatly since it goes to the hiring committee

    Refine solution
        Asks questions before going further


Feel free to say what you plan on refining as you code.

Don't forget to state how you would test the code and run through a simple example, statign potential problems.

Talk about the time/space tradeoff, and state the choices that you are making.
    
Refine later !! Talk through the naive solution, consider big/small input and improvements.
    
It isn't a memory test, don't be afraid to ask API related questions, if you don't remember a call make one up (but say so).

"""


# Question: develop an algorithm to pick a coloured marble at random from a bucket full of marbles.

# Need to decide on data structure, with/without replacement

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

