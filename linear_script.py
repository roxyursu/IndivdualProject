import sys
import numpy as np

def init_line(size):
   s = ""
   for i in range (1, size+1) :
      while True :
         j = int(input ("Enter the colour of the player "+ str(i) +" (0 for black or 1 for white):"))
         if (j==0 or j==1) :
            break
         print("Try again!\n")
      s += "\t\tinit(line["+ str(i) +"]) := "+ str(j) +"\n"
   return s


def change_pos(size):
   string = ''
   if size > 2:
      for i in range (2, size):
         string +="\t\tnext(line[" + str(i) + "]) :=\n"+"\t\t\tcase\n" +"\t\t\t\tnew_pos =  "+ str(i) +" : line[old_pos];\n" +"\t\t\t\tnew_pos > old_pos &  "+ str(i) +" >= old_pos &  "+ str(i)   +" < new_pos : line["+str(i+1) +"];\n"+"\t\t\t\tnew_pos < old_pos & "+ str(i) +" > new_pos & "+ str(i)  +" <= old_pos : line["+ str(i-1) +"];\n""\t\t\t\tTRUE : line["+ str(i) +"];\n"+"\t\t\tesac; \n"
   return string   

def happy_init_helper(start,i,end):
   s = "line["+str(start)+ "] + "
   for j in range (start+1, end):
      s += "line["+str(j)+"] + "
   s += "line["+str(end)+"] - line["+str(i)+"] "
   return s

def happy_init(size, n):
   string = ''
   if n >= size :
      for i in range(1, size+1):
         string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(1,i,size) +" <= "+ str((size)//2) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(1,i,size)+" >= "+ str((size)//2) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
   else:
      for i in range(1, size+1):
         if i <= n :
            if i+n > size :
               string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(1,i,size) +" <= "+ str((size)//2) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(1,i,size)+" >= "+ str((size)//2) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
            else :
               string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(1,i,i+n) +" <= "+ str((i+n)//2) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(1,i,i+n)+" >= "+ str((i+n)//2) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
         elif i >= size-n :
            string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(i-n,i,size) +" <= "+ str((size-i+n+1)//2) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(i-n,i,size)+" >= "+ str((size-i+n+1)//2) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
         else :
            string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(i-n,i,i+n) +" <= "+ str(n) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(i-n,i,i+n)+" >= "+ str(n) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
   return string

def happy_next_helper(start,i,end):
   s = "next(line["+str(start)+"]) +"
   for j in range (start+1, end):
      s += "next(line["+str(j)+"]) + "
   s += "next(line["+str(end)+"]) - next(line["+str(i)+"]) "
   return s

def happy_next(size, n):
   string = ''
   if n >= size :
      for i in range(1, size+1):
         string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(1,i,size) +" <= "+ str((size)//2) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(1,i,size)+" >= "+ str((size)//2) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
   else:
      for i in range(1, size+1):
         if i <= n :
            if i+n > size :
               string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(1,i,size) +" <= "+ str((size)//2) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(1,i,size)+" >= "+ str((size)//2) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
            else :
               string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(1,i,i+n) +" <= "+ str((i+n)//2) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(1,i,i+n)+" >= "+ str((i+n)//2) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
         elif i >= size-n :
            string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(i-n,i,size) +" <= "+ str((size-i+n+1)//2) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(i-n,i,size)+" >= "+ str((size-i+n+1)//2) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
         else :
            string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(i-n,i,i+n) +" <= "+ str(n) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(i-n,i,i+n)+" >= "+ str(n) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
   return string

def change_next(size) :
   s = "\t\tnext(change) := \n"
   s += "\t\t\tcase \n"
   for i in range (1, size+1) :
      s += "\t\t\t\tline["+str(i)+"] != next(line["+str(i)+"]) : TRUE;\n"
   s += "\t\t\t\tTRUE : FALSE;\n \t\t\tesac;\n"
   return s

def move_next_helper_left(start, i, end):
   s = ""
   if (i>=start) & (i<=end) :
      for j in range (start, end):
         s += "persons.line["+str(j)+"] + "
      s += "persons.line["+str(end)+"] - persons.line["+str(i)+"] "
   else :
      for j in range (start, end-1):
         s += "persons.line["+str(j)+"] + "
      s += "persons.line["+str(end-1)+"] "
   return s

def move_next_helper_right(start, i, end):
   s = ""
   if (i>=start) & (i<=end) :
      for j in range (start, end):
         s += "persons.line["+str(j)+"] + "
      s += "persons.line["+str(end)+"] - persons.line["+str(i)+"] "
   else :
      for j in range (start+1, end):
         s += "persons.line["+str(j)+"] + "
      s += "persons.line["+str(end)+"] "
   return s


def compare_0(i, start, end) :
   return str(int(np.floor((end-start)/2.0)))

def compare_1(i, start, end) :
   return str(int(np.ceil((end-start)/2.0)))


def move_both_left_and_right(i, j, start1, end1, start2, end2) :
   string  = "\t\t\t\told_pos="+ str(i) +" & persons.happy["+ str(i) +"] = FALSE & persons.line["+ str(i) +"] = 0 & "+move_next_helper_left(start1, i, end1)+"<= "+ compare_0(i, start1, end1) +" & "+move_next_helper_right(start2, i, end2)+"<= "+ compare_0(i, start2, end2) +" : {"+ str(i-j) +","+ str(i+j) +"};\n" 
   string += "\t\t\t\told_pos="+ str(i) +" & persons.happy["+ str(i) +"] = FALSE & persons.line["+ str(i) +"] = 1 & "+move_next_helper_left(start1, i, end1)+">= "+ compare_1(i, start1, end1) +" & "+move_next_helper_right(start2, i, end2)+" >= "+ compare_1(i, start2, end2) +" : {"+ str(i-j) +","+ str(i+j) +"};\n"
   return string

def move_right(i, j, start, end) :
   string  = "\t\t\t\told_pos="+ str(i) +" & persons.happy["+ str(i) +"] = FALSE & persons.line["+ str(i) +"] = 0 & "+move_next_helper_right(start, i, end)+"<= "+ compare_0(i, start, end) +" : {"+ str(i+j) +"};\n" 
   string += "\t\t\t\told_pos="+ str(i) +" & persons.happy["+ str(i) +"] = FALSE & persons.line["+ str(i) +"] = 1 & "+move_next_helper_right(start, i, end)+">= "+ compare_1(i, start, end) +" : {"+ str(i+j) +"};\n"
   return string

def move_left(i, j, start, end) :
   string  = "\t\t\t\told_pos="+ str(i) +" & persons.happy["+ str(i) +"] = FALSE & persons.line["+ str(i) +"] = 0 & "+move_next_helper_left(start, i, end)+"<= "+ compare_0(i, start, end) +" : {"+ str(i-j) +"};\n"   
   string += "\t\t\t\told_pos="+ str(i) +" & persons.happy["+ str(i) +"] = FALSE & persons.line["+ str(i) +"] = 1 & "+move_next_helper_left(start, i, end)+">= "+ compare_1(i, start, end) +" : {"+ str(i-j) +"};\n"
   return string


def move_next(size, n) :
   string = ''
   for i in range(1, size+1):
      string += "\t\t\t\told_pos="+ str(i) +" & persons.happy["+ str(i) +"] = TRUE : "+ str(i) +";\n"
      for j in range(1, size) :
         if (i-j>=1) & (i+j<=size) :
            if (i+j+n <= size) & (i-j-n<1) :
               if (i+j-n>=1) :
                  string += move_both_left_and_right(i, j, 1, i-j+n, i+j-n, i+j+n) 
                  string += move_left(i, j, 1, i-j+n) + move_right(i, j, i+j-n, i+j+n)
               else :
                  string += move_both_left_and_right(i, j, 1, i-j+n, 1, i+j+n) 
                  string += move_left(i, j, 1, i-j+n) + move_right(i, j, 1, i+j+n)

            elif (i+j+n>size) & (i-j-n>=1) :
               if (i-j+n <= size) :
                  string += move_both_left_and_right(i, j, i-j-n, i-j+n, i+j-n, size) 
                  string += move_left(i, j, i-j-n, i-j+n) + move_right(i, j, i+j-n, size)
               else :
                  string += move_both_left_and_right(i, j, i-j-n, size, i+j-n, size) 
                  string += move_left(i, j, i-j-n, size) + move_right(i, j, i+j-n, size)

            elif (i+j+n>size) & (i-j-n<1) :
               if (i-j+n<=size) & (i+j-n>=1) :
                  string += move_both_left_and_right(i, j, 1, i-j+n, i+j-n, size) 
                  string += move_left(i, j, 1, i-j+n) + move_right(i, j, i+j-n, size)  
               elif (i-j+n<=size) :
                  string += move_both_left_and_right(i, j, 1, i-j+n, 1, size) 
                  string += move_left(i, j, 1, i-j+n) + move_right(i, j, 1, size)
               elif (i+j-n>=1) :
                  string += move_both_left_and_right(i, j, 1, size, i+j-n, size) 
                  string += move_left(i, j, 1, size) + move_right(i, j, i+j-n, size)

            elif (i+j+n<= size) & (i-j-n>=1) :
               string += move_both_left_and_right(i, j, i-j-n, i-j+n, i+j-n, i+j+n) 
               string += move_left(i, j, i-j-n, i-j+n) + move_right(i, j, i+j-n, i+j+n)
         elif (i-j>=1) :
            if (i-j-n<1) :
               if (i-j+n<=size) :
                  string += move_left(i, j, 1, i-j+n)
               else :
                  string += move_left(i, j, 1, size)
            else :
               if (i-j+n<=size) :
                  string += move_left(i, j, i-j-n, i-j+n)
               else :
                  string += move_left(i, j, i-j-n, size)
         elif (i+j<=size) : 
            if (i+j-n>=1) :
               if (i+j+n<=size) :
                  string += move_right(i, j, i+j-n, i+j+n)
               else :
                  string += move_right(i, j, i+j-n, size)
            else :
               if (i+j+n<=size) :
                  string += move_right(i, j, 1, i+j+n)
               else :
                  string += move_right(i, j, 1, size)

   return string



def create():
   print("creating new  file")
   size=int(input ("enter the size of the line (at least 2 players):"))
   n=int(raw_input ("enter the neighbourhood size(at least 1):"))
   try:
     file=open("file.smv",'w')
     file.write('-- The module below encodes the line. It has an array called line where each\n'
      '-- element can be either 0 or 1; 0 for black, and 1 for white. So line[3]=0\n'
      '-- represents that there is a black person at position 3. It also has a\n'
      '-- boolean array called happy representing whether the happiness status of each\n'
      '-- position in the line. So happy[2]=TRUE represents that the person at\n'
      '-- position 2 is happy.\n'
      '-- The module takes as input old_pos (the current position of the person to\n'
      '-- move) and new_pos (the new position of the person to move)\n'
      '-- The boolean variable -change- is true if at least one happiness status changed\n'
      '-- It is false if no happiness status changed\n\n'
      'MODULE line(old_pos,new_pos)\n'
	   '\tVAR\n'
      '\t\tline  : array 1..' + str(size) + ' of 0..1;\n' 
	   '\t\thappy : array 1..' + str(size) + ' of boolean;\n'
      '\t\tchange : boolean; \n\n'
      '\tASSIGN\n\n'
      '-- Initialise the line with zeros and ones that are passed as an input\n'
      '-- i.e. Construct the initial line configuration\n\n'
      + init_line(size) +
		'\n-- This is how the colours change in the line when the person in\n'
		'-- old_pos moves to new_pos.\n\n'
      '\t\tnext(line[1]) :=\n'
		'\t\t\tcase\n'
		'\t\t\t\tnew_pos = 1 : line[old_pos]; \n'   
		'\t\t\t\tnew_pos > old_pos & 1 >= old_pos & 1 < new_pos : line[2];\n'
		'\t\t\t\tTRUE : line[1];\n'
		'\t\t\tesac;\n'
      +change_pos(size)+
      '\t\tnext(line[' + str(size) + ']) :=\n'
		'\t\t\tcase\n'
		'\t\t\t\tnew_pos = ' + str(size) + ' : line[old_pos]; \n'   
		'\t\t\t\tnew_pos < old_pos & ' + str(size) + ' > new_pos & ' + str(size) + 
               ' <= old_pos : line[' + str(size-1) + '];\n'
		'\t\t\t\tTRUE : line[' + str(size) + '];\n'
		'\t\t\tesac;\n\n'
      '-- We initialise the happiness status.\n\n'
      +happy_init(size, n) + '\n\n'

      '-- This is how the hapiness statuses change in the line when the person in\n'
		'-- old_pos moves to new_pos.\n\n'
      +happy_next(size, n) + '\n\n' 

      '\t\tinit(change) := FALSE;\n\n'    
      +change_next(size) + 
      
      '-- The main module has an old_pos variable. The value of this variable is\n'
      '-- always arbitrary from 1 to n. If, at a step, old_pos = 3, then we represent\n'
      '-- that is the turn of the person in position 3 to move. If this person is\n'
      '-- already happy (i.e., in the module above happy[3] = TRUE), then it remains\n'
      '-- in the same position (i.e., we set the new_pos variable below to 3).\n'
      '-- Otherwise, if the person at position 3 is not happy, then we find the\n'
      '-- nearest position where it could be happy. We do this in cases, from nearest\n'
      '-- to furthest. \n\n'

      'MODULE main\n'
	   '\tVAR\n'
      '\t\told_pos: 1..5;\n'   
      '\t\tnew_pos: 1..5;\n'
      '\t\tpersons: line(old_pos,new_pos);\n\n'

      '\tASSIGN\n'
		'\t\tnext(new_pos) :=\n'
			'\t\t\tcase\n'
         + move_next(size, n)+
         '\t\t\t\tTRUE : old_pos;\n' 
			'\t\tesac;\n\n'
      'SPEC\n'
      '\tAF AG (!change);\n\n\n')

     file.close()
   except:
         print("error occured")
         sys.exit(0)

create()

