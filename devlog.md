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

