CS 7200 Algorithm Analysis and Design
Assignment 1
Author: Bibek Raj Joshi
Deadline: Feb 6, 2023
W_ID = w140bxj

Details on the Program:
The is_stable_matching function is used to determine the stability of a matching of pairs. The function takes as input two dictionaries women_prefs and men_prefs, which represent the preferences of each woman and each man, respectively. It also takes a dictionary matching that represents the current matching of pairs. 

The function starts by creating two dictionaries better_men_options and better_women_options, which store the better options for each man and woman, respectively. The better options for a man are the women who are ranked higher in the man's preference list than the woman he is currently paired with and vice versa.

Then, the function loops over each man in the better_men_options dictionary, and for each man, it loops over the women who are his better options. For each woman, the function checks if the woman has the current man in her list of better men. If she does, then the current pair is unstable and the function adds them to the unstable_pair list.

The function returns three values: a boolean indicating whether the matching is stable or not, a list of unstable pairs, and a list of pairs that were checked.

The program requires one input to run. 

Input File Format
(The inputfile needs to be configured/encoded as provided in the assignment1 handout. )
The first line representing the number of men or women.
Then, n*2 lines representing the preferences of men and women - n lines for men and n lines for women.
Finally, the last n number of lines containing the "matching".



Run the program

For example: 

inputfileName = input.txt


To run the program enter the command as follows from terminal. 

python assignment1.py <inputFileName> 

python assignment1.py input.txt 

