# python-ndfa-emulator
a simple non-deterministic finite automata machine emulator written in python
    
quick note: I created this because I was in a slump and just wanted to complete a project, so please forgive the sloppy code      
also: ndfa stands for non-deterministic finite automata             

#how-to-use 
Every state is represented by a txt file with the name of the state. for example state 1 would be in 1.txt              
The transitions for each state are represented by a line for each state. A single arc/transition is represented by the character that would cause that transition and then the state that it will transition into. Optionally instead of using the letter you can put a - before it to have an arc for everything that isn't the letter supplied. if the state is an accepting state than it should only contain the string ACCEPT.                                               
for example:                   
m1 (if the next letter in the alphabet is m then it will transition into state 1)                    
-m0 (if the next letter in the alphabet is not m then it will transition into state 0)                                 

to run the code run the python file ndfa.py . optionally if you include the argument d then it will output debugging information in the form [character]: [states after the character]                                                      
the alphabet is stored in alphabet.txt                           

for an example of a fully working program that will detect any string that has main in it in that order see the files included in the github. Also if you want an alphabet the code will accept rename alphabetaccept.txt to just alphabet.txt                   
though the only file you need to create your own is ndfa.py.                         
