## 2024-12-07 10:02 AM
### Log Entry 1

Today, in this entry, I am atarting this project. I can recognize that it is due tomorrow, but to be honest just didnt have time because of way too many finals, so this is how its going to be.

the plan first of all is to set up the git structure and start on a basic start to the project overall

my understanding of the project right now is that I need to create software to create, read, and edit these index files containing b trees, and also to implement a search and load. 
im going to commit this log, then begin work on just getting a rough idea of the structure of these b trees, and try to decode the sample.idx file so I can tell what's happening.

## 2024-12-07 11:03 PM

## Log Entry 2

i've been studying for my finals all day, but its time to get started on this. I've been thinking about this project all day, and i now have an idea on how im going to start implementing it. this session, im going to set up the BTreeNode class, which should have methods to serialize and deserialize, while sticking to the structure required for this.

## 2024-12-07 11:41 PM

## Log Entry 3

just finished the implementation i was going to do before, it wasnt very hard. i was mostly just trying to take the parameters tying the entire thing together from the instructions and putting it into code. I didnt really have problems, and im going to take a 5 minute break before starting to code again. nothing really happened, we are just beginning, so i accomplished everything i wanted to get done! next, i want to read the header of the index file, so thats going to be the next part of my implementation


## 2024-12-07 11:52 PM

## Log Entry 4

ok its time for me to start coding again. going back to what i was expecting to do before, i want to write some code to read the headers. that's about it honestly, i havent had much time to think in between the last session and this one, but this is a pretty boring, simple next step so just time to do it i guess.

## 2024-12-08 12:10 AM

## Log Entry 5

well, i was able to completely implement the index reading thing, wasnt too bad, i havent had any thoughts about this since the last session, so thats great. i didnt really face any problems, to be honest this was equally as easy to implement, not really at the logic part yet, just setting up infrastructure, so its fast and easy. I ACCOMPLISHED MY GOAL YAY!!! next session, after my little break, i am going to figure out how to dynamically allocate nodes. thats the plan, ill think about it and get back to this log when i start developing yay

## 2024-12-08 12:10 AM

## Log Entry 6 

time to start working again, the goal of this session is to dynamically allocate notes, so that the next block id is updated, and is synced in the header as well. this should ideally not be that bad? but i guess we shall see. time to code this out, lets see how it does

## 2024-12-08 12:35 AM

## Log Entry 7

this absolutely should not have taken so long, but got a bit distracted. the implementation was quite simple, and im all done yay. the next thing ive got to do is add the implementation for the search. this is one of the core functions of the assignment, so lets go. didnt really hit any problems, i just took too long because i got distracted. going to do one more session tonight before i sleep, and finish this up tomorrow, hoping i dont lose points for doing this all in one day, technically. ok, signing off for a short break, and the next session is the search.

## 2024-12-08 12:45 AM

## Log Entry 8

time to start working again, i feel like im messing up the git thing somehow, im so exhausted i feel like ive missed a commit or two somewhere along the line, for right now though, im fine, not many thoughts since before, but going to try and make this search functionality a reality. gonna just jump right into it.


## 2024-12-08 12:58 AM

## Log Entry 9

ok got the search function done, this was a little annoying, i had a few issues with indexing child pointers during the traversal of the tree, but at the end of the day i got it to work, and there arent any issues right now. the current time is almost 1 am, so im going to go to sleep and keep working on this in the morning. I dont think this is going to be so bad after all. but anyway, going to sleep on the thoughts, the next few steps are to implement splitting of nodes, which im going to think about in my dreams. goodnight log

## 2024-12-08 9:03 AM

## log entry 10

ok, i had the chance to sleep, and was thinking about how i was going to implement the node splitting/insertion. there are basically two cases i have to consider with this, and they are inserting a node when there is room to insert another node, so basically inserting into a non full node, and the case of when i am inserting into a node that is already full, and i have to deal with moving the  middle key to the parent and splitting the node. this seems challenging, but going to give it a shot and see how it goes.

## 2024-12-08 11:29 AM

## log entry 11
Ive been working for a few horus now, this has definitely been the most challegning parts of the entire project, i first did some basic changes to make the system better, including adding a constants section, instead of hardcoding in numbers. it was getting hard to keep track of what was what, so that was necessary. i also changed up the Btree class, adding in the functionality of inserting a node when its full, as well as when theres room. this is probably the hardest part of the project, so glad its finally done. this wasn't technically part of the plan, but it fit in the same section in my head, so got it done. granted, im going to do the majority of my debugging later, but for now, it should be ok. im still fleshing this out based on the plan i wrote out, so its going well so far. i accomplished my goal for the session, and for the next session, i think im going to do an easy section, which is just the create command. this should be super easy since i already have the insert and whatnot, just need to get it done. anyway, going to eat breakfast and get back to work.

## 2024-12-08 11:57 AM

## log entry 12

got back with breakfast in hand, and going to do the easy parts while i eat. going to try and implement the create function, which should be just makign and using the main function to run the right set of commands. this is the first part im doing of the "frontend" of this system, but again, shouldnt be too hard. havent had many insights, this is just putting pieces together.

## 2024-12-08 12:16 PM

## log entry 13

implementing the main function, as well as the create command, wasnt hard at all, happy with how it went, i guess. there's now a clear framework for how im going to implement the rest of the functions, just one by one, so planning on doing those sequentially. in terms of this session, it was super straight forward. going to stick to nested if statements for this, because im too tired to work with anything else right now, but shouldnt cause any issues with this simple menu. plan for the next "session" is to just work on another function, not sure which one yet, but ill decide when i get there. going to have another snack, and ill be back in a few minutes.

## 2024-12-08 1:26 PM

## log entry 14

ok that break was longer than a few minutes, and if im being honest, im running out of time to take these breaks, considering that this project is due tonight, even with the extension. this is going to be another long coding session, my plan is essentially threefold. i have to complete the logic for read/write/allocate, i have to do the logic for printing, and anything that goes with that, and i need to do any traversal necessary here. the final step after that is to finish up the main function, putting everything together. im going to work for a few hours, and get as much done as possible, then check back up on this log.

## 2024-12-08 2:31 PM

## log entry 15

writing this while im still working on the tasks i was mentioning in the previous log, but for right now, ive managed to implement functionality for different cases for the readwrite, readonly, and open to create. 

## 2024-12-08 3:11 PM

## log entry 16

finished up the writenode, readnode, and allocatenode functions, as i planned, and also created a few helper functions for that, im still working but i think im supposed to be doing this while i work as well. it's a good thing i had to learn b+ trees for database systems, otherwise this would have definitely been more difficult. i only have the print function, and the overall menu system in the main function to deal with, and ill finally be done with this. the plan is to keep working, and be done with everything, as a first run through, then start with any debugging i need to do, although im hoping that doing everything in such a sequential, modular manner reduces the amout of pain i have to go through to make sure that everything works properly and there arent any bugs. anyway, continuing onwards to the main function and print.


## 2024-12-08 3:56 PM

## log entry 17

finally finsihed with the coding of everything except the main method, going to take a break for a few hours, then after that im going to do the main function as well as debugging, i am very ready to get this done. I didnt encounter too many issues while doing this part, this section of coding mostly consisted of me implementing the logic for printing, i meant to be finished with the main function as well by now, but im going to have to finish it while i do my debugging. currently not facing too many issues, the conditions for each task are easy to meet based on an in depth understanding of how b trees work (THANKS DSA) and im able to execute them without too much issue. time to take this break, study for other classes, then get back to it to finish my main function and do all the debugging needed to make a finished product.
