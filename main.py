name = input('\033[1;31;40m What is your name?\n')
print ('Hi, %s.\n' % name)
print ('Please answer the following questions so we can evaluate \n your Calculus skills\n')
question1= "What is derivative of 3x^3+2x?"
options1="(a) 9x^2+2\n(b) 5x\n(c) 9x^3+2\n(d) 3x^2+2\n"
print (question1) 
print (options1)
while True:
  response=input("select 'a', 'b', 'c' or 'd' for your answer \n")
  if response == "a":
    print ("Correct!")
    break
  else:
    print ("Incorrect. Please work on finding basic derviatives.")
    stop=True
    break

question2="\n Find the derivative of (x^3+3)^5"
options2="a)3x+3\nb)10x(x^2+6)\nc)15x^2(x^3+4)^4\nd)25x^3(x^2+4)^2"
print ( question2) 
print (options2)
while True:
  response=input("\n select 'a', 'b' 'c' or 'd' for your answer\n")
  if response == "c":
    print ("Correct\n")
    break
  else:
    print ("Incorrect. Please work on the chain rule.")
    stop=True
    break

question3="Find the derivative of x^2(-3x^2-2)"
options3="a)12x^3\nb)-12x^3-4x\nc)-3x^3+2\nd)6x^2+4x"
print ( question3) 
print (options3)
while True:
  response=input("\nselect 'a', 'b' 'c' or 'd' for your answer\n")
  if response == "b":
    print ("Correct\n")
    break
  else:
    print ("Incorrect. Please work on the product rule.")
    stop=True
    break

question4="Find the derivative of 2/x^5-5"
options4="a)10^2/x^3+4\nb)10x^4/x^10-10x^5+25\nc)5x^3+4/8\nd)4x^4/5x^2+5"
print ( question4) 
print (options4)
while True:
  response=input("\nselect 'a', 'b' 'c' or 'd' for your answer\n")
  if response == "b":
    print ("Correct\n")
    break
  else:
    print ("Incorrect. Please work on the quotient rule.")
    stop=True
    break
##alt turtle code below 
##name=input('What is the derivative of 3x^3+2x?\n')
##question=input(' "What is derivative of 3x^3+2x?\n\n\n(a) 9x^2+2\n(b) 5x\n(c) 9x^3+2\n(d) 3x^2+2\n')
##question = input[
   ## "What is derivative of 3x^3+2x?\n\n(a) 9x^2+2\n(b) 5x\n(c)9x^3+2\n(d) 3x^2+2\n ->\t",
     ##"What is 5 * 5 ?\n\n(a) 25 \n(b) 66\n(c) 100\n\n ->\t",
     ##"What is sin(90) ?\n\n(a) 1 \n(b) 69\n(c) 410\n\n ->\t",
     ##"What is cot(32) ?\n\n(a) 1.6 \n(b) 2.5\n(c) 3.4\n\n ->\t",]   
##class Question :

##questions = [
    ## Question(question[0], "a"),
     ##Question(question[1], "a"),
     ##Question(question[2], "a"),
     ##Question(question[3], "a"),
##]