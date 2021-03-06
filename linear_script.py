import sys
import numpy as np

def init_line(size):
   s = ""
   for i in range (1, size+1) :
      while True :
         j = int(input ("Enter the colour of the player "+ str(i) +" (0 for white or 1 for black): "))
         if (j==0 or j==1) :
            break
         print("Try again!\n")
      s += "\t\tinit(line["+ str(i) +"]) := "+ str(j) +";\n"
   return s

def change_pos(size):
   s = ""
   if size > 2:
      for i in range (2, size):
         s +="\t\tnext(line[" + str(i) + "]) :=\n"+"\t\t\tcase\n" 
         s +="\t\t\t\tnew_pos =  "+ str(i) +" : line[old_pos];\n" 
         s +="\t\t\t\tnew_pos > old_pos &  "+ str(i) +" >= old_pos &  "+ str(i)   +" < new_pos : line["+str(i+1) +"];\n"
         s +="\t\t\t\tnew_pos < old_pos & "+ str(i) +" > new_pos & "+ str(i)  +" <= old_pos : line["+ str(i-1) +"];\n"
         s +="\t\t\t\tTRUE : line["+ str(i) +"];\n"+"\t\t\tesac; \n"
   return s 


def compare_0(i, start, end) :
   return str(int(np.floor((end-start)/2.0)))

def compare_1(i, start, end) :
   return str(int(np.ceil((end-start)/2.0)))
 
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
         string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(1,i,size) +" <= "+ compare_0(i, 1, size) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(1,i,size)+" >= "+ compare_1(i, 1, size) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
   else:
      for i in range(1, size+1):
         if i <= n :
            if i+n > size :
               string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(1,i,size) +" <= "+compare_0(i, 1, size) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(1,i,size)+" >= "+compare_1(i, 1, size) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
            else :
               string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(1,i,i+n) +" <= "+ compare_0(i, 1, i+n) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(1,i,i+n)+" >= "+ compare_1(i, 1, i+n) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
         elif i >= size-n :
            string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(i-n,i,size) +" <= "+ compare_0(i, i-n, size) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(i-n,i,size)+" >= "+ compare_1(i, i-n, size) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
         else :
            string +="\t\tinit(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tline["+ str(i) +"] = 0 & "+ happy_init_helper(i-n,i,i+n) +" <= "+ compare_0(i, i-n, i+n) +" : TRUE;\n" +"\t\t\t\tline["+ str(i) +"] = 1 & "+ happy_init_helper(i-n,i,i+n)+" >= "+ compare_1(i, i-n, i+n) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
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
         string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(1,i,size) +" <= "+ compare_0(i, 1, size) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(1,i,size)+" >= "+ compare_1(i, 1, size) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
   else:
      for i in range(1, size+1):
         if i <= n :
            if i+n > size :
               string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(1,i,size) +" <= "+ compare_0(i, 1, size) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(1,i,size)+" >= "+ compare_1(i, 1, size) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
            else :
               string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(1,i,i+n) +" <= "+ compare_0(i, 1, i+n) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(1,i,i+n)+" >= "+ compare_1(i, 1, i+n) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
         elif i >= size-n :
            string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(i-n,i,size) +" <= "+ compare_0(i, i-n, size) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(i-n,i,size)+" >= "+ compare_1(i, i-n, size) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
         else :
            string +="\t\tnext(happy["+ str(i) +"]) :=\n" +"\t\t\tcase \n" +"\t\t\t\tnext(line["+ str(i) +"]) = 0 & "+ happy_next_helper(i-n,i,i+n) +" <= "+ compare_0(i, i-n, i+n) +" : TRUE;\n" +"\t\t\t\tnext(line["+ str(i) +"]) = 1 & "+ happy_next_helper(i-n,i,i+n)+" >= "+ compare_1(i, i-n, i+n) +" : TRUE;\n" +"\t\t\t\tTRUE: FALSE;\n" +"\t\t\tesac;\n"
   return string

def sep_table_init(size) :
   s = ""
   for i in range (1, size+1) :
      s += "\t\tinit(separation_table["+str(i)+"]) := \n"
      s += "\t\t\tcase \n"
      s += "\t\t\t\tline["+str(i)+"] != line["+str(i+1)+"] : 1;\n"
      s += "\t\t\t\tTRUE : 0;\n \t\t\tesac;\n\n"
   return s

def fairness_constraint(size) :
   s = ""
   for i in range (1, size+1) :
      s += "\tFAIRNESS old_pos = "+str(i)+"\n"
   return s

def sep_table_next(size) :
   s = ""
   for i in range (1, size+1) :
      s += "\t\tnext(separation_table["+str(i)+"]) := \n"
      s += "\t\t\tcase \n"
      s += "\t\t\t\tnext(line["+str(i)+"]) != next(line["+str(i+1)+"]) : 1;\n"
      s += "\t\t\t\tTRUE : 0;\n \t\t\tesac;\n\n"
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

def move_next_helper_left_next(start, i, end):
   s = ""
   if (i>=start) & (i<=end) :
      for j in range (start, end):
         s += "next(persons.line["+str(j)+"]) + "
      s += "next(persons.line["+str(end)+"]) - next(persons.line["+str(i)+"]) "
   else :
      for j in range (start, end-1):
         s += "next(persons.line["+str(j)+"]) + "
      s += "next(persons.line["+str(end-1)+"]) "
   return s

def move_next_helper_right_next(start, i, end):
   s = ""
   if (i>=start) & (i<=end) :
      for j in range (start, end):
         s += "next(persons.line["+str(j)+"]) + "
      s += "next(persons.line["+str(end)+"]) - next(persons.line["+str(i)+"]) "
   else :
      for j in range (start+1, end):
         s += "next(persons.line["+str(j)+"]) + "
      s += "next(persons.line["+str(end)+"]) "
   return s


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

def move_both_left_and_right_next(i, j, start1, end1, start2, end2) :
   string  = "\t\t\t\tnext(old_pos)="+ str(i) +" & next(persons.happy["+ str(i) +"]) = FALSE & next(persons.line["+ str(i) +"]) = 0 & "+move_next_helper_left_next(start1, i, end1)+"<= "+ compare_0(i, start1, end1) +" & "+move_next_helper_right_next(start2, i, end2)+"<= "+ compare_0(i, start2, end2) +" : {"+ str(i-j) +","+ str(i+j) +"};\n" 
   string += "\t\t\t\tnext(old_pos)="+ str(i) +" & next(persons.happy["+ str(i) +"]) = FALSE & next(persons.line["+ str(i) +"]) = 1 & "+move_next_helper_left_next(start1, i, end1)+">= "+ compare_1(i, start1, end1) +" & "+move_next_helper_right_next(start2, i, end2)+" >= "+ compare_1(i, start2, end2) +" : {"+ str(i-j) +","+ str(i+j) +"};\n"
   return string

def move_right_next(i, j, start, end) :
   string  = "\t\t\t\tnext(old_pos)="+ str(i) +" & next(persons.happy["+ str(i) +"]) = FALSE & next(persons.line["+ str(i) +"]) = 0 & "+move_next_helper_right_next(start, i, end)+"<= "+ compare_0(i, start, end) +" : {"+ str(i+j) +"};\n" 
   string += "\t\t\t\tnext(old_pos)="+ str(i) +" & next(persons.happy["+ str(i) +"]) = FALSE & next(persons.line["+ str(i) +"]) = 1 & "+move_next_helper_right_next(start, i, end)+">= "+ compare_1(i, start, end) +" : {"+ str(i+j) +"};\n"
   return string

def move_left_next(i, j, start, end) :
   string  = "\t\t\t\tnext(old_pos)="+ str(i) +" & next(persons.happy["+ str(i) +"]) = FALSE & next(persons.line["+ str(i) +"]) = 0 & "+move_next_helper_left_next(start, i, end)+"<= "+ compare_0(i, start, end) +" : {"+ str(i-j) +"};\n"   
   string += "\t\t\t\tnext(old_pos)="+ str(i) +" & next(persons.happy["+ str(i) +"]) = FALSE & next(persons.line["+ str(i) +"]) = 1 & "+move_next_helper_left_next(start, i, end)+">= "+ compare_1(i, start, end) +" : {"+ str(i-j) +"};\n"
   return string

def move_init(size, n) :
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

def move_next(size, n) :
   string = ""
   for i in range(1, size+1):
      string += "\t\t\t\tnext(old_pos)="+ str(i) +" & next(persons.happy["+ str(i) +"]) = TRUE : "+ str(i) +";\n"
      for j in range(1, size) :
         if (i-j>=1) & (i+j<=size) :
            if (i+j+n <= size) & (i-j-n<1) :
               if (i+j-n>=1) :
                  string += move_both_left_and_right_next(i, j, 1, i-j+n, i+j-n, i+j+n) 
                  string += move_left_next(i, j, 1, i-j+n) + move_right_next(i, j, i+j-n, i+j+n)
               else :
                  string += move_both_left_and_right_next(i, j, 1, i-j+n, 1, i+j+n) 
                  string += move_left_next(i, j, 1, i-j+n) + move_right_next(i, j, 1, i+j+n)

            elif (i+j+n>size) & (i-j-n>=1) :
               if (i-j+n <= size) :
                  string += move_both_left_and_right_next(i, j, i-j-n, i-j+n, i+j-n, size) 
                  string += move_left_next(i, j, i-j-n, i-j+n) + move_right_next(i, j, i+j-n, size)
               else :
                  string += move_both_left_and_right_next(i, j, i-j-n, size, i+j-n, size) 
                  string += move_left_next(i, j, i-j-n, size) + move_right_next(i, j, i+j-n, size)

            elif (i+j+n>size) & (i-j-n<1) :
               if (i-j+n<=size) & (i+j-n>=1) :
                  string += move_both_left_and_right_next(i, j, 1, i-j+n, i+j-n, size) 
                  string += move_left_next(i, j, 1, i-j+n) + move_right_next(i, j, i+j-n, size)  
               elif (i-j+n<=size) :
                  string += move_both_left_and_right_next(i, j, 1, i-j+n, 1, size) 
                  string += move_left_next(i, j, 1, i-j+n) + move_right_next(i, j, 1, size)
               elif (i+j-n>=1) :
                  string += move_both_left_and_right_next(i, j, 1, size, i+j-n, size) 
                  string += move_left_next(i, j, 1, size) + move_right_next(i, j, i+j-n, size)

            elif (i+j+n<= size) & (i-j-n>=1) :
               string += move_both_left_and_right_next(i, j, i-j-n, i-j+n, i+j-n, i+j+n) 
               string += move_left_next(i, j, i-j-n, i-j+n) + move_right_next(i, j, i+j-n, i+j+n)
         elif (i-j>=1) :
            if (i-j-n<1) :
               if (i-j+n<=size) :
                  string += move_left_next(i, j, 1, i-j+n)
               else :
                  string += move_left_next(i, j, 1, size)
            else :
               if (i-j+n<=size) :
                  string += move_left_next(i, j, i-j-n, i-j+n)
               else :
                  string += move_left_next(i, j, i-j-n, size)
         elif (i+j<=size) : 
            if (i+j-n>=1) :
               if (i+j+n<=size) :
                  string += move_right_next(i, j, i+j-n, i+j+n)
               else :
                  string += move_right_next(i, j, i+j-n, size)
            else :
               if (i+j+n<=size) :
                  string += move_right_next(i, j, 1, i+j+n)
               else :
                  string += move_right_next(i, j, 1, size)

   return string

def convergence_spec() :
   while True :
      ans = raw_input("Do you want to test convergence? [yes/no]\n").lower()
      if ans in ('yes', 'y'):
         return "SPEC\n\tAF AG (!change);\n\n"
      elif ans in ('no','n'):
         return ""
      else:
         sys.stdout.write("Please respond with 'yes' or 'no'")


def complete_segregation(size) :
   s = ""
   for i in range(1, size-1) :
      s += "persons.separation_table["+ str(i) +"] + "
   s += "persons.separation_table["+ str(size-1) +"] "
   return s

def segregation_level(size) : 
   s = ""
   for i in range(1, size) :
      s += "SPEC\n"
      s += "\tEF AG ( " 
      for j in range (1, size-1) :
         s += "persons.separation_table["+ str(j) +"] + "
      s += "persons.separation_table["+ str(size-1) +"] = "+ str(i)+ " ); \n\n"
   return s

def complete_segregation_spec(size) :
   while True :
      ans = raw_input("Do you want to test for complete segregation? [yes/no]\n").lower()
      if ans in ('yes', 'y'):
         s = "-- Is complete segregation going to occur in all scenarios?"
         s += "\nSPEC\n"
         s += "\tAF AG( " + complete_segregation(size) + "=1 | " + complete_segregation(size) + " = 0 );\n\n"
         return s
      elif ans in ('no','n'):
         return ""
      else:
         sys.stdout.write("Please respond with 'yes' or 'no'")

def level_of_segregation_spec(size) :
   while True :
      ans = raw_input("Do you want to test for the level of segregation? [yes/no]\n").lower()
      if ans in ('yes', 'y'):
         return "-- Testing for different degrees of segregation\n" + segregation_level(size)
      elif ans in ('no','n'):
         return ""
      else:
         sys.stdout.write("Please respond with 'yes' or 'no'")

def create():
   print("Creating a new .smv file for your model.")
   size=int(input ("Please, enter the size of the line (at least 2 players): "))
   n=int(raw_input ("Please, enter the neighbourhood size (at least 1): "))
   try:
     file=open("model.smv",'w')
     file.write('-- The module below encodes the line. It has an array called line where each\n'
      '-- element can be either 0 or 1; 0 for white, and 1 for black. So line[3]=0\n'
      '-- represents that there is a white person at position 3. It also has a\n'
      '-- boolean array called happy representing whether the happiness status of each\n'
      '-- position in the line. So happy[2]=TRUE represents that the person at\n'
      '-- position 2 is happy.\n\n'

      '-- The module takes as input old_pos (the current position of the person to\n'
      '-- move) and new_pos (the new position of the person to move)\n\n'

      '-- Separation table is an array of size (n-1) of integers 1 and 0\n'
      '-- separation_table[i] is 1 if line[i] != line[i+1], 0 otherwise\n\n'      

      'MODULE line(old_pos,new_pos)\n'
	   '\tVAR\n'
      '\t\tline  : array 1..' + str(size) + ' of 0..1;\n' 
	   '\t\thappy : array 1..' + str(size) + ' of boolean;\n'
      '\t\tseparation_table : array 1..' + str(size-1) + ' of 0..1;\n\n' 

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
      
      '-- Create the separation_table array\n'
      +sep_table_init(size-1) + 
      sep_table_next(size-1) +
      '\n\n'
      
      '-- The main module has an old_pos variable. The value of this variable is\n'
      '-- always arbitrary from 1 to n. If, at a step, old_pos = 3, then we represent\n'
      '-- that is the turn of the person in position 3 to move. If this person is\n'
      '-- already happy (i.e., in the module above happy[3] = TRUE), then it remains\n'
      '-- in the same position (i.e., we set the new_pos variable below to 3).\n'
      '-- Otherwise, if the person at position 3 is not happy, then we find the\n'
      '-- nearest position where it could be happy. We do this in cases, from nearest\n'
      '-- to furthest. \n\n'

      '-- The boolean variable -change- is true if at least one agent changed his/her position\n'
      '-- It is false if no player has moved\n\n'

      'MODULE main\n'
	   '\tVAR\n'
      '\t\told_pos: 1..' + str(size) + ';\n'   
      '\t\tnew_pos: 1..' + str(size) + ';\n'
      '\t\tchange : boolean; \n'
      '\t\tpersons: line(old_pos,new_pos);\n\n'

      '\tASSIGN\n'
      '\t\tinit(new_pos) :=\n'
         '\t\t\tcase\n'
         + move_init(size, n)+
         '\t\t\t\tTRUE : old_pos;\n' 
         '\t\tesac;\n\n'
		'\t\tnext(new_pos) :=\n'
			'\t\t\tcase\n'
         + move_next(size, n)+
         '\t\t\t\tTRUE : next(old_pos);\n' 
			'\t\tesac;\n\n'

      '-- Initilise change variable \n'
      '\t\tinit(change) := FALSE;\n\n'    
      '\t\tnext(change) := \n'
      '\t\t\tcase\n'
      '\t\t\t\tnext(old_pos) != next(new_pos) : TRUE;\n' 
      '\t\t\t\tTRUE : FALSE;\n'
      '\t\t\tesac; \n\n'

      + fairness_constraint(size) +
      '\n\n'
      + convergence_spec() +
      
      complete_segregation_spec(size) +

      level_of_segregation_spec(size) +

      
      '\n\n\n')
      
     file.close()
   except:
         print("error occured")
         sys.exit(0)

create()

